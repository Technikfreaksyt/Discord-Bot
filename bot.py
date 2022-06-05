import discord

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
    activity = discord.Game(name="KI", type=1)

    await client.change_presence(status=discord.Status.online, activity=activity)



                             

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    

 

        


    


client.run("Durch Token deines Bots ersetzen")