#TODO: importar as bibliotecas
import telebot
import time
from telebot import types
from datetime import datetime
from datetime import date

#TODO: Definir a variavel chave API

CHAVE_API = "6823297602:AAErOFwPtF3ZTEdF10hN_qsHtb1yrVz5o-A"

#TODO: Conexão com o BOT

bot = telebot.TeleBot(CHAVE_API)

#TODO:Verificar os dias da semana

dia_hoje = date.today().weekday()
print(dia_hoje)

#TODO: Verificar o horário

date = datetime.now()
datehour = date.strftime("%d/%m/%Y %H:%M")
horaatual = datetime.now()
print(horaatual)

if dia_hoje < 5 and 8 >= horaatual.hour <= 18 or dia_hoje >= 5:

    def verificar(mensagem):
        return True

    @bot.message_handler(commands=["Opcao1"])
    def opcao1 (mensagem):
           bot.send_message(mensagem.chat.id, "Texto")

    @bot.message_handler(commands=["Opcao2"])
    def Opcao2(mensagem):
        bot.send_message(mensagem.chat.id, "Texto")

    @bot.message_handler(commands=["Opcao3"])
    def Opcao3(mensagem):
        bot.send_message(mensagem.chat.id, "Texto")

    @bot.message_handler(commands=["Opcao4"])
    def Opcao4(mensagem):
        bot.send_message(mensagem.chat.id, "Texto")

#def botiniciado():

    @bot.message_handler(func=verificar)
    def responder(mensagem):

        #Cumprimentos
        if horaatual.hour < 12:
            cumprimento = "Bom dia"
        elif 12 <= horaatual.hour < 18:
             cumprimento = "Boa tarde"
        else:
              cumprimento = "Boa noite"

# TODO: Nome do cliente e Empresa
        primeiro_nome = mensagem.from_user.first_name
        nome_empresa = mensagem.chat.title
        print(nome_empresa)
        print(primeiro_nome)
        minutos = 50
        texto1 = f"""

{cumprimento}, {primeiro_nome}! Eu sou o BOT da VMB Tecnologia, trabalho apenas fora do horário comercial. 

Aguarde que vou checar as opções que o contrato da {nome_empresa} oferece de opções para este horário:"""

        texto2 = f"""Chequei seu contrato e ele te oferece as opções abaixo, para este horário:

Escolha uma das opções abaixo:
/Opcao1. Solicitar suporte emergencial:
     (Atendimento em até {minutos} minutos )

/Opcao2. Registrar uma ocorrência
/Opcao3. Abrir um chamado técnico
/Opcao4. Solicitar segunda via do boleto"""

        bot.reply_to(mensagem, texto1)
        time.sleep(10)
        bot.reply_to(mensagem, texto2)

bot.polling()

#TODO: Coletar dados do contato
#TODO: Gravar log mongodb