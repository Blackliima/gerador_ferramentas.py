# -*- coding: utf-8 -*-
import os
import urllib.parse
import urllib.request
import urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DOMINIO_SITE = "https://gerador-ferramentas-py.pages.dev"
MONETAG_SCRIPT = '<script src="https://quge5.com/88/tag.min.js" data-zone="309679" async data-cfasync="false"></script>'
GOOGLE_META = '<meta name="google-site-verification" content="pbgwZbVwgKMwqqqGYFcHeGGbV7EM7nBdlns1c_DN_Sw" />'
ADSENSE_SCRIPT = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5379027874215422" crossorigin="anonymous"></script>'

AD_BANNER = """
<div style="text-align:center; margin: 25px auto; background:var(--card-bg); padding:18px; border-radius:20px; box-shadow: 0 4px 20px rgba(0,0,0,0.04); border: 1px solid var(--border-color); max-width: 100%; overflow: hidden;">
    <p style="color:var(--text-light); font-size:10px; margin: 0 0 10px 0; text-transform: uppercase; letter-spacing: 2px; font-weight:800;">Publicidade</p>
    <div style="display: flex; justify-content: center; width: 100%;">
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
</div>
"""

RODAPE_AUTENTICO = """
<div style="font-size: 13px; color: var(--text-light); line-height: 1.6; margin-top: 40px; padding: 30px 20px; background: var(--card-bg); border-radius: 20px; border: 1px solid var(--border-color); text-align: center; box-shadow: 0 4px 20px rgba(0,0,0,0.02);">
    <div style="margin-bottom: 15px; display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
        <a href="index.html" style="color: var(--primary); text-decoration: none; font-weight: 700;">Início</a>
        <a href="faq.html" style="color: var(--primary); text-decoration: none; font-weight: 700;">FAQ</a>
        <a href="termos.html" style="color: var(--primary); text-decoration: none; font-weight: 700;">Termos de Uso</a>
    </div>
    <p style="margin: 0 0 6px 0;"><strong>Nexto Utilidades Práticas</strong> - A sua central definitiva de ferramentas online.</p>
    <p style="margin: 0;">© 2026 Todos os direitos reservados.</p>
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
    <title>Nexto Utilidades Práticas - Ferramentas Inteligentes para o Dia a Dia</title>
    <meta name="description" content="Otimize seu tempo com utilidades digitais de alta performance: gerador de fontes, links diretos do WhatsApp, contadores e compactadores inteligentes.">
    
    <meta property="og:title" content="Nexto Utilidades Práticas - Ferramentas Gratuitas">
    <meta property="og:description" content="Utilidades digitais rápidas e seguras direto no seu navegador.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://gerador-ferramentas-py.pages.dev/index.html">

    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Nexto Utilidades Práticas",
      "url": "https://gerador-ferramentas-py.pages.dev/",
      "potentialAction": {
        "@type": "SearchAction",
        "target": "https://gerador-ferramentas-py.pages.dev/index.html?q={search_term_string}",
        "query-input": "required name=search_term_string"
      }
    }
    </script>

    <link rel="manifest" href="manifest.json">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>">
    <style>
        :root { 
            --primary: #2563eb; --primary-dark: #1d4ed8; --bg-color: #f1f5f9; 
            --card-bg: #ffffff; --text: #0f172a; --text-light: #64748b; 
            --header-bg: linear-gradient(135deg, #2563eb, #1d4ed8); --border-color: #e2e8f0;
        }
        [data-theme="dark"] { 
            --primary: #3b82f6; --primary-dark: #60a5fa; --bg-color: #030712; 
            --card-bg: #111827; --text: #f9fafb; --text-light: #9ca3af; 
            --header-bg: linear-gradient(135deg, #1e3a8a, #172554); --border-color: #1f2937;
        }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: var(--text); background: var(--bg-color); margin: 0; padding: 0; transition: background 0.3s, color 0.3s; }
        .navbar { background: var(--card-bg); border-bottom: 1px solid var(--border-color); padding: 15px 20px; position: sticky; top: 0; z-index: 1000; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.03); }
        .logo { font-weight: 800; color: var(--primary); font-size: 18px; text-decoration: none; display: flex; align-items: center; gap: 8px; }
        .theme-btn { background: var(--bg-color); color: var(--text); border: 1px solid var(--border-color); padding: 8px 16px; border-radius: 20px; cursor: pointer; font-weight: 600; font-size: 13px; transition: all 0.2s; }
        .theme-btn:hover { border-color: var(--primary); }
        .container { max-width: 650px; margin: 25px auto; padding: 0 15px; }
        header { background: var(--header-bg); color: white; padding: 45px 25px; border-radius: 24px; margin-bottom: 25px; text-align: center; box-shadow: 0 12px 35px -10px rgba(37,99,235,0.35); }
        header h1 { margin: 0 0 12px 0; font-size: 26px; font-weight: 800; letter-spacing: -0.5px; }
        header p { margin: 0; opacity: 0.95; font-size: 15px; line-height: 1.6; }
        
        .search-box { margin-bottom: 25px; }
        .search-input { width: 100%; padding: 15px 20px; border: 1.5px solid var(--border-color); border-radius: 16px; background: var(--card-bg); color: var(--text); font-size: 15px; box-sizing: border-box; outline: none; box-shadow: 0 4px 15px rgba(0,0,0,0.02); transition: all 0.2s; }
        .search-input:focus { border-color: var(--primary); box-shadow: 0 4px 20px rgba(37,99,235,0.1); }

        .tools-grid { display: grid; grid-template-columns: 1fr; gap: 16px; }
        .tool-card { background: var(--card-bg); border: 1.5px solid var(--border-color); padding: 24px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.02); text-decoration: none; color: var(--text); display: block; transition: all 0.25s ease; }
        .tool-card:hover { transform: translateY(-3px); border-color: var(--primary); box-shadow: 0 10px 25px rgba(37,99,235,0.1); }
        .tool-card h3 { margin: 0 0 8px 0; color: var(--primary); font-size: 18px; display: flex; align-items: center; gap: 10px; font-weight: 700; }
        .tool-card p { margin: 0; font-size: 14px; color: var(--text-light); line-height: 1.5; }
        
        .seo-box { background: var(--card-bg); border: 1.5px solid var(--border-color); padding: 25px; border-radius: 24px; margin-top: 35px; box-shadow: 0 4px 15px rgba(0,0,0,0.02); }
        .seo-box h2 { font-size: 18px; color: var(--primary); margin-top: 0; margin-bottom: 12px; }
        .seo-box p { font-size: 14px; color: var(--text-light); line-height: 1.6; margin-bottom: 15px; }
        footer { text-align: center; margin-top: 35px; }
    </style>
</head>
<body data-theme="light">
    <div class="navbar">
        <a href="index.html" class="logo">⚡ Nexto Utilidades Práticas</a>
        <button class="theme-btn" onclick="toggleTheme()">🌓 Tema</button>
    </div>
    <div class="container">
        {{ ad_banner | safe }}
        
        <header>
            <h1>Sua produtividade em um só toque</h1>
            <p>Criamos utilidades digitais inteligentes e de alta performance para impulsionar seus negócios, redes sociais e tarefas diárias direto pelo celular — 100% gratuito e sem instalações.</p>
        </header>

        <div class="search-box">
            <input type="text" id="searchInput" class="search-input" placeholder="🔍 Buscar ferramenta rapidamente..." oninput="filtrarFerramentas()">
        </div>

        <div class="tools-grid" id="toolsGrid">
            <a href="fontes.html" class="tool-card" data-name="letras fontes instagram tiktok bio estilizadas">
                <h3>✨ Gerador de Letras & Fontes para Instagram</h3>
                <p>Dezenas de fontes estilizadas para bio, legendas e stories com cópia rápida em um toque.</p>
            </a>
            <a href="whatsapp.html" class="tool-card" data-name="whatsapp link mensagem conversa direto qr code">
                <h3>💬 Criador de Link WhatsApp & QR Code</h3>
                <p>Gere links com mensagens prontas e QR Code instantâneo para atendimento comercial.</p>
            </a>
            <a href="contador.html" class="tool-card" data-name="contador letras palavras texto tamanho limites">
                <h3>📊 Contador de Letras, Palavras & Redes</h3>
                <p>Meca caracteres, palavras e verifique o limite ideal para a bio do Instagram e posts.</p>
            </a>
            <a href="compressor.html" class="tool-card" data-name="compressor diminuir fotos imagens compactar leve">
                <h3>🖼️ Compressor de Fotos Inteligente</h3>
                <p>Reduza o peso de imagens direto no navegador com controle de qualidade e download ágil.</p>
            </a>
            <a href="conversor-texto.html" class="tool-card" data-name="conversor texto maiusculas minusculas caixa">
                <h3>🔤 Conversor de Letras Maiúsculas e Minúsculas</h3>
                <p>Transforme rapidamente seu texto inteiro em maiúsculas, minúsculas, capitalizado ou inverso.</p>
            </a>
            <a href="gerador-senhas.html" class="tool-card" data-name="gerador senhas forte seguras gerador">
                <h3>🔐 Gerador de Senhas Seguras</h3>
                <p>Crie senhas fortes e impenetráveis com letras, números e símbolos em segundos.</p>
            </a>
        </div>

        <div class="seo-box">
            <h2>Por que escolher o Nexto Utilidades Práticas?</h2>
            <p>Nossa missão é entregar uma experiência digital fluida, segura e de alto nível técnico. Desenvolvemos cada utilitário com foco em velocidade e eficiência para resolver problemas reais de empreendedores, criadores de conteúdo e usuários exigentes, tudo sem armazenar seus dados pessoais e com total privacidade.</p>
        </div>

        {{ ad_banner | safe }}
        <footer>
            {{ rodape_autentico | safe }}
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

        function filtrarFerramentas() {
            let termo = document.getElementById('searchInput').value.toLowerCase();
            let cards = document.querySelectorAll('.tool-card');
            cards.forEach(card => {
                let nome = card.getAttribute('data-name');
                if (nome.includes(termo)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }
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
    <title>{{ tool.title }} - Nexto Utilidades Práticas</title>
    <meta name="description" content="{{ tool.desc }}">
    
    <meta property="og:title" content="{{ tool.title }}">
    <meta property="og:description" content="{{ tool.desc }}">
    <meta property="og:type" content="article">

    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "{{ tool.title }}",
      "operatingSystem": "All",
      "applicationCategory": "UtilitiesApplication",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "BRL"
      }
    }
    </script>

    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>">
    <style>
        :root { 
            --primary: #2563eb; --primary-dark: #1d4ed8; --bg-color: #f1f5f9; 
            --card-bg: #ffffff; --text: #0f172a; --text-light: #64748b; 
            --header-bg: linear-gradient(135deg, #2563eb, #1d4ed8); --border-color: #e2e8f0;
        }
        [data-theme="dark"] { 
            --primary: #3b82f6; --primary-dark: #60a5fa; --bg-color: #030712; 
            --card-bg: #111827; --text: #f9fafb; --text-light: #9ca3af; 
            --header-bg: linear-gradient(135deg, #1e3a8a, #172554); --border-color: #1f2937;
        }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: var(--text); background: var(--bg-color); margin: 0; padding: 0; transition: background 0.3s, color 0.3s; }
        .navbar { background: var(--card-bg); border-bottom: 1px solid var(--border-color); padding: 15px 20px; position: sticky; top: 0; z-index: 1000; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.03); }
        .back-link { color: var(--primary); text-decoration: none; font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 6px; }
        .theme-btn { background: var(--bg-color); color: var(--text); border: 1px solid var(--border-color); padding: 8px 16px; border-radius: 20px; cursor: pointer; font-weight: 600; font-size: 13px; }
        .container { max-width: 650px; margin: 25px auto; padding: 0 15px; }
        .tool-box { background: var(--card-bg); border: 1.5px solid var(--border-color); padding: 25px 20px; border-radius: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); margin-bottom: 25px; }
        .tool-box h1 { margin: 0 0 10px 0; color: var(--primary); font-size: 22px; font-weight: 800; }
        .tool-box p { margin: 0 0 20px 0; font-size: 14px; color: var(--text-light); line-height: 1.5; }
        textarea, input[type="text"], input[type="url"], select { width: 100%; padding: 14px 16px; border: 1.5px solid var(--border-color); border-radius: 14px; background: var(--bg-color); color: var(--text); font-size: 15px; box-sizing: border-box; margin-bottom: 15px; outline: none; transition: border-color 0.2s; }
        textarea:focus, input:focus, select:focus { border-color: var(--primary); }
        button.action-btn { background: var(--primary); color: white; border: none; padding: 15px 20px; border-radius: 14px; font-weight: 700; font-size: 15px; cursor: pointer; width: 100%; transition: background 0.2s; box-shadow: 0 4px 15px rgba(37,99,235,0.25); }
        button.action-btn:hover { background: var(--primary-dark); }
        .output-item { display: flex; justify-content: space-between; align-items: center; padding: 14px 0; border-bottom: 1px solid var(--border-color); gap: 12px; }
        .output-item:last-child { border-bottom: none; }
        .copy-btn { background: var(--bg-color); border: 1.5px solid var(--border-color); color: var(--primary); padding: 8px 16px; border-radius: 10px; cursor: pointer; font-weight: 700; font-size: 13px; white-space: nowrap; transition: all 0.2s; }
        .copy-btn:hover { background: var(--primary); color: white; border-color: var(--primary); }
        
        .seo-content { background: var(--card-bg); border: 1.5px solid var(--border-color); padding: 25px; border-radius: 24px; margin-bottom: 25px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); }
        .seo-content h2 { font-size: 17px; color: var(--primary); margin-top: 0; margin-bottom: 10px; }
        .seo-content p { font-size: 14px; color: var(--text-light); line-height: 1.6; margin-bottom: 12px; }
        
        .cluster-links { background: var(--card-bg); border: 1.5px solid var(--border-color); padding: 20px; border-radius: 20px; margin-bottom: 25px; }
        .cluster-links h3 { font-size: 15px; color: var(--primary); margin-top: 0; margin-bottom: 10px; }
        .cluster-links ul { margin: 0; padding-left: 20px; font-size: 14px; color: var(--text-light); }
        .cluster-links li { margin-bottom: 6px; }
        .cluster-links a { color: var(--primary); text-decoration: none; font-weight: 600; }
        .cluster-links a:hover { text-decoration: underline; }

        footer { text-align: center; margin-top: 35px; }
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

        <div class="seo-content">
            <h2>Como funciona esta ferramenta?</h2>
            <p>{{ tool.seo_text }}</p>
            <h2 style="margin-top: 15px;">Dúvidas Frequentes</h2>
            <p><strong>É gratuito?</strong> Sim, todas as nossas utilidades rodam diretamente no navegador do seu celular ou computador sem custo.</p>
            <p><strong>Precisa instalar aplicativo?</strong> Não, tudo funciona online de forma rápida e leve.</p>
        </div>

        <div class="cluster-links">
            <h3>🔗 Outras Ferramentas Úteis para Você:</h3>
            <ul>
                <li><a href="fontes.html">Gerador de Letras & Fontes para Instagram</a></li>
                <li><a href="whatsapp.html">Criador de Link Direto para WhatsApp</a></li>
                <li><a href="contador.html">Contador de Letras e Palavras</a></li>
                <li><a href="compressor.html">Compressor Inteligente de Fotos</a></li>
                <li><a href="conversor-texto.html">Conversor de Letras Maiúsculas e Minúsculas</a></li>
                <li><a href="gerador-senhas.html">Gerador de Senhas Fortes e Seguras</a></li>
            </ul>
        </div>

        {{ ad_banner | safe }}
        <footer>
            {{ rodape_autentico | safe }}
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

STATIC_PAGES = {
    "faq.html": {
        "title": "Perguntas Frequentes (FAQ) - Nexto Utilidades Práticas",
        "desc": "Tire suas dúvidas sobre o uso das nossas ferramentas gratuitas para celular.",
        "content": """
            <h1>Perguntas Frequentes (FAQ)</h1>
            <p>Tire suas dúvidas rápidas sobre a nossa plataforma de utilidades.</p>
            <div style="margin-top: 20px;">
                <p><strong>1. As ferramentas são 100% gratuitas?</strong><br>Sim, todas as utilidades do site são totalmente gratuitas para uso ilimitado.</p>
                <p><strong>2. Preciso instalar algum aplicativo no celular?</strong><br>Não! Nenhuma ferramenta exige download. Tudo funciona direto no seu navegador com total leveza.</p>
                <p><strong>3. Meus dados ou fotos ficam salvos?</strong><br>Não. Processamentos como compressão de fotos e conversão de textos ocorrem inteiramente no seu próprio aparelho, garantindo privacidade absoluta.</p>
            </div>
        """
    },
    "termos.html": {
        "title": "Termos de Uso e Privacidade - Nexto Utilidades Práticas",
        "desc": "Conheça nossos termos de uso e políticas de privacidade.",
        "content": """
            <h1>Termos de Uso e Privacidade</h1>
            <p>A sua privacidade é prioridade para nós no Nexto Utilidades Práticas.</p>
            <div style="margin-top: 20px;">
                <p><strong>Uso das Ferramentas:</strong> Nossos utilitários são disponibilizados para auxílio pessoal, comercial e de marketing sem garantias de ganhos ou desempenho em plataformas de terceiros.</p>
                <p><strong>Anúncios e Cookies:</strong> Utilizamos redes de anúncios de terceiros (como Google AdSense e Monetag) para exibir publicidade relevante. Estas redes podem utilizar cookies para otimizar a exibição de anúncios.</p>
                <p><strong>Privacidade de Dados:</strong> Nenhum dado sensível inserido nas ferramentas de texto ou imagens é armazenado em nossos servidores.</p>
            </div>
        """
    }
}

FERRAMENTAS = {
    "fontes.html": {
        "title": "Gerador Avançado de Letras & Fontes",
        "desc": "Digite o seu texto abaixo e escolha entre dezenas de estilos de letras estilizadas para colar no Instagram, TikTok ou WhatsApp.",
        "seo_text": "Este gerador utiliza caracteres unicode especiais para transformar frases comuns em fontes estéticas e atraentes. Perfeito para destacar sua biografia do Instagram, legendas do TikTok ou mensagens em negrito no WhatsApp.",
        "html_content": """
            <textarea id="inputText" placeholder="Digite seu texto aqui..." oninput="gerarFontes()" style="height: 95px;">Nexto Prático</textarea>
            <div id="fontsOutput" style="margin-top: 15px;"></div>
            <script>
                const mapas = {
                    'Negrito Moderno': {'a': '𝗮','b': '𝗯','c': '𝗰','d': '𝗱','e': '𝗲','f': '𝗳','g': '𝗴','h': '𝗵','i': '𝗶','j': '𝗷','k': '𝗸','l': '𝗹','m': '𝗺','n': '𝗻','o': '𝗼','p': '𝗽','q': '𝗾','r': '𝗿','s': '𝘀','t': '𝘁','u': '𝘂','v': '𝘃','w': '𝘄','x': '𝘅','y': '𝘆','z': '𝘇', ' ' : ' '},
                    'Itálico Elegante': {'a': '𝘢','b': '𝘣','c': '𝘤','d': '𝘥','e': '𝘦','f': '𝘧','g': '𝘨','h': '𝘩','i': '𝘪','j': '𝘫','k': '𝘬','l': '𝘭','m': '𝘮','n': '𝘯','o': '𝘰','p': '𝘱','q': '𝘲','r': '𝘳','s': '𝘴','t': '𝘵','u': '𝘶','v': '𝘷','w': '𝘸','x': '𝘹','y': '𝘺','z': '𝘻', ' ' : ' '},
                    'Negrito Itálico': {'a': '𝙖','b': '𝙗','c': '𝙘','d': '𝙙','e': '𝙚','f': '𝙛','g': '𝙜','h': '𝙝','i': '𝙞','j': 'j','k': '𝙠','l': '𝙡','m': '𝙢','n': '𝙣','o': '𝙤','p': '𝙥','q': '𝙦','r': '𝙧','s': '𝙨','t': '𝙩','u': '𝙪','v': '𝙫','w': '𝙬','x': '𝙭','y': '𝙮','z': 'զ', ' ' : ' '},
                    'Letra Gótica': {'a': '𝔞','b': '𝔟','c': '𝔠','d': '𝔡','e': 'ⓔ','f': '𝔣','g': '𝔤','h': '𝔥','i': '𝔦','j': '𝔧','k': '𝔨','l': 'ℓ','m': '𝔪','n': '𝔫','o': '𝔬','p': '𝔭','q': '𝔮','r': '𝔯','s': '𝔰','t': '𝔱','u': '𝔲','v': '𝔳','w': '𝔴','x': '𝔵','y': '𝔶','z': '𝔃', ' ' : ' '},
                    'Letras Circuladas': {'a': 'ⓐ','b': 'ⓑ','c': 'ⓒ','d': 'ⓓ','e': 'ⓔ','f': 'ⓕ','g': 'ⓖ','h': 'ⓗ','i': 'ⓘ','j': 'ⓙ','k': 'ⓚ','l': 'ⓛ','m': 'ⓜ','n': 'ⓝ','o': 'ⓞ','p': 'ⓟ','q': 'ⓠ','r': 'ⓡ','s': 'ⓢ','t': 'ⓣ','u': 'ⓤ','v': 'ⓥ','w': 'ⓦ','x': 'ⓧ','y': 'ⓨ','z': 'ⓩ', ' ' : ' '},
                    'Espaçado Estiloso': {'a': '𝚊 ','b': '𝚋 ','c': '𝚌 ','d': '𝚍 ','e': '𝚎 ','f': '𝚏 ','g': '𝚐 ','h': '𝚑 ','i': '𝚒 ','j': '𝚓 ','k': '𝚔 ','l': '𝚕 ','m': '𝚖 ','n': '𝚗 ','o': '𝚘 ','p': '𝚙 ','q': '𝚚 ','r': '𝚛 ','s': '𝚜 ','t': '𝚝 ','u': '𝚞 ','v': '𝚟 ','w': '𝚠 ','x': '𝚡 ','y': '𝚢 ','z': '𝚣 ', ' ' : '   '}
                };
                function gerarFontes() {
                    let txt = document.getElementById('inputText').value;
                    let html = '';
                    for (let [estilo, mapa] of Object.entries(mapas)) {
                        let convertido = txt.split('').map(c => mapa[c.toLowerCase()] || c).join('');
                        html += `<div class="output-item"><div style="overflow:hidden;"><small style="color:var(--text-light); font-weight:700; font-size:11px; text-transform:uppercase;">${estilo}</small><div style="font-size:16px; font-weight:700; margin-top:3px; word-break:break-all;">${convertido}</div></div><button class="copy-btn" onclick="copiarTexto('${convertido}', this)">Copiar</button></div>`;
                    }
                    document.getElementById('fontsOutput').innerHTML = html;
                }
                gerarFontes();
            </script>
        """
    },
    "whatsapp.html": {
        "title": "Criador Profissional de Link WhatsApp",
        "desc": "Monte um link direto para o seu WhatsApp com mensagem automática e gere o QR Code para imprimir ou divulgar.",
        "seo_text": "O link direto do WhatsApp facilita o primeiro contato de potenciais clientes com o seu negócio. Basta inserir o número com o DDD e a mensagem padrão para gerar um link clicável e um QR Code pronto para uso em redes sociais e panfletos.",
        "html_content": """
            <label style="font-size:13px; font-weight:700; display:block; margin-bottom:6px; color:var(--text);">Seu Número (DDI + DDD + Número, ex: 5511999999999):</label>
            <input type="text" id="numeroWp" placeholder="5511999999999" value="5511999999999">
            
            <label style="font-size:13px; font-weight:700; display:block; margin-bottom:6px; color:var(--text);">Mensagem automática que o cliente vai enviar:</label>
            <textarea id="msgWp" placeholder="Digite a mensagem..." style="height:85px;">Olá! Vi seu site e gostaria de tirar dúvidas.</textarea>
            
            <button class="action-btn" onclick="gerarLinkWp()">Gerar Link & QR Code do WhatsApp</button>
            
            <div id="resultadoWp" style="margin-top:20px;"></div>
            
            <script>
                function gerarLinkWp() {
                    let num = document.getElementById('numeroWp').value.replace(/\\D/g,'');
                    let msg = encodeURIComponent(document.getElementById('msgWp').value);
                    let link = `https://wa.me/${num}?text=${msg}`;
                    let qrApi = `https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=${encodeURIComponent(link)}`;
                    
                    document.getElementById('resultadoWp').innerHTML = `
                        <div class="output-item" style="background:var(--bg-color); padding:14px; border-radius:12px; border:1.5px solid var(--border-color); display:block; margin-bottom:15px;">
                            <div style="font-size:12px; font-weight:700; color:var(--text-light); margin-bottom:6px;">SEU LINK DIRETO:</div>
                            <div style="word-break:break-all; font-size:13px; font-weight:600; margin-bottom:10px;">${link}</div>
                            <div style="display:flex; gap:10px;">
                                <button class="copy-btn" style="flex:1;" onclick="copiarTexto('${link}', this)">Copiar Link</button>
                                <a href="${link}" target="_blank" class="copy-btn" style="flex:1; text-align:center; text-decoration:none; display:inline-block; padding:8px;">Testar Conversa</a>
                            </div>
                        </div>
                        <div style="text-align:center; background:var(--bg-color); padding:15px; border-radius:12px; border:1.5px solid var(--border-color);">
                            <div style="font-size:12px; font-weight:700; color:var(--text-light); margin-bottom:10px;">QR CODE PARA DIVULGAÇÃO:</div>
                            <img src="${qrApi}" alt="QR Code WhatsApp" style="border-radius:8px; margin-bottom:10px; max-width:150px; background:#fff; padding:5px;">
                            <div><a href="${qrApi}" download="qrcode-whatsapp.png" class="copy-btn" style="text-decoration:none; display:inline-block;">Baixar Imagem do QR Code</a></div>
                        </div>
                    `;
                }
                gerarLinkWp();
            </script>
        """
    },
    "contador.html": {
        "title": "Contador de Textos & Limites",
        "desc": "Cole seu texto abaixo para ver estatísticas detalhadas de caracteres, palavras e adequação aos limites das redes sociais.",
        "seo_text": "Ideal para criadores de conteúdo, redatores e estudantes que precisam gerenciar o tamanho de postagens, redações ou biografias em redes sociais que possuem limites rígidos de caracteres.",
        "html_content": """
            <textarea id="textoContador" placeholder="Cole ou digite seu texto aqui..." oninput="contar()" style="height:140px;"></textarea>
            
            <div style="display:flex; gap:10px; margin-bottom:15px;">
                <button class="copy-btn" style="flex:1; padding:10px;" onclick="limparContador()">Limpar Texto 🗑️</button>
            </div>

            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px; margin-top:15px;">
                <div style="background:var(--bg-color); padding:16px; border-radius:14px; border:1.5px solid var(--border-color); text-align:center;">
                    <small style="color:var(--text-light); font-weight:700; font-size:12px; text-transform:uppercase;">Caracteres (com espaço)</small>
                    <div id="numChars" style="font-size:24px; font-weight:800; color:var(--primary); margin-top:4px;">0</div>
                </div>
                <div style="background:var(--bg-color); padding:16px; border-radius:14px; border:1.5px solid var(--border-color); text-align:center;">
                    <small style="color:var(--text-light); font-weight:700; font-size:12px; text-transform:uppercase;">Total de Palavras</small>
                    <div id="numPalavras" style="font-size:24px; font-weight:800; color:var(--primary); margin-top:4px;">0</div>
                </div>
            </div>

            <div style="margin-top:15px; background:var(--bg-color); padding:15px; border-radius:14px; border:1.5px solid var(--border-color);">
                <div style="font-size:13px; font-weight:700; margin-bottom:8px; color:var(--text);">Status para Redes Sociais:</div>
                <div id="statusBio" style="font-size:13px; color:var(--text-light); margin-bottom:4px;">• Bio do Instagram (Limite: 150 caracteres): <strong id="bioCount" style="color:var(--primary);">OK</strong></div>
                <div id="statusTwitter" style="font-size:13px; color:var(--text-light); margin-bottom:4px;">• Twitter / X (Limite: 280 caracteres): <strong id="twitterCount" style="color:var(--primary);">OK</strong></div>
                <div id="statusLeitura" style="font-size:13px; color:var(--text-light);">• Tempo estimado de leitura: <strong id="leituraTime" style="color:var(--primary);">0 segundos</strong></div>
            </div>

            <script>
                function contar() {
                    let val = document.getElementById('textoContador').value;
                    let chars = val.length;
                    let palavras = val.trim() === '' ? 0 : val.trim().split(/\\s+/).length;
                    
                    document.getElementById('numChars').innerText = chars;
                    document.getElementById('numPalavras').innerText = palavras;
                    
                    let bioEl = document.getElementById('bioCount');
                    if (chars <= 150) {
                        bioEl.innerText = `${chars}/150 (Cabe na Bio! ✔)`;
                        bioEl.style.color = '#16a34a';
                    } else {
                        bioEl.innerText = `${chars}/150 (Passou do limite ❌)`;
                        bioEl.style.color = '#dc2626';
                    }

                    let twEl = document.getElementById('twitterCount');
                    if (chars <= 280) {
                        twEl.innerText = `${chars}/280 (Permitido! ✔)`;
                        twEl.style.color = '#16a34a';
                    } else {
                        twEl.innerText = `${chars}/280 (Excede o limite ❌)`;
                        twEl.style.color = '#dc2626';
                    }
                    
                    let segundos = Math.ceil(palavras / 3);
                    document.getElementById('leituraTime').innerText = segundos < 60 ? `${segundos} seg` : `${Math.ceil(segundos/60)} min`;
                }
                function limparContador() {
                    document.getElementById('textoContador').value = '';
                    contar();
                }
            </script>
        """
    },
    "compressor.html": {
        "title": "Compressor de Fotos Inteligente",
        "desc": "Selecione uma foto da galeria do seu celular para reduzir o tamanho e o peso do arquivo de forma rápida e segura.",
        "seo_text": "Compacte imagens diretamente no seu dispositivo sem precisar enviar fotos pessoais para servidores externos. Otimize o espaço e envie arquivos mais leves para sites e redes sociais.",
        "html_content": """
            <input type="file" id="uploadImg" accept="image/*" style="margin-bottom:15px; font-size:14px; padding:12px; background:var(--bg-color); border:1.5px solid var(--border-color); border-radius:12px; width:100%; box-sizing:border-box;" onchange="comprimirImagem(event)">
            
            <div id="statusCompress" style="font-size:13px; font-weight:700; color:var(--text-light); margin-bottom:12px; text-align:center;"></div>
            <div id="resultadoCompress" style="text-align:center;"></div>
            
            <script>
                function comprimirImagem(e) {
                    let file = e.target.files[0];
                    if(!file) return;
                    
                    let tamanhoOriginalMB = (file.size / (1024*1024)).toFixed(2);
                    document.getElementById('statusCompress').innerText = `Foto original: ${tamanhoOriginalMB} MB. Compactando com alta eficiência...`;
                    
                    let reader = new FileReader();
                    reader.onload = function(event) {
                        let img = new Image();
                        img.src = event.target.result;
                        img.onload = function() {
                            let canvas = document.createElement('canvas');
                            let ctx = canvas.getContext('2d');
                            let maxW = 1000;
                            let scale = maxW / img.width;
                            if (scale > 1) scale = 1;
                            canvas.width = img.width * scale;
                            canvas.height = img.height * scale;
                            ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
                            
                            let dataUrl = canvas.toDataURL('image/jpeg', 0.75);
                            
                            // Calcula tamanho aproximado em base64
                            let base64Length = dataUrl.length - (dataUrl.indexOf(',') + 1);
                            let compressedSizeMB = ((base64Length * 0.75) / (1024*1024)).toFixed(2);
                            
                            document.getElementById('statusCompress').innerText = `Pronto! Novo peso estimado: ~${compressedSizeMB} MB (Otimizada com sucesso ✔)`;
                            document.getElementById('resultadoCompress').innerHTML = `
                                <a href="${dataUrl}" download="foto-otimizada-nexto.jpg" class="action-btn" style="text-decoration:none; display:block; text-align:center; padding:15px;">Baixar Foto Compactada Agora</a>
                            `;
                        }
                    }
                    reader.readAsDataURL(file);
                }
            </script>
        """
    },
    "conversor-texto.html": {
        "title": "Conversor de Letras Maiúsculas e Minúsculas",
        "desc": "Alterne instantaneamente o formato do seu texto entre letras maiúsculas, minúsculas, formato de título ou invertido.",
        "seo_text": "Ferramenta essencial para formatar artigos, títulos ou mensagens rapidamente. Corrija o formato de blocos de texto inteiros com apenas um clique.",
        "html_content": """
            <textarea id="textoConv" placeholder="Digite ou cole seu texto aqui..." style="height:120px;" oninput="converterTudo()"></textarea>
            
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px; margin-bottom:15px;">
                <button class="copy-btn" style="padding:10px;" onclick="mudarModo('maiusc')">MAIÚSCULAS</button>
                <button class="copy-btn" style="padding:10px;" onclick="mudarModo('minusc')">minúsculas</button>
                <button class="copy-btn" style="padding:10px;" onclick="mudarModo('titulo')">Primeira Letra Maiúscula</button>
                <button class="copy-btn" style="padding:10px;" onclick="mudarModo('inverso')">Inverter Texto</button>
            </div>

            <div id="resConvOut"></div>

            <script>
                function mudarModo(tipo) {
                    let txt = document.getElementById('textoConv').value;
                    let res = '';
                    if(tipo === 'maiusc') res = txt.toUpperCase();
                    if(tipo === 'minusc') res = txt.toLowerCase();
                    if(tipo === 'titulo') res = txt.toLowerCase().replace(/(^|\\s)\\S/g, l => l.toUpperCase());
                    if(tipo === 'inverso') res = txt.split('').reverse().join('');
                    
                    document.getElementById('resConvOut').innerHTML = `
                        <div class="output-item" style="background:var(--bg-color); padding:14px; border-radius:12px; border:1.5px solid var(--border-color); display:block;">
                            <div style="word-break:break-all; font-size:14px; font-weight:600; margin-bottom:10px;">${res}</div>
                            <button class="copy-btn" style="width:100%;" onclick="copiarTexto('${res.replace(/'/g, "\\\\'")}', this)">Copiar Texto Convertido</button>
                        </div>
                    `;
                }
                function converterTudo() { mudarModo('maiusc'); }
            </script>
        """
    },
    "gerador-senhas.html": {
        "title": "Gerador de Senhas Seguras",
        "desc": "Proteja suas contas criando senhas fortes, complexas e aleatórias com letras, números e símbolos.",
        "seo_text": "A segurança digital começa com senhas robustas. Utilize nosso gerador para criar combinações aleatórias difíceis de adivinhar por softwares maliciosos.",
        "html_content": """
            <div style="background:var(--bg-color); padding:20px; border-radius:16px; border:1.5px solid var(--border-color); text-align:center; margin-bottom:15px;">
                <div id="senhaGerada" style="font-size:20px; font-weight:800; color:var(--primary); word-break:break-all; margin-bottom:15px;">Clique no botão abaixo</div>
                <button class="action-btn" onclick="gerarSenha()">Gerar Nova Senha Forte</button>
            </div>
            <script>
                function gerarSenha() {
                    let chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%&*!+=?";
                    let senha = "";
                    for (let i = 0; i < 16; i++) {
                        senha += chars.charAt(Math.floor(Math.random() * chars.length));
                    }
                    document.getElementById('senhaGerada').innerHTML = `
                        <div>${senha}</div>
                        <button class="copy-btn" style="margin-top:12px;" onclick="copiarTexto('${senha}', this)">Copiar Senha</button>
                    `;
                }
                gerarSenha();
            </script>
        """
    }
}

def gerar_manifest():
    manifest_content = """{
  "name": "Nexto Utilidades Práticas",
  "short_name": "Nexto",
  "start_url": "/index.html",
  "display": "standalone",
  "background_color": "#f1f5f9",
  "theme_color": "#2563eb",
  "icons": [
    {
      "src": "data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>",
      "sizes": "192x192 512x512",
      "type": "image/svg+xml"
    }
  ]
}"""
    with open("manifest.json", "w", encoding="utf-8") as f:
        f.write(manifest_content)

def gerar_sitemap():
    data_hoje = datetime.now().strftime("%Y-%m-%d")
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml.append(f'  <url><loc>{DOMINIO_SITE}/index.html</loc><lastmod>{data_hoje}</lastmod><changefreq>daily</changefreq><priority>1.0</priority></url>')
    for f_nome in FERRAMENTAS.keys():
        xml.append(f'  <url><loc>{DOMINIO_SITE}/{f_nome}</loc><lastmod>{data_hoje}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>')
    for s_nome in STATIC_PAGES.keys():
        xml.append(f'  <url><loc>{DOMINIO_SITE}/{s_nome}</loc><lastmod>{data_hoje}</lastmod><changefreq>monthly</changefreq><priority>0.5</priority></url>')
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
    print("Gerando Nexto Utilidades Práticas com o ápice da performance e usabilidade...")
    from jinja2 import Template
    
    gerar_manifest()
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(Template(INDEX_TEMPLATE).render(ad_banner=AD_BANNER, adsense_script=ADSENSE_SCRIPT, monetag_script=MONETAG_SCRIPT, google_meta=GOOGLE_META, rodape_autentico=RODAPE_AUTENTICO))
    
    static_layout = Template("""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {{ adsense_script | safe }}
        {{ monetag_script | safe }}
        {{ google_meta | safe }}
        <title>{{ page.title }}</title>
        <meta name="description" content="{{ page.desc }}">
        <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>">
        <style>
            :root { 
                --primary: #2563eb; --primary-dark: #1d4ed8; --bg-color: #f1f5f9; 
                --card-bg: #ffffff; --text: #0f172a; --text-light: #64748b; --border-color: #e2e8f0;
            }
            [data-theme="dark"] { 
                --primary: #3b82f6; --primary-dark: #60a5fa; --bg-color: #030712; 
                --card-bg: #111827; --text: #f9fafb; --text-light: #9ca3af; --border-color: #1f2937;
            }
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: var(--text); background: var(--bg-color); margin: 0; padding: 0; }
            .navbar { background: var(--card-bg); border-bottom: 1px solid var(--border-color); padding: 15px 20px; position: sticky; top: 0; z-index: 1000; display: flex; justify-content: space-between; align-items: center; }
            .back-link { color: var(--primary); text-decoration: none; font-weight: 700; font-size: 14px; display: flex; align-items: center; gap: 6px; }
            .container { max-width: 650px; margin: 25px auto; padding: 0 15px; }
            .content-box { background: var(--card-bg); border: 1.5px solid var(--border-color); padding: 30px 25px; border-radius: 24px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); margin-bottom: 25px; }
            .content-box h1 { color: var(--primary); font-size: 24px; margin-top: 0; }
            .content-box p { color: var(--text-light); font-size: 14px; line-height: 1.7; }
            footer { text-align: center; margin-top: 35px; }
        </style>
    </head>
    <body data-theme="light">
        <div class="navbar">
            <a href="index.html" class="back-link">← Voltar ao Início</a>
        </div>
        <div class="container">
            {{ ad_banner | safe }}
            <div class="content-box">
                {{ page.content | safe }}
            </div>
            {{ ad_banner | safe }}
            <footer>
                {{ rodape_autentico | safe }}
            </footer>
        </div>
    </body>
    </html>
    """)
    
    for filename, pdata in STATIC_PAGES.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(static_layout.render(page=pdata, ad_banner=AD_BANNER, adsense_script=ADSENSE_SCRIPT, monetag_script=MONETAG_SCRIPT, google_meta=GOOGLE_META, rodape_autentico=RODAPE_AUTENTICO))

    t_layout = Template(TOOL_LAYOUT)
    for filename, data in FERRAMENTAS.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(t_layout.render(tool=data, ad_banner=AD_BANNER, adsense_script=ADSENSE_SCRIPT, monetag_script=MONETAG_SCRIPT, google_meta=GOOGLE_META, rodape_autentico=RODAPE_AUTENTICO))
            
    gerar_sitemap()
    send_search_engine_pings()
    print("Sucesso absoluto! Todas as ferramentas foram aprimoradas com funções inteligentes.")

if __name__ == "__main__":
    gerar_site()
