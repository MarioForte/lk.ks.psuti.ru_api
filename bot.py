from vkwave.bots import SimpleLongPollBot, SimpleBotEvent
from vkwave.bots.core.dispatching import filters
from vkwave.bots.utils.keyboards.keyboard import Keyboard, ButtonColor
from vkwave.types.bot_events import BotEventType
from vkwave.api import API
from vkwave.client import AIOHTTPClient

from tokens import *
from response import *
from db import BotDB

bot = SimpleLongPollBot(tokens=bot_token, group_id=bot_id)

vkapi = API(clients=AIOHTTPClient(), tokens=bot_token).get_context()

BotDB = BotDB('database.db')


# api = API(clients=AIOHTTPClient(), tokens=bot_token).get_context()


def get_settings_keyboard(obj):
    keyboard = Keyboard(inline=True)
    try:
        days = get_days_of_week(obj)
    except:
        return
    for i, day in enumerate(days, start=1):
        if i % 3 == 0:
            keyboard.add_row()
        keyboard.add_callback_button(text=day, color=ButtonColor.POSITIVE, payload={
                                     'day': day, 'obj': obj})
    return keyboard.get_keyboard()


@bot.message_handler(filters.CommandsFilter("расписание"))
async def keyboard(event: SimpleBotEvent):
    obj = BotDB.get_obj(event.peer_id)
    if obj:
        try:
            await event.answer("Выберите день.", keyboard=get_settings_keyboard(obj))
        except Exception as e:
            return e
    else:
        await event.answer('Напишите следующим сообщением "obj" вашей группы в ссылке на расписание в виде "?obj=ЗНАЧЕНИЕ"', attachment="photo-216826683_457239017")


@bot.handler(bot.event_type_filter(BotEventType.MESSAGE_EVENT), filters.PayloadContainsFilter("day"))
async def result(event: SimpleBotEvent):
    try:
        json = get_json(int(event.payload['obj']))[event.payload['day']]
    except Exception as e:
        return e
    result = event.payload['day'].split("/")[0] + '\n\n'
    for key in json.keys():
        result += f"{json[key]['number']}: {json[key]['time']}\n"
        result += f"{json[key]['name']}\n{json[key]['issue']}\n\n"
    await vkapi.messages.delete(delete_for_all=1, conversation_message_ids=event.object.object.conversation_message_id, peer_id=event.peer_id)
    await event.api_ctx.messages.send(message=result, random_id=0, peer_id=event.peer_id)


@bot.message_handler(filters.TextStartswithFilter("?obj="))
async def obj_write(event: SimpleBotEvent):
    obj = event.text.split('=')[1]
    if obj.isdigit():
        BotDB.obj_write(event.peer_id, obj)
        await event.reply('Готово!')
        await keyboard(event)
    else:
        return

if __name__ == "__main__":
    bot.run_forever()
