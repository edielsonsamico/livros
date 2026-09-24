import streamlit as st

# Configuração da página
st.set_page_config(page_title="Sebo Digital - Clássicos e Raridades", page_icon="📖", layout="centered")

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
st.markdown("<div class='subtitle'>Garimpe grandes clássicos, poesia e obras raras em domínio público</div>", unsafe_allow_html=True)

# Base de dados inspirada na nossa coleção de clássicos
livros_sebo = [
    {"id": 1, "titulo": "A Divina Comédia", "autor": "Dante Alighieri", "categoria": "Poesia Épica", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 2, "titulo": "A Comédia dos Erros", "autor": "William Shakespeare", "categoria": "Teatro", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=2341"},
    {"id": 3, "titulo": "Poemas de Fernando Pessoa", "autor": "Fernando Pessoa", "categoria": "Poesia", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 4, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "categoria": "Romance", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 5, "titulo": "Cancioneiro", "autor": "Fernando Pessoa", "categoria": "Poesia", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 6, "titulo": "Romeu e Julieta", "autor": "William Shakespeare", "categoria": "Teatro", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=2341"},
    {"id": 15, "titulo": "Livro do Desassossego", "autor": "Fernando Pessoa", "categoria": "Prosa", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 21, "titulo": "Este mundo da injustiça globalizada", "autor": "José Saramago", "categoria": "Ensaios", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 24, "titulo": "A Cidade e as Serras", "autor": "José Maria Eça de Queirós", "categoria": "Romance", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 31, "titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "categoria": "Romance", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 37, "titulo": "Os Lusíadas", "autor": "Luís Vaz de Camões", "categoria": "Poesia Épica", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 38, "titulo": "A Metamorfose", "autor": "Franz Kafka", "categoria": "Novela", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 60, "titulo": "Iracema", "autor": "José de Alencar", "categoria": "Romance Indianista", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 63, "titulo": "O Alienista", "autor": "Machado de Assis", "categoria": "Conto", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 77, "titulo": "Os Maias", "autor": "José Maria Eça de Queirós", "categoria": "Romance", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 120, "titulo": "O Cortiço", "autor": "Aluísio de Azevedo", "categoria": "Naturalismo", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 135, "titulo": "Ilíada", "autor": "Homero", "categoria": "Poesia Épica", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
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

st.write(f"Encontradas **{len(livros_filtrados)}** obras nas prateleiras:")
st.write("")

# Exibição das obras em formato de "prateleira" digital
for livro in livros_filtrados:
    with st.container():
        st.markdown(f"""
            <div class='sebo-card'>
                <strong>{livro['id']}. {livro['titulo']}</strong><br>
                <span style='color: #555;'>Autor: {livro['autor']}</span> | 
                <em style='color: #8b5a2b;'>[{livro['categoria']}]</em><br><br>
                <a href='{livro['link']}' target='_blank' style='text-decoration: none; background-color: #5c4033; color: white; padding: 5px 10px; border-radius: 4px; font-size: 14px;'>📖 Examinar / Ler Obra</a>
            </div>
        """, unsafe_allow_html=True)
