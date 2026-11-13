import os
import urllib.parse
import urllib.request
import urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DOMINIO_SITE = "https://gerador-ferramentas.pages.dev"
MONETAG_SCRIPT = '<script src="https://quge5.com/88/tag.min.js" data-zone="309679" async data-cfasync="false"></script>'
GOOGLE_META = '<meta name="google-site-verification" content="pbgwZbVwgKMwqqqGYFcHeGGbV7EM7nBdlns1c_DN_Sw" />'
ADSENSE_SCRIPT = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5379027874215422" crossorigin="anonymous"></script>'

AD_BANNER = """
<div style="text-align:center; margin: 20px 0; background:var(--card-bg); padding:15px; border-radius:12px; box-shadow: 0 4px 12px rgba(0,0,0,0.04); border: 1px dashed rgba(0,0,0,0.1);">
    <p style="color:var(--text-light); font-size:10px; margin-bottom:6px; text-transform: uppercase; letter-spacing: 1.5px; font-weight:600;">Publicidade Patrocinada</p>
    <script type="text/javascript">
        atOptions = {
            'key' : '7d8438dbf1b7a796906a9575be2722b3',
            'format' : 'iframe',
            'height' : 250,
            'width' : 300,
            'params' : {}
        };
    </script>
    <script type="text/javascript" src="https://bauval.org/22/7d8438dbf1b7a796906a9575be2722b3"></script>
</div>
"""

LICENCA_RODAPE = """
<div style="font-size: 12px; color: var(--text-light); line-height: 1.5; margin-top: 30px; padding: 20px; background: var(--card-bg); border-radius: 12px; border: 1px solid var(--border-color); text-align: center;">
    <p style="margin: 0 0 8px 0;"><strong>Ferramentas Gratuitas Mobile:</strong> Processamento 100% no seu navegador com total privacidade.</p>
    <p style="margin: 0;">© 2026 Ferramentas Rápidas. Todos os direitos reservados.</p>
</div>
"""

INDEX_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {{ adsense_script | safe }}
    {{ monetag_script | safe }}
    {{ google_meta | safe }}
    <title>Central de Ferramentas Rápidas - Utilitários para Celular</title>
    <meta name="description" content="Ferramentas online gratuitas para celular: gerador de fontes para Instagram, encurtador de link para WhatsApp, compressor de imagens e contador de caracteres.">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>">
    <style>
        :root { 
            --primary: #2563eb; --primary-dark: #1d4ed8; --bg-color: #f8fafc; 
            --card-bg: #ffffff; --text: #0f172a; --text-light: #64748b; 
            --header-bg: linear-gradient(135deg, #0f172a, #1e3a8a); --border-color: #e2e8f0;
        }
        [data-theme="dark"] { 
            --primary: #3b82f6; --primary-dark: #60a5fa; --bg-color: #030712; 
            --card-bg: #111827; --text: #f9fafb; --text-light: #9ca3af; 
            --header-bg: linear-gradient(135deg, #020617, #0f172a); --border-color: #1f2937;
        }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.5; color: var(--text); background: var(--bg-color); margin: 0; padding: 0; transition: background 0.3s, color 0.3s; }
        .navbar { background: var(--card-bg); border-bottom: 1px solid var(--border-color); padding: 12px 20px; position: sticky; top: 0; z-index: 1000; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
        .logo { font-weight: 800; color: var(--primary); font-size: 16px; text-decoration: none; }
        .theme-btn { background: var(--bg-color); color: var(--text); border: 1px solid var(--border-color); padding: 6px 12px; border-radius: 20px; cursor: pointer; font-weight: 600; font-size: 12px; }
        .container { max-width: 700px; margin: 20px auto; padding: 0 15px; }
        header { background: var(--header-bg); color: white; padding: 30px 20px; border-radius: 16px; margin-bottom: 25px; text-align: center; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1); }
        header h1 { margin: 0 0 10px 0; font-size: 26px; font-weight: 800; }
        header p { margin: 0; opacity: 0.9; font-size: 14px; }
        .tools-grid { display: grid; grid-template-columns: 1fr; gap: 15px; }
        .tool-card { background: var(--card-bg); border: 1px solid var(--border-color); padding: 20px; border-radius: 14px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); text-decoration: none; color: var(--text); display: block; transition: transform 0.2s, border-color 0.2s; }
        .tool-card:hover { transform: translateY(-2px); border-color: var(--primary); }
        .tool-card h3 { margin: 0 0 6px 0; color: var(--primary); font-size: 18px; display: flex; align-items: center; gap: 8px; }
        .tool-card p { margin: 0; font-size: 13px; color: var(--text-light); }
        footer { text-align: center; margin-top: 40px; padding-bottom: 20px; }
    </style>
