import importlib

print("===== TESTE DE AMBIENTE – PROVA DE PYTHON =====\n")

bibliotecas_necessarias = {
    "streamlit": "streamlit",
    "requests": "requests",
    "base64 (interna)": "base64",     # esta já vem no Python
}

# opcionais que você usa durante o semestre
bibliotecas_opcionais = {
    "pyautogui": "pyautogui",
    "pandas": "pandas"
}

faltando = []

print("🔍 Verificando bibliotecas OBRIGATÓRIAS...\n")

for nome_visivel, nome_real in bibliotecas_necessarias.items():
    try:
        importlib.import_module(nome_real)
        print(f"[OK] {nome_visivel}")
    except ImportError:
        print(f"[ERRO] {nome_visivel} NÃO instalada")
        faltando.append(nome_real)

print("\n🔍 Verificando bibliotecas OPCIONAIS...\n")

for nome_visivel, nome_real in bibliotecas_opcionais.items():
    try:
        importlib.import_module(nome_real)
        print(f"[OK] {nome_visivel}")
    except ImportError:
        print(f"[AVISO] {nome_visivel} não instalada (não impede a prova)")

print("\n==============================================")

if len(faltando) == 0:
    print("🎉 AMBIENTE APROVADO! Você está APTO a rodar a prova.")
else:
    print("⚠ Atenção! Seu computador NÃO está apto para a prova.\n")
    print("Instale as bibliotecas abaixo:")
    for b in faltando:
        print(f"pip install {b}")

print("==============================================")
