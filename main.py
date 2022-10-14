from configparser import ConfigParser
from pyrogram import Client, filters
from asyncio import sleep
# instantiate
config = ConfigParser()
# Read exist file
config.read('config.ini')

# Read values from section
api_id = config.get('pyrogram', 'api_id')
api_hash = config.get('pyrogram', 'api_hash')
phone_number = config.get('pyrogram', 'phone_number')


app = Client(name='zajroid',
             api_id=api_id,
             api_hash=api_hash,
             phone_number=phone_number)

@app.on_message(filters=filters.dice & filters.incoming & filters.private)
async def dice(client, message):
    player_1 = message # usr
    player_2 = (await app.send_dice(message.chat.id)) # bot

    await sleep(3.5)

    if player_1.dice.value > player_2.dice.value:
        await app.send_message(message.chat.id, 'Ты выиграл!')
    elif player_1.dice.value < player_2.dice.value:
        await app.send_message(message.chat.id, 'Ты проиграл')
    else:
        await app.send_message(message.chat.id, 'Ничья')

    # print(player_1)

app.run()