</head>
<body data-theme="light">
    <div class="navbar">
        <a href="index.html" class="logo">⚡ FastTools Mobile</a>
        <button class="theme-btn" onclick="toggleTheme()">🌓 Tema</button>
    </div>
    <div class="container">
        {{ ad_banner | safe }}
        <header>
            <h1>Utilitários para Celular</h1>
            <p>Ferramentas rápidas, leves e sem cadastro para o seu dia a dia.</p>
        </header>

        <div class="tools-grid">
            <a href="fontes.html" class="tool-card">
                <h3>✨ Gerador de Fontes para Instagram</h3>
                <p>Transforme seu texto comum em letras estilizadas para Bio e Stories com um clique.</p>
            </a>
            <a href="whatsapp.html" class="tool-card">
                <h3>💬 Gerador de Link para WhatsApp</h3>
                <p>Crie links diretos com mensagens prontas para atendimento ou negócios.</p>
            </a>
            <a href="contador.html" class="tool-card">
                <h3>📊 Contador de Caracteres & Palavras</h3>
                <p>Conte letras, palavras e parágrafos instantaneamente para legendas e redações.</p>
            </a>
            <a href="compressor.html" class="tool-card">
                <h3>🖼️ Compressor de Imagens Leve</h3>
                <p>Reduza o tamanho de fotos direto no navegador sem perder qualidade.</p>
            </a>
        </div>

        {{ ad_banner | safe }}
        <footer>
            {{ licenca_rodape | safe }}
        </footer>
    </div>
    <script>
        function toggleTheme() {
            const body = document.body;
            const nextTheme = body.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
            body.setAttribute('data-theme', nextTheme);
            localStorage.setItem('theme', nextTheme);
        }
        if (localStorage.getItem('theme') === 'dark') { document.body.setAttribute('data-theme', 'dark'); }
    </script>
