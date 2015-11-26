import discord
import logging

from credentials import Credentials

credentials = Credentials()

# Set up the logging module to output diagnostic to the console.
logging.basicConfig()

client = discord.Client()
client.login(credentials.email, credentials.password)

if not client.is_logged_in:
    print('Logging in to Discord failed')
    exit(1)

@client.event
def on_message(message):

    for user in message.mentions:
        if user.name == "Kortana":
            client.send_message(message.channel, "Ich bin eine künstliche Intelligenz.")
        if user.name == "Pace":
            client.send_message(message.channel, "De acordo com os meus cálculos, o Roberto é **viado**.")

    if message.content.find('robert') >= 0:
        client.send_message(message.channel, "De acordo com os meus cálculos, o Roberto é **viado**.")
    if message.content.startswith('!cortana'):
        #client.send_message(message.channel, 'Hello {}!'.format(message.author.mention()))
        arg = int(message.content.split(" ")[1])
        soma = 0
        for i in range(arg):
            soma += i
        client.send_message(message.channel, str(soma))


@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
