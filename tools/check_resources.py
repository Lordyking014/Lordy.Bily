#!/usr/bin/env python3
import sys
import urllib.request
import urllib.parse
from html.parser import HTMLParser
from urllib.error import URLError, HTTPError

URL = sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8000/'

class ResourceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.resources = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'script' and 'src' in attrs:
            self.resources.add(attrs['src'])
        if tag == 'link' and attrs.get('rel','').lower() in ('stylesheet','preload','shortcut icon','icon') and 'href' in attrs:
            self.resources.add(attrs['href'])
        if tag == 'img' and 'src' in attrs:
            self.resources.add(attrs['src'])
        if tag == 'source' and 'src' in attrs:
            self.resources.add(attrs['src'])
        if tag == 'iframe' and 'src' in attrs:
            self.resources.add(attrs['src'])


def norm(url, base):
    return urllib.parse.urljoin(base, url)


def check_url(u):
    try:
        req = urllib.request.Request(u, headers={'User-Agent':'ResourceChecker/1.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            return (r.getcode(), len(r.read(1024)))
    except HTTPError as e:
        return (e.code, None)
    except URLError as e:
        return (None, str(e))
    except Exception as e:
        return (None, str(e))


def main():
    print('Fetching', URL)
    try:
        with urllib.request.urlopen(URL, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print('Error fetching main page:', e)
        sys.exit(2)

    p = ResourceParser()
    p.feed(html)
    resources = sorted(p.resources)
    results = []
    for res in resources:
        full = norm(res, URL)
        status, info = check_url(full)
        results.append((res, full, status, info))
        print(f'{res} -> {full}  status={status} info={info}')

    # Save report
    import os
    os.makedirs(os.path.dirname(__file__), exist_ok=True)
    report_path = os.path.join(os.path.dirname(__file__), 'resource_report.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('Resource check for ' + URL + '\n\n')
        for r in results:
            f.write(f'{r[0]} -> {r[1]}  status={r[2]} info={r[3]}\n')

    print('\nReport saved to', report_path)

if __name__ == '__main__':
    main()
