import discord
import disctoken
client = discord.Client()

@client.event
async def on_connect():
    for user in client.user.friends:
        try:
            await user.send('Opa sorry')
            print(f'Working with: {user.name}')
        except:
            print(f'Not working on: {user.name}')

client.run(disctoken.token, bot=False)
