import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        # Layout
        sg.theme('DefaultNoMoreNagging')
        layout = [
            [sg.Text('Site/Software', size=(11, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(11, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(
                range(30)), key='total_chars', default_value=6, size=(3, 1))],
            [sg.Output(size=(50, 10))],
            [sg.Button('Gerar Senha')]
        ]
        # Declarar janela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print('Nova senha gerada: ',nova_senha)
                self.salvar_senha(nova_senha, valores)

    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(
                f"site: {valores['site']}, usuario: {valores['usuario']}, nova senha: {nova_senha}\n")

        print('Arquivo "senhas.txt" salvo no caminho:', os.getcwd(),'\n')


gen = PassGen()
gen.Iniciar()
