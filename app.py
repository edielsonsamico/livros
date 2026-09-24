import streamlit as st

# Configuração da página
st.set_page_config(page_title="Sebo Digital - Clássicos em Português", page_icon="📖", layout="centered")

# Estilos CSS com tema de Sebo / Livraria Antiga
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-family: 'Georgia', serif;
        color: #5c4033;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        color: #8b5a2b;
        margin-bottom: 25px;
        font-size: 16px;
        font-style: italic;
    }
    .sebo-card {
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #d2b48c;
        background-color: #fdf5e6;
        margin-bottom: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📖 Sebo Digital Literário</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Garimpe grandes clássicos e obras fundamentais inteiramente em Português</div>", unsafe_allow_html=True)

# Base de dados focada em obras traduzidas ou escritas em Português com links estáveis
livros_sebo = [
    {"id": 1, "titulo": "A Divina Comédia", "autor": "Dante Alighieri", "idioma": "🇵🇹 Português", "categoria": "Poesia Épica", "link": "https://www.gutenberg.org/ebooks/59111"},
    {"id": 2, "titulo": "A Comédia dos Erros", "autor": "William Shakespeare", "idioma": "🇵🇹 Português", "categoria": "Teatro", "link": "https://www.gutenberg.org/ebooks/16474"},
    {"id": 3, "titulo": "Poemas de Fernando Pessoa", "autor": "Fernando Pessoa", "idioma": "🇵🇹 Português", "categoria": "Poesia", "link": "https://www.gutenberg.org/ebooks/52569"},
    {"id": 4, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "idioma": "🇵🇹 Português", "categoria": "Romance", "link": "https://www.gutenberg.org/ebooks/54992"},
    {"id": 5, "titulo": "Cancioneiro", "autor": "Fernando Pessoa", "idioma": "🇵🇹 Português", "categoria": "Poesia", "link": "https://www.gutenberg.org/ebooks/52569"},
    {"id": 6, "titulo": "Romeu e Julieta", "autor": "William Shakespeare", "idioma": "🇵🇹 Português", "categoria": "Teatro", "link": "https://www.gutenberg.org/ebooks/17615"},
    {"id": 15, "titulo": "Livro do Desassossego", "autor": "Fernando Pessoa", "idioma": "🇵🇹 Português", "categoria": "Prosa", "link": "https://www.gutenberg.org/ebooks/52569"},
    {"id": 24, "titulo": "A Cidade e as Serras", "autor": "José Maria Eça de Queirós", "idioma": "🇵🇹 Português", "categoria": "Romance", "link": "https://www.gutenberg.org/ebooks/47301"},
    {"id": 31, "titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "idioma": "🇵🇹 Português", "categoria": "Romance", "link": "https://www.gutenberg.org/ebooks/39719"},
    {"id": 37, "titulo": "Os Lusíadas", "autor": "Luís Vaz de Camões", "idioma": "🇵🇹 Português", "categoria": "Poesia Épica", "link": "https://www.gutenberg.org/ebooks/3333"},
    {"id": 38, "titulo": "A Metamorfose", "autor": "Franz Kafka", "idioma": "🇵🇹 Português", "categoria": "Novela", "link": "https://www.gutenberg.org/ebooks/22464"},
    {"id": 60, "titulo": "Iracema", "autor": "José de Alencar", "idioma": "🇵🇹 Português", "categoria": "Romance Indianista", "link": "https://www.gutenberg.org/ebooks/46219"},
    {"id": 63, "titulo": "O Alienista", "autor": "Machado de Assis", "idioma": "🇵🇹 Português", "categoria": "Conto", "link": "https://www.gutenberg.org/ebooks/56501"},
    {"id": 77, "titulo": "Os Maias", "autor": "José Maria Eça de Queirós", "idioma": "🇵🇹 Português", "categoria": "Romance", "link": "https://www.gutenberg.org/ebooks/56230"},
    {"id": 120, "titulo": "O Cortiço", "autor": "Aluísio de Azevedo", "idioma": "🇵🇹 Português", "categoria": "Naturalismo", "link": "https://www.gutenberg.org/ebooks/53612"},
    {"id": 135, "titulo": "Ilíada", "autor": "Homero", "idioma": "🇵🇹 Português", "categoria": "Poesia Épica", "link": "https://www.gutenberg.org/ebooks/24933"},
]

# Filtro lateral estilo estante de sebo
st.sidebar.markdown("### 🗄️ Prateleiras do Sebo")
categoria_selecionada = st.sidebar.selectbox(
    "Filtrar por Categoria:",
    ["Todas"] + list(set([item["categoria"] for item in livros_sebo]))
)

# Barra de pesquisa principal
termo_busca = st.text_input("🔍 Garimpar no acervo (Título ou Autor):", "")

# Filtragem dos livros
livros_filtrados = []
for livro in livros_sebo:
    match_categoria = (categoria_selecionada == "Todas" or livro["categoria"] == categoria_selecionada)
    match_busca = (termo_busca.lower() in livro["titulo"].lower() or termo_busca.lower() in livro["autor"].lower())
    if match_categoria and match_busca:
        livros_filtrados.append(livro)

st.write(f"Encontradas **{len(livros_filtrados)}** obras disponíveis em Português nas prateleiras:")
st.write("")

# Exibição das obras em formato de "prateleira" digital
for livro in livros_filtrados:
    with st.container():
        st.markdown(f"""
            <div class='sebo-card'>
                <strong>{livro['id']}. {livro['titulo']}</strong><br>
                <span style='color: #555;'>Autor: {livro['autor']}</span> | 
                <span style='color: #2c3e50;'>{livro['idioma']}</span> | 
                <em style='color: #8b5a2b;'>[{livro['categoria']}]</em><br><br>
                <a href='{livro['link']}' target='_blank' style='text-decoration: none; background-color: #5c4033; color: white; padding: 5px 10px; border-radius: 4px; font-size: 14px;'>📖 Ler / Baixar em Português</a>
            </div>
        """, unsafe_allow_html=True)
