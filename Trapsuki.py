import discord

TOKEN = 'NDMyNDQ1OTg5MjE5OTkxNTUy.Dav2zQ.MDEQ81HGyygD_Zbp6myA-6FfGiw'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!daddy'):
        msg = 'Stop That.'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Natsuki'):
        msg = 'Its not like I like you or anything..... Baka'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('brendon'):
        msg = 'ew what a fag'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('ashe'):
        msg = 'I would T A P S U K I'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Mario'):
        msg = 'do the mario!'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('Manga isnt literature'):
        msg = '*now you wait just one second-*'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('manga isnt literature'):
        msg = '*now you wait just one second-*'.format(message)
        await client.send_message(message.channel, msg)






@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(process.env.BOT_TOKEN)

