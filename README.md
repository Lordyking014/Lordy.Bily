# Lordy.Bily

Projeto estático de exemplo com páginas: `index.html`, `about.html`, `contact.html`.

Como rodar localmente:

```powershell
# Abrir página diretamente no navegador
start index.html

# Ou rodar um servidor local (Python)
python -m http.server 8000
# e abrir http://localhost:8000
```

Arquivos principais:
- `index.html` — página principal
- `about.html` — sobre
- `contact.html` — formulário demo
- `styles.css` — estilos
- `script.js` — comportamento JS
- `assets/favicon.svg` — favicon
# Deployment & Recommendations

- Para desenvolvimento rápido abra `index.html` ou use o servidor Python:

```powershell
python -m http.server 8000
# Abrir http://localhost:8000
```

- Para servir na rede, inicie o servidor ligado a `0.0.0.0` e permita a porta no firewall:

```powershell
# bind 0.0.0.0
python -m http.server 8000 --bind 0.0.0.0
# permitir porta (admin)
netsh advfirewall firewall add rule name="Local HTTP Server 8000" dir=in action=allow protocol=TCP localport=8000
```

- Para produção recomendo usar GitHub Pages (simples para sites estáticos) ou um host estático (Netlify, Vercel). Para Tailwind em produção:

1. Instale Node.js e npm.
2. Instale Tailwind como dependência e crie um build para `styles.css` (PostCSS/Tailwind CLI).

Exemplo mínimo:

```bash
npm init -y
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss -i ./src/input.css -o ./dist/styles.css --minify
```

Copie `dist/styles.css` e atualize `index.html` para apontar para o CSS local em vez da CDN.

Alternativa para debug rápido: usar `ngrok http 8000` para expor localmente sem configuração adicional.
# Lordy.Bily
Hello World
