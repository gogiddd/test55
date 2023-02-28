from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client('session', api_id='26757683', api_hash='7fbe63d3dcd5cf0f040376b0a34f100e')


chat_id = "@anonkarubot"  #тут свой чат в котором спамить

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if '/stop - завершить диалог' in message.text:  # Меняем это значение если хотим спамить в другом чате
        sleep(1.8)
        await app.send_message(chat_id, "Привет! Хочешь шоп, который является мастадонтом среди своих аналогов?")
        sleep(2)
        await app.send_message(chat_id, """Я с кентом вейпшоп прямо тут в тг открыл.\n
Заходи, вступай в канал и получай плюхи)\n
В подарок к первому заказу отсылаем одноразку или жижу на выбор!)""")

        if '/stop - завершить диалог' in message.text:
             sleep(1.7)
             await app.send_sticker(chat_id, "CAACAgIAAxkBAAEH6thj_C-6uWOrxwIr7gXHLiZS6wnAdgAC-CQAAsUm4UsyPMyKe6Drni4E")
             sleep(2)

             if "/stop - завершить диалог"  in message.text:  # Меняем это значение если хотим спамить в другом чате
                 await app.send_message(chat_id, "/stop")
                 sleep(1.5 )
                 await app.send_message(chat_id, "Найти собеседника 🔎")


app.run()