</body>
</html>
"""

TOOL_LAYOUT = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {{ adsense_script | safe }}
    {{ monetag_script | safe }}
    {{ google_meta | safe }}
    <title>{{ tool.title }} - FastTools Mobile</title>
    <meta name="description" content="{{ tool.desc }}">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>">
    <style>
        :root { 
            --primary: #2563eb; --primary-dark: #1d4ed8; --bg-color: #f8fafc; 
            --card-bg: #ffffff; --text: #0f172a; --text-light: #64748b; 
            --header-bg: linear-gradient(135deg, #0f172a, #1e3a8a); --border-color: #e2e8f0;
        }
        [data-theme="dark"] { 
            --primary: #3b82f6; --primary-dark: #60a5fa; --bg-color: #030712; 
            --card-bg: #111827; --text: #f9fafb; --text-light: #9ca3af; 
            --header-bg: linear-gradient(135deg, #020617, #0f172a); --border-color: #1f2937;
        }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.5; color: var(--text); background: var(--bg-color); margin: 0; padding: 0; transition: background 0.3s, color 0.3s; }
        .navbar { background: var(--card-bg); border-bottom: 1px solid var(--border-color); padding: 12px 20px; position: sticky; top: 0; z-index: 1000; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
        .back-link { color: var(--primary); text-decoration: none; font-weight: 600; font-size: 14px; }
        .theme-btn { background: var(--bg-color); color: var(--text); border: 1px solid var(--border-color); padding: 6px 12px; border-radius: 20px; cursor: pointer; font-weight: 600; font-size: 12px; }
        .container { max-width: 700px; margin: 20px auto; padding: 0 15px; }
        .tool-box { background: var(--card-bg); border: 1px solid var(--border-color); padding: 25px 20px; border-radius: 16px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02); margin-bottom: 25px; }
        .tool-box h1 { margin: 0 0 8px 0; color: var(--primary); font-size: 22px; }
        .tool-box p { margin: 0 0 20px 0; font-size: 14px; color: var(--text-light); }
        textarea, input[type="text"], input[type="url"] { width: 100%; padding: 12px; border: 1px solid var(--border-color); border-radius: 10px; background: var(--bg-color); color: var(--text); font-size: 15px; box-sizing: border-box; margin-bottom: 15px; outline: none; }
        textarea:focus, input:focus { border-color: var(--primary); }
        button.action-btn { background: var(--primary); color: white; border: none; padding: 12px 20px; border-radius: 10px; font-weight: 700; font-size: 15px; cursor: pointer; width: 100%; transition: background 0.2s; }
        button.action-btn:hover { background: var(--primary-dark); }
        .output-area { margin-top: 15px; background: var(--bg-color); border: 1px solid var(--border-color); padding: 15px; border-radius: 10px; word-break: break-all; }
        .output-item { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid var(--border-color); }
        .output-item:last-child { border-bottom: none; }
        .copy-btn { background: var(--card-bg); border: 1px solid var(--border-color); color: var(--primary); padding: 6px 12px; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 12px; }
        .copy-btn:hover { background: var(--primary); color: white; }
        footer { text-align: center; margin-top: 40px; padding-bottom: 20px; }
    </style>
</head>
<body data-theme="light">
    <div class="navbar">
        <a href="index.html" class="back-link">← Voltar ao Início</a>
        <button class="theme-btn" onclick="toggleTheme()">🌓 Tema</button>
    </div>
    <div class="container">
        {{ ad_banner | safe }}
        
        <div class="tool-box">
            <h1>{{ tool.title }}</h1>
            <p>{{ tool.desc }}</p>
            {{ tool.html_content | safe }}
        </div>

        {{ ad_banner | safe }}
        <footer>
            {{ licenca_rodape | safe }}
        </footer>
    </div>
    <script>
        function toggleTheme() {
            const body = document.body;
            const nextTheme = body.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
            body.setAttribute('data-theme', nextTheme);
            localStorage.setItem('theme', nextTheme);
        }
        if (localStorage.getItem('theme') === 'dark') { document.body.setAttribute('data-theme', 'dark'); }
        
        function copiarTexto(texto, btn) {
            navigator.clipboard.writeText(texto);
            let original = btn.innerText;
            btn.innerText = "Copiado! ✔";
            setTimeout(() => btn.innerText = original, 2000);
        }
    </script>
</body>
</html>
"""

