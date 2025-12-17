import streamlit as st
import base64
import requests

# ---------------------------
# CONFIGURAÇÕES DO GOOGLE FORMS
# (envia apenas NOME e NOTA)
# ---------------------------
URL_FORMS = "https://docs.google.com/forms/d/e/1FAIpQLScJfs-Ga8Yg1-inK8JL7H6ERJUkBgyAYVo8Vzt24QgcsICdjA/formResponse"
CAMPOS = {
    "nome": "entry.1112338505",
    "nota": "entry.1973735152"
}

# ---------------------------
# Função de descriptografia (BASE64)
# ---------------------------
def decrypt(txt: str) -> str:
    return base64.b64decode(txt.encode()).decode()

# ---------------------------
# DICIONÁRIO COMPLETO COM 30 QUESTÕES
# 'correta' está criptografada (base64)
# ---------------------------
questoes = {
    1: {"pergunta": "Qual das opções abaixo representa uma variável válida em Python?",
        "alternativas": ["1valor", "valor_1", "valor-1", "valor 1"],
        "correta": "Yg=="},  

    2: {"pergunta": "Qual é o tipo de dado retornado por input() em Python?",
        "alternativas": ["int", "float", "str", "bool"],
        "correta": "Yw=="},  

    3: {"pergunta": "Qual operador é usado para verificar igualdade?",
        "alternativas": ["=", "==", "!=", "==="],
        "correta": "Yg=="},  

    4: {"pergunta": "Qual estrutura é usada para decisões simples?",
        "alternativas": ["for", "if", "while", "def"],
        "correta": "Yg=="},  

    5: {"pergunta": "Qual função converte texto para número inteiro?",
        "alternativas": ["float()", "str()", "input()", "int()"],
        "correta": "ZA=="},  

    6: {"pergunta": "Qual comando imprime valores no console?",
        "alternativas": ["echo()", "print()", "mostrar()", "console()"],
        "correta": "Yg=="},  

    7: {"pergunta": "Qual das opções representa a forma correta de declarar e atribuir um valor a uma variável em Python?",
        "alternativas": ["int numero = 10", "var numero <- 10", "numero = 10", "numero := 10"],
        "correta": "Yw=="},  

    8: {"pergunta": "Qual comando adiciona um novo elemento ao final de uma lista em Python?",
        "alternativas": ["lista.add(item)", "lista.append(item)", "lista.push(item)", "lista.insert(item)"],
        "correta": "Yg=="},  

    9: {"pergunta": "Qual método remove a primeira ocorrência de um valor de uma lista?",
        "alternativas": ["lista.delete(valor)", "lista.remove(valor)", "del lista(valor)", "lista.pop(valor)"],
        "correta": "Yg=="},  

    10: {"pergunta": "Dada a lista numeros = [10, 20, 30, 40], qual comando acessa o valor 30?",
         "alternativas": ["numeros[1]", "numeros[2]", "numeros[3]", "numeros[30]"],
         "correta": "Yg=="},  

    11: {"pergunta": "Dado o dicionário aluno = {'nome': 'Pedro', 'idade': 17}, como acessar o valor 'Pedro'?",
         "alternativas": ["aluno['nome']", "aluno('nome')", "aluno.nome", "aluno.get['nome']"],
         "correta": "YQ=="},  

    12: {"pergunta": "Qual comando cria um loop que repete enquanto a condição for verdadeira?",
         "alternativas": ["for", "if", "while", "try"],
         "correta": "Yw=="},  

    13: {"pergunta": "Qual estrutura é ideal para percorrer listas?",
         "alternativas": ["if", "for", "while", "break"],
         "correta": "Yg=="}, 

    14: {"pergunta": "Qual comando adiciona a chave 'cidade' com o valor 'São Paulo' ao dicionário dados?",
         "alternativas": ["dados.append('cidade', 'São Paulo')",
                          "dados.add('cidade': 'São Paulo')",
                          "dados['cidade'] = 'São Paulo'",
                          "insert dados('cidade', 'São Paulo')"],
         "correta": "Yw=="},  

    15: {"pergunta": "Qual é a principal vantagem de usar funções em um programa Python?",
         "alternativas": ["Tornar o código mais lento, porém mais seguro",
                          "Organizar o código, permitir reutilização e facilitar a manutenção",
                          "Substituir todas as variáveis do programa automaticamente",
                          "Executar comandos apenas uma vez e depois apagar do código"],
         "correta": "Yg=="},  

    16: {"pergunta": "Qual é a saída de print(3 * 'ab')?",
         "alternativas": ["abab", "ab ab ab", "ababab", "Erro"],
         "correta": "Yw=="},  

    17: {"pergunta": "Qual comando importa a biblioteca pandas usando o apelido pd?",
         "alternativas": ["import pandas == pd", "import pandas as pd", "import pandas(pd)", "import pd as pandas"],
         "correta": "Yg=="},  

    18: {"pergunta": "Qual comando importa somente a função sleep da biblioteca time?",
         "alternativas": ["import time.sleep", "from time import all", "from time import sleep", "import sleep from time"],
         "correta": "Yw=="},  

    19: {"pergunta": "Qual comando do PyAutoGUI digita um texto automaticamente?",
         "alternativas": ["pyautogui.text('Olá')", "pyautogui.write('Olá')", "pyautogui.type('Olá')", "pyautogui.keyboard('Olá')"],
         "correta": "Yg=="},  

    20: {"pergunta": "Qual é a forma correta de definir uma função?",
         "alternativas": ["def minha_funcao:", "func minha_funcao()", "def minha_funcao():", "function minha_funcao:"],
         "correta": "Yw=="},  

    21: {"pergunta": "Qual símbolo cria comentários de linha?",
         "alternativas": ["//", "/* */", "#", "<!-- -->"],
         "correta": "Yw=="},  

    22: {"pergunta": "Qual estrutura permite várias condições?",
         "alternativas": ["if/else", "if/elif/else", "while/else", "switch"],
         "correta": "Yg=="},  

    23: {"pergunta": "Qual dos seguintes NÃO é um tipo primitivo de Python?",
         "alternativas": ["int", "float", "str", "num"],
         "correta": "ZA=="},  

    24: {"pergunta": "Qual função converte para número decimal?",
         "alternativas": ["int()", "float()", "double()", "decimal()"],
         "correta": "Yg=="},  

    25: {"pergunta": "Qual código imprime números de 0 a 4?",
         "alternativas": ["for i in 5:", "for i in range(1,5):", "for i in range(5):", "for i to 5"],
         "correta": "Yw=="},  

    26: {"pergunta": "Qual comando realiza um clique com o mouse na posição atual?",
         "alternativas": ["pyautogui.mouseclick()", "pyautogui.click()", "pyautogui.press()", "pyautogui.tap()"],
         "correta": "Yg=="},  

    27: {"pergunta": "Qual comando exibe as 5 primeiras linhas de um DataFrame?",
         "alternativas": ["df.start()", "df.first()", "df.begin()", "df.head()"],
         "correta": "ZA=="},  

    28: {"pergunta": "Qual comando é usado para carregar um arquivo CSV no Pandas?",
         "alternativas": ["pd.load('arquivo.csv')", "pd.open_csv('arquivo.csv')", "pd.read_csv('arquivo.csv')", "pd.csv('arquivo.csv')"],
         "correta": "Yw=="},  

    29: {"pergunta": "Qual comando define um tempo de pausa padrão entre cada ação do PyAutoGUI?",
         "alternativas": ["pyautogui.PAUSE = 1", "pyautogui.wait = 1", "pyautogui.time(1)", "pyautogui.sleep(1)"],
         "correta": "YQ=="},  

    30: {"pergunta": "Qual estrutura repete um bloco um número conhecido de vezes?",
         "alternativas": ["while", "if", "for", "repeat"],
         "correta": "Yw=="}  
}

