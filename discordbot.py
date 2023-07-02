#APP ID: 1124912185181753394
#Public Key: 1dd8046210b18c499414da47cdba365a22ca000be3f25d18df9746284d23b280
import discord
import os
import openai

chat = ""

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("SECRET_KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
      global chat
      chat += f"{message.author}: {message.content}"
      print(f'Message from {message.author}: {message.content}')
      if self.user!=message.author:  #Bot will only respond to a message from the user
        if self.user in message.mentions:   #Bot will only respond if mentioned (or tagged @)
          print(chat)
          response = openai.Completion.create (
            model="text-davinci-003",
            prompt= f"{chat}\nJazibGPT: ",
            temperature=1,
            max_tokens=256, #Max is 4000
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
          )
          channel = message.channel
          messageToSend = response.choices[0].text
          await channel.send(messageToSend)
        

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