# HTMLs específicos para cada ferramenta interativa
FERRAMENTAS = {
    "fontes.html": {
        "title": "Gerador de Fontes para Instagram",
        "desc": "Digite seu texto e copie fontes estilizadas instantaneamente para usar na sua Bio ou nos Stories.",
        "html_content": """
            <textarea id="inputText" placeholder="Digite seu texto aqui..." oninput="gerarFontes()">FastTools</textarea>
            <div id="fontsOutput" style="margin-top: 20px;"></div>
            <script>
                const mapas = {
                    'Gótica': {'a': '𝔞','b': '𝔟','c': '𝔠','d': '𝔡','e': 'ⓔ','f': '𝔣','g': '𝔤','h': '𝔥','i': '𝔦','j': '𝔧','k': '𝔨','l': 'ℓ','m': '𝔪','n': '𝔫','o': '𝔬','p': '𝔭','q': '𝔮','r': '𝔯','s': '𝔰','t': '𝔱','u': '𝔲','v': '𝔳','w': '𝔴','x': '𝔵','y': '𝔶','z': '𝔟'},
                    'Negrito Sans': {'a': '𝗮','b': '𝗯','c': '𝗰','d': '𝗱','e': '𝗲','f': '𝗳','g': '𝗴','h': '𝗵','i': '𝗶','j': '𝗷','k': '𝗸','l': '𝗹','m': '𝗺','n': '𝗻','o': '𝗼','p': '𝗽','q': '𝗾','r': '𝗿','s': '𝘀','t': '𝘁','u': '𝘂','v': '𝘃','w': '𝘄','x': '𝘅','y': '𝘆','z': '𝘇'},
                    'Itálico': {'a': '𝘢','b': '𝘣','c': '𝘤','d': '𝘥','e': '𝘦','f': '𝘧','g': '𝘨','h': '𝘩','i': '𝘪','j': '𝘫','k': '𝘬','l': '𝘭','m': '𝘮','n': '𝘯','o': '𝘰','p': '𝘱','q': '𝘲','r': '𝘳','s': '𝘴','t': '𝘵','u': '𝘶','v': '𝘷','w': '𝘸','x': '𝘹','y': '𝘺','z': '𝘻'},
                    'Espaçado': {'a': '𝚊 ','b': '𝚋 ','c': '𝚌 ','d': '𝚍 ','e': '𝚎 ','f': '𝚏 ','g': '𝚐 ','h': '𝚑 ','i': '𝚒 ','j': '𝚓 ','k': '𝚔 ','l': '𝚕 ','m': '𝚖 ','n': '𝚗 ','o': '𝚘 ','p': '𝚙 ','q': '𝚚 ','r': '𝚛 ','s': '𝚜 ','t': '𝚝 ','u': '𝚞 ','v': '𝚟 ','w': '𝚠 ','x': '𝚡 ','y': '𝚢 ','z': '𝚣 '}
                };
                function gerarFontes() {
                    let txt = document.getElementById('inputText').value;
                    let html = '';
                    for (let [estilo, mapa] of Object.entries(mapas)) {
                        let convertido = txt.split('').map(c => mapa[c.toLowerCase()] || c).join('');
                        html += `<div class="output-item"><div><small style="color:var(--text-light)">${estilo}</small><br><strong>${convertido}</strong></div><button class="copy-btn" onclick="copiarTexto('${convertido}', this)">Copiar</button></div>`;
                    }
                    document.getElementById('fontsOutput').innerHTML = html;
                }
                gerarFontes();
            </script>
        """
    },
    "whatsapp.html": {
        "title": "Gerador de Link para WhatsApp",
        "desc": "Crie um link direto para o seu WhatsApp com uma mensagem automática.",
        "html_content": """
            <label style="font-size:13px; font-weight:600; display:block; margin-bottom:5px;">Seu Número (com DDD e DDI, ex: 5511999999999):</label>
            <input type="text" id="numeroWp" placeholder="5511988887777" value="5511999999999">
            <label style="font-size:13px; font-weight:600; display:block; margin-bottom:5px;">Mensagem Automática:</label>
            <textarea id="msgWp" placeholder="Olá, gostaria de mais informações...">Olá, vim pelo site e quero tirar dúvidas!</textarea>
            <button class="action-btn" onclick="gerarLinkWp()">Gerar Link do WhatsApp</button>
            <div id="resultadoWp" style="margin-top:15px;"></div>
            <script>
                function gerarLinkWp() {
                    let num = document.getElementById('numeroWp').value.replace(/\\D/g,'');
                    let msg = encodeURIComponent(document.getElementById('msgWp').value);
                    let link = `https://wa.me/${num}?text=${msg}`;
                    document.getElementById('resultadoWp').innerHTML = `<div class="output-item"><div style="word-break:break-all; font-size:13px;"><strong>${link}</strong></div><button class="copy-btn" onclick="copiarTexto('${link}', this)">Copiar Link</button></div>`;
                }
            </script>
        """
    },
    "contador.html": {
        "title": "Contador de Caracteres & Palavras",
        "desc": "Cole seu texto abaixo para contar caracteres, palavras e linhas em tempo real.",
        "html_content": """
            <textarea id="textoContador" placeholder="Digite ou cole seu texto aqui..." onrows="6" oninput="contar()" style="height:120px;"></textarea>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px; margin-top:10px;">
                <div style="background:var(--bg-color); padding:15px; border-radius:10px; border:1px solid var(--border-color); text-align:center;">
                    <small style="color:var(--text-light)">Caracteres</small>
                    <div id="numChars" style="font-size:22px; font-weight:bold; color:var(--primary);">0</div>
                </div>
                <div style="background:var(--bg-color); padding:15px; border-radius:10px; border:1px solid var(--border-color); text-align:center;">
                    <small style="color:var(--text-light)">Palavras</small>
                    <div id="numPalavras" style="font-size:22px; font-weight:bold; color:var(--primary);">0</div>
                </div>
            </div>
            <script>
                function contar() {
                    let val = document.getElementById('textoContador').value;
                    document.getElementById('numChars').innerText = val.length;
                    let palavras = val.trim() === '' ? 0 : val.trim().split(/\\s+/).length;
                    document.getElementById('numPalavras').innerText = palavras;
                }
            </script>
        """
    },
    "compressor.html": {
        "title": "Compressor de Imagens Leve",
        "desc": "Selecione uma foto da galeria do celular para redimensionar e compactar rapidamente.",
        "html_content": """
            <input type="file" id="uploadImg" accept="image/*" style="margin-bottom:15px;" onchange="comprimirImagem(event)">
            <div id="statusCompress" style="font-size:13px; color:var(--text-light);"></div>
            <div id="resultadoCompress" style="margin-top:15px; text-align:center;"></div>
            <script>
                function comprimirImagem(e) {
                    let file = e.target.files[0];
                    if(!file) return;
                    document.getElementById('statusCompress').innerText = "Processando imagem...";
                    let reader = new FileReader();
                    reader.onload = function(event) {
                        let img = new Image();
                        img.src = event.target.result;
                        img.onload = function() {
                            let canvas = document.createElement('canvas');
                            let ctx = canvas.getContext('2d');
                            let maxW = 800;
                            let scale = maxW / img.width;
                            canvas.width = maxW;
                            canvas.height = img.height * scale;
                            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
                            let dataUrl = canvas.toDataURL('image/jpeg', 0.7);
                            document.getElementById('statusCompress').innerText = "Pronto! Clique abaixo para baixar.";
                            document.getElementById('resultadoCompress').innerHTML = `<a href="${dataUrl}" download="imagem-compactada.jpg" class="action-btn" style="text-decoration:none; display:inline-block; padding:12px;">Baixar Imagem Otimizada</a>`;
                        }
                    }
                    reader.readAsDataURL(file);
                }
            </script>
        """
    }
}

