import streamlit as st

# Configuração da página
st.set_page_config(page_title="Biblioteca Digital de Clássicos", page_icon="📚", layout="centered")

# Estilos CSS personalizados
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
        color: #2c3e50;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        color: #7f8c8d;
        margin-bottom: 25px;
        font-size: 16px;
    }
    .book-card {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        background-color: #fdfefe;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📚 Biblioteca Digital de Clássicos</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Explore e leia centenas de obras clássicas gratuitas em domínio público</div>", unsafe_allow_html=True)

# Base de dados com os livros da sua lista e links oficiais do Domínio Público
livros_db = [
    {"id": 1, "titulo": "A Divina Comédia", "autor": "Dante Alighieri", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 2, "titulo": "A Comédia dos Erros", "autor": "William Shakespeare", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=2341"},
    {"id": 3, "titulo": "Poemas de Fernando Pessoa", "autor": "Fernando Pessoa", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 4, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 5, "titulo": "Cancioneiro", "autor": "Fernando Pessoa", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 6, "titulo": "Romeu e Julieta", "autor": "William Shakespeare", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=2341"},
    {"id": 7, "titulo": "A Cartomante", "autor": "Machado de Assis", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 8, "titulo": "Mensagem", "autor": "Fernando Pessoa", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 9, "titulo": "A Carteira", "autor": "Machado de Assis", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 10, "titulo": "A Megera Domada", "autor": "William Shakespeare", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=2341"},
    {"id": 11, "titulo": "A Tragédia de Hamlet, Príncipe da Dinamarca", "autor": "William Shakespeare", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=2341"},
    {"id": 12, "titulo": "Sonho de Uma Noite de Verão", "autor": "William Shakespeare", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=2341"},
    {"id": 15, "titulo": "Livro do Desassossego", "autor": "Fernando Pessoa", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 21, "titulo": "Este mundo da injustiça globalizada", "autor": "José Saramago", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 24, "titulo": "A Cidade e as Serras", "autor": "José Maria Eça de Queirós", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 31, "titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 37, "titulo": "Os Lusíadas", "autor": "Luís Vaz de Camões", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 38, "titulo": "A Metamorfose", "autor": "Franz Kafka", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 60, "titulo": "Iracema", "autor": "José de Alencar", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 63, "titulo": "O Alienista", "autor": "Machado de Assis", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 65, "titulo": "A Volta ao Mundo em 80 Dias", "autor": "Júlio Verne", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 73, "titulo": "Eu e Outras Poesias", "autor": "Augusto dos Anjos", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 77, "titulo": "Os Maias", "autor": "José Maria Eça de Queirós", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 91, "titulo": "Quincas Borba", "autor": "Machado de Assis", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 93, "titulo": "Os Sertões", "autor": "Euclides da Cunha", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 120, "titulo": "O Cortiço", "autor": "Aluísio de Azevedo", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
    {"id": 135, "titulo": "Ilíada", "autor": "Homero", "link": "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1965"},
]

# Barra de Pesquisa Interativa
pesquisa = st.text_input("🔍 Pesquisar por título ou autor:", "")

# Filtrar os livros com base na pesquisa
livros_filtrados = [
    l for l in livros_db 
    if pesquisa.lower() in l['titulo'].lower() or pesquisa.lower() in l['autor'].lower()
]

st.write(f"Mostrando **{len(livros_filtrados)}** obras disponíveis:")
st.write("")

# Exibição dos livros em formato de cartões limpos
for livro in livros_filtrados:
    with st.container():
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"**{livro['id']}. {livro['titulo']}**")
            st.markdown(f"<span style='color: gray; font-size: 14px;'>Autor: {livro['autor']}</span>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"[📖 Ler / Baixar]({livro['link']})", unsafe_allow_html=True)
        st.divider()
