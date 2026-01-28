# HÓRUS MKT - Website

Agência de Marketing de Elite. Estratégia, Dados e Visão.

## 📁 Estrutura do Projeto

```
Lordy.Bily/
├── index.html                 # Página principal
├── package.json               # Dependências do projeto
├── tailwind.config.js         # Configuração do Tailwind CSS
├── postcss.config.js          # Configuração do PostCSS
├── src/
│   └── input.css             # CSS customizado (entrada do Tailwind)
├── dist/
│   └── styles.css            # CSS compilado (saída do Tailwind)
└── tools/
    ├── capture_console.py
    ├── check_resources.py
    └── resource_report.txt
```

## 🚀 Como Usar

### Instalação Inicial
```bash
npm install
```

### Desenvolvimento - Compilar CSS
Toda vez que modificar o HTML ou `src/input.css`, compile o CSS:
```bash
npm run build
```

Ou para compilação contínua:
```bash
npm run build:css
```

### Servidor Local
Para visualizar o site, inicie um servidor HTTP:
```bash
python -m http.server 8000
```

Acesse em: `http://localhost:8000`

## 🎨 Customização

### Cores
As cores estão definidas em `tailwind.config.js`:
- **Ouro (Gold)**: `#D4AF37`, `#FFD700`
- **Obsidiana (Dark)**: `#050505`, `#121212`

### Fontes
- **Display**: Cinzel (títulos principais)
- **Body**: Manrope (textos)

Ambas são importadas do Google Fonts no `<head>` do HTML.

### CSS Customizado
Adicione estilos personalizados em `src/input.css` e compile com `npm run build`.

## 📝 Seções do Site

1. **Navegação**: Menu flutuante com logo HÓRUS
2. **Hero**: Secção de impacto com CTA principal
3. **Método**: Estatísticas e valores (360°, ROI, 24/7, 100%)
4. **Serviços**: Grid Bento com 5 cards (Tráfego, Branding, Growth, Conteúdo)
5. **Agência**: Sobre com imagem e estatísticas
6. **Contacto**: Formulário de solicitação
7. **Footer**: Informações mínimas

## 🔧 Scripts Disponíveis

- `npm run build` - Compila CSS do Tailwind
- `npm run build:css` - Compila CSS do Tailwind (sem minificação)

## ✅ Arquitetura Corrigida

- ✅ Dependências instaladas e atualizadas
- ✅ CSS do Tailwind compilado em `dist/styles.css`
- ✅ `.gitignore` configurado
- ✅ Estrutura de pastas organizada
- ✅ Todas as referências de recursos validadas

---

**Desenvolvido em 28/01/2026**