def gerar_sitemap():
    data_hoje = datetime.now().strftime("%Y-%m-%d")
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml.append(f'  <url><loc>{DOMINIO_SITE}/index.html</loc><lastmod>{data_hoje}</lastmod><changefreq>daily</changefreq><priority>1.0</priority></url>')
    for f_nome in FERRAMENTAS.keys():
        xml.append(f'  <url><loc>{DOMINIO_SITE}/{f_nome}</loc><lastmod>{data_hoje}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>')
    xml.append('</urlset>')
    with open("sitemap.xml", "w", encoding="utf-8") as f: f.write("\n".join(xml))

def send_search_engine_pings():
    sitemap_url = f"{DOMINIO_SITE}/sitemap.xml"
    encoded_sitemap = urllib.parse.quote(sitemap_url, safe='')
    pings = [
        f"https://www.google.com/ping?sitemap={encoded_sitemap}",
        f"https://www.bing.com/ping?sitemap={encoded_sitemap}"
    ]
    print("🚀 Disparando pings de SEO automáticos...")
    for url in pings:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Compatible; FastToolsBot/1.0)'})
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.status == 200: print(f"✔ Ping enviado para: {url.split('/')[2]}")
        except Exception as e:
            print(f"[Aviso] Ping offline: {e}")

def gerar_site():
    print("Gerando Central de Ferramentas Mobile-First...")
    from jinja2 import Template
    
    # Gerar index
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(Template(INDEX_TEMPLATE).render(ad_banner=AD_BANNER, adsense_script=ADSENSE_SCRIPT, monetag_script=MONETAG_SCRIPT, google_meta=GOOGLE_META, licenca_rodape=LICENCA_RODAPE))
    
    # Gerar páginas das ferramentas
    t_layout = Template(TOOL_LAYOUT)
    for filename, data in FERRAMENTAS.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(t_layout.render(tool=data, ad_banner=AD_BANNER, adsense_script=ADSENSE_SCRIPT, monetag_script=MONETAG_SCRIPT, google_meta=GOOGLE_META, licenca_rodape=LICENCA_RODAPE))
            
    gerar_sitemap()
    send_search_engine_pings()
    print("Sucesso absoluto! Central de ferramentas gerada com sucesso.")

if __name__ == "__main__":
    gerar_site()
