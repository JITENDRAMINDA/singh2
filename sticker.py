from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
app = Client ("ssss",bot_token="959566620:AAFq_Rc8jlpttg3MZauPsW5yuKrApoL_x58",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9")                                   

@app.on_message(Filters.channel)
def main(client, message):
 if message.text == "6":
  client.send_sticker(message.chat.id,'CAADBQADHAAD271NHXPgZgboyWwDAg')
 elif message.text == "4":
  client.send_sticker(message.chat.id,'CAADBQADGwAD271NHWpGz0fJOgEPAg')
 elif "WICKET" in message.text:
  client.send_sticker(message.chat.id,'CAADBQADHQAD271NHQimFHP2bU9cAg')
 elif 'DRINKS BREAK' in message.text:
  client.send_sticker(message.chat.id,'CAADBQADJQAD271NHRSHuFn7xmbvAg')
 elif 'WIDE' in message.text:
  client.send_sticker(message.chat.id,'CAADBQADHgAD271NHUFx5PgLyzp9Ag')

@app.on_message(Filters.chat(Filters.private & Filters.sticker)
def forawrd(client, message):
  client.send_sticker(message.chat.id,'CAADBQADHwAD271NHQtXw-moeKYWAg')
  client.send_message(message.chat.id,message.sticker.file_id )


app.run()
