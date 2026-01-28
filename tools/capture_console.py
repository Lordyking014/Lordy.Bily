#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
import sys
import os

URL = sys.argv[1] if len(sys.argv) > 1 else 'http://localhost:8000/'
OUT_DIR = os.path.join(os.path.dirname(__file__))

os.makedirs(OUT_DIR, exist_ok=True)
LOG_PATH = os.path.join(OUT_DIR, 'console_log.txt')
SHOT_PATH = os.path.join(OUT_DIR, 'screenshot.png')

logs = []

try:
    print('Starting Playwright...')
    with sync_playwright() as p:
        print('Launching Chromium...')
        browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
        page = browser.new_page()

        def handle_console(msg):
            try:
                text = msg.text()
            except Exception:
                text = str(msg)
            entry = f"{msg.type}: {text}"
            print(entry)
            logs.append(entry)

        page.on('console', handle_console)
        page.on('pageerror', lambda e: (print('pageerror:', e), logs.append('pageerror: ' + str(e))))

        print('Navigating to', URL)
        page.goto(URL, wait_until='networkidle', timeout=60000)
        print('Taking screenshot...')
        page.screenshot(path=SHOT_PATH, full_page=True)

        browser.close()

    with open(LOG_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(logs))

    print('\nSaved:', LOG_PATH)
    print('Saved:', SHOT_PATH)
except Exception as e:
    print('Error during capture:', e)
    import traceback
    traceback.print_exc()
    sys.exit(1)