# ---------------------------
# Interface Streamlit
# ---------------------------
st.set_page_config(page_title="Prova de Python", layout="wide")
st.title("📘 Prova – Linguagem de Programação (Python)")
st.write("Preencha seu nome antes de iniciar. Ao enviar, Nome e Nota serão registrados automaticamente.")
st.markdown("---")

nome = st.text_input("Nome completo", key="nome_input")

st.markdown("---")

# Guardar respostas em um dict
respostas = {}

# Exibir cada questão com radio (padrão: primeira opção)
for num, q in questoes.items():
    st.subheader(f"{num}. {q['pergunta']}")
    letras = ["a", "b", "c", "d"]

    # função formatadora que captura a questão q por parâmetro padrão
    def mostrar(letra, q=q):
        idx = letras.index(letra)
        return f"{letra}) {q['alternativas'][idx]}"

    escolha = st.radio(
        label=f"Escolha a resposta da questão {num}:",
        options=letras,
        format_func=mostrar,
        key=f"q{num}"
    )
    respostas[num] = escolha
    st.markdown("---")

# Botão de envio e correção
if st.button("Enviar Prova"):

    if nome.strip() == "":
        st.error("Por favor preencha seu Nome antes de enviar.")
        st.stop()

    # Corrigir
    acertos = 0
    for num, q in questoes.items():
        correta = decrypt(q["correta"])
        if respostas.get(num) == correta:
            acertos += 1

    # Mostrar nota ao aluno
    st.success(f"🎉 Você acertou {acertos} de {len(questoes)} questões.")

    # Enviar Nome + NOTA para Google Forms
    payload = {
        CAMPOS["nome"]: nome,
        CAMPOS["nota"]: str(acertos)
    }

    try:
        requests.post(URL_FORMS, data=payload, timeout=4)
        st.info("📨 Nome e nota registrados com sucesso.")
    except Exception:
        st.warning("⚠️ Não foi possível registrar no Google Forms (sem conexão ou bloqueio). A correção foi feita localmente.")
