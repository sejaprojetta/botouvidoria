from email import message
import telebot

bot = telebot.TeleBot("5191200153:AAFUDgBCc0VAM8iIzihHZLt6ckozzm40Q_Y")

def verificar(mensagem):
    return True

#message_handler
@bot.message_handler(commands=["start"])
def enviar(mensagem):
#    print(mensagem.chat.id)
    bot.send_message(
        mensagem.chat.id,
        f""" Oi, {mensagem.chat.first_name}, tá com algum problema? Sou todo ouvidos! 🦻"""
    )
    bot.send_message(
        mensagem.chat.id,
        "Clica aí na opção que tu quer que eu já te explico como funciona por aqui."
    )
    bot.send_message(
        mensagem.chat.id,
        """/reclamacao Se tiver algo interno que tá te chateando, com membros, direx ou geral mesmo
/feedback Se tiver alguma coisa ou alguém que tu queira reconhecer positiva ou negativamente
/sugestao Caso tu queira sugerir algo e sente que não tem abertura, ou quer fazer no anonimato""")


@bot.message_handler(commands=["reclamacao"])
def enviar(mensagem):
    bot.send_message(
        mensagem.chat.id,
        """Eita, bora resolver isso! Pra mandar uma reclamação, tu envia com um "REC" no comecinho"""
    )
    bot.send_message(
        mensagem.chat.id, """Aí tu manda tipo:

REC: Eu amo Abílio; ou
REC Socorro, Deus

Tendo o "REC" no comecinho, funciona. É só para filtrar mesmo.
E pronto, já vai pra ouvidoria da VPGG (tudo anonimamente, viu)""")
    bot.send_message(
        mensagem.chat.id,
        """Ah e manda tudo em uma mensagem só, senão vai ter que ficar mandando o "REC" no começo de todas."""
    )


@bot.message_handler(commands=["feedback"])
def enviar(mensagem):
    bot.send_message(
        mensagem.chat.id,
        """Espero que seja coisa boa! Mas se não for também, a gente tenta arrumar. Pra mandar um feedback pra alguém, tu envia a mensagem com um "FEED" no começo."""
    )
    bot.send_message(
        mensagem.chat.id, """Aí tu manda tipo:

FEED: Abílio é muito legal; ou
FEED Jennifer tá sumida

Tendo o "FEED" no comecinho, funciona. É só para filtrar mesmo.
E pronto, já vai pra ouvidoria da VPGG (tudo anonimamente, viu)""")
    bot.send_message(
        mensagem.chat.id,
        """Ah e manda tudo em uma mensagem só, senão vai ter que ficar mandando o "FEED" no começo de todas. E não esquece o nome da pessoa do teu feedback se for pra alguém específico."""
    )


@bot.message_handler(commands=["sugestao"])
def enviar(mensagem):
    bot.send_message(
        mensagem.chat.id,
        """Uhuuuu, sugestão é sempre bom! Pra mandar uma sugestão, tu manda com um "SUG" na frente."""
    )
    bot.send_message(
        mensagem.chat.id, """Aí tu manda tipo:

SUG: Abílio merece uma fantasia; ou
SUG A salinha precisa de um ar condicionado.

Tendo o "SUG" no comecinho, funciona.
E pronto, já vai pra ouvidoria da VPGG (tudo anonimamente, viu)""")
    bot.send_message(
        mensagem.chat.id,
        """Ah e manda tudo em uma mensagem só, senão vai ter que ficar mandando o "SUG" no começo de todas."""
    )


'''@bot.message_handler(commands=["bomdiabot"])
def enviar(mensagem):
    bot.send_message(
        mensagem.chat.id,
        """Bom dia, família! Bom dia, grupo! Bom dia, MEEEEEJ! 😍😍""")
    bot.send_message(
        mensagem.chat.id,
        """Quiser mandar algum /feedback /sugestao ou /reclamacao, é só dizer que hoje eu tô feliz!"""
    )'''


@bot.message_handler(commands=["help"])
def enviar(mensagem):
    bot.send_message(
        mensagem.chat.id,
        """Pra enviar alguma mensagem pra ouvidoria, é só mandar a mensagem com as letras no começo que eu já encaminho pra análise."""
    )
    bot.send_message(
        mensagem.chat.id, """Tu manda começando tipo assim:

SUG para sugestão
FEED para feedback
REC para reclamações

E pronto, já vai pra ouvidoria da VPGG!""")
    bot.send_message(
        mensagem.chat.id,
        """Ah e manda tudo em uma mensagem só, senão vai ter que ficar mandando o código no começo de todas."""
    )
    bot.send_message(
        mensagem.chat.id,
        "Se mesmo assim não der certo, fala com VPGG, por favor."
    )


@bot.message_handler(commands=["socorro"])
def enviar(mensagem):
    bot.send_message(
        mensagem.chat.id,
        """É que eu sou meio lerdo kkkk, aí eu só entendo quando mandam escrito "REC", "SUG" ou "FEED" na frente. Se não tiver, eu bugo. 🤡"""
    )

bia = -1001858208313
@bot.message_handler(func=verificar)
def chamada(mensagem):
    if mensagem.text.startswith("REC"):
        bot.send_message(bia, mensagem.text, mensagem.photo,
                         mensagem.audio, mensagem.video)
        bot.reply_to(
            mensagem,
            "Enviei a mensagem pra análise, viu? Vamos resolver esse problema!")
       
    elif mensagem.text.startswith("rec"):
        bot.send_message(bia, mensagem.text, mensagem.photo,
                         mensagem.audio, mensagem.video)
        bot.reply_to(
            mensagem,
            "Enviei a mensagem pra análise, viu? Vamos resolver esse problema!")
    elif mensagem.text.startswith("Rec"):
        bot.send_message(bia, mensagem.text, mensagem.photo,
                         mensagem.audio, mensagem.video)
        bot.reply_to(
            mensagem,
            "Enviei a mensagem pra análise, viu? Vamos resolver esse problema!")
    elif mensagem.text.startswith("SUG"):
        bot.send_message(bia, mensagem.text, mensagem.photo,
                         mensagem.audio, mensagem.video)
        bot.reply_to(mensagem, "Sugestão enviadaaaa! VPGG já recebeu.")
    elif mensagem.text.startswith("sug"):
        bot.send_message(bia, mensagem.text, mensagem.photo,
                         mensagem.audio, mensagem.video)
        bot.reply_to(mensagem, "Sugestão enviadaaaa! VPGG já recebeu.")
    elif mensagem.text.startswith("Sug"):
        bot.send_message(bia, mensagem.text, mensagem.photo,
                         mensagem.audio, mensagem.video)
        bot.reply_to(mensagem, "Sugestão enviadaaaa! VPGG já recebeu.")
    elif mensagem.text.startswith("FEED"):
        bot.send_message(bia, mensagem.text, mensagem.photo,
                         mensagem.audio, mensagem.video)
        bot.reply_to(mensagem, "Feedback enviado pra VPGG, viu?")
    elif mensagem.text.startswith("feed"):
        bot.send_message(bia, mensagem.text, mensagem.photo,
                         mensagem.audio, mensagem.video)
        bot.reply_to(mensagem, "Feedback enviado pra VPGG, viu?")
    elif mensagem.text.startswith("Feed"):
        bot.send_message(bia, mensagem.text, mensagem.photo,
                         mensagem.audio, mensagem.video)
        bot.reply_to(mensagem, "Feedback enviado pra VPGG, viu?")
    else:
        bot.reply_to(
            mensagem,
            """Puts! Não reconheci o começo da mensagem com os códigos, daí nem enviei. 😅
Se precisar de ajuda, clica em /help ou /start""")


@bot.message_handler(func=verificar)
def imagem(mensagem):
    bot.send_message(bia, mensagem.text, mensagem.photo, mensagem.audio,
                     mensagem.video)
    bot.reply_to(mensagem, "Imagem enviada!")

print ()
print ()
print ("O bot está ativo, buscando mensagens...")

bot.polling()
print("Bot desativado! Lembre de rodar todos os dias!")