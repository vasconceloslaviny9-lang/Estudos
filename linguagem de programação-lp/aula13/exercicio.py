#criar um pequeno sistema automatizado que mostre uma mensagem de alerta e confirmação para o usuário, peça informações básicas (nome e email) confirme se o usuário quer continuar, caso sim tire automaticamente uma captura de tela.

import pyautogui
import time

pyautogui.alert(text='Bem-vindo ao sistema automatizado!', 
                title='Início da automação',
                button='OK',)

nome=pyautogui.prompt(text='Digite seu nome:', title='Informação obrigatória')
email=pyautogui.prompt(text='Digite seu email:', title='Informação obrigatória')

resposta=pyautogui.confirm(
    text=f'Confirme seus dados:\n\n Nome: {nome}\n\n Email: {email}\n\n Deseja continuar com a captura de tela?',
    title='Confirmação de dados',
    buttons=['Sim', 'Não', 'Cancelar']
)

if resposta== 'Sim':
    pyautogui.alert('Prepare-se! A captura de tela sera feita em 3 segundos', title='captura de tela')
    time.sleep(3)
    pyautogui.screenshot('Captura_Usuário.png')
    pyautogui.alert('Captura realizada com sucesso!', title='Sucesso')
elif resposta=='Não':
    pyautogui.alert('Processo cancelado pelo usuário', title='Cancelado')
else:pyautogui.alert('Automação foi interrompida', title='Encerrado')

print(f'Nome: {nome}')
print(f'email: {email}')
print(f'Resposta do usuário: {resposta}')

