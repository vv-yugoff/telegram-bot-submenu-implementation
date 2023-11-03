# External libraries
from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

# Internal libraries
from config import TOKEN
from keyboards import *

# Key variables
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
storage = MemoryStorage()

# @dp.message_handler() - Responsible for processing incoming messages from the user

# Command for processing /start from user
@dp.message_handler(commands=['start']) 
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup=markup) # Response message from the bot to the /start command


@dp.message_handler()
async def submenu_btn2_message(message: types.Message):
    if message.text == 'Где находимся?':
        await bot.send_message(message.from_user.id, 'Выберите опцию:', reply_markup=submenu_markup)
    else:
        await bot.send_message(message.from_user.id, message.text)

# Displaying the office address
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'address')
async def process_address(callback_query: types.CallbackQuery):
    message = "<b>Адрес:</b> ул. Горького, 65, Екатеринбург, Свердловская обл., 620026"
    await bot.send_message(callback_query.from_user.id, message, parse_mode='HTML')
    await bot.answer_callback_query(callback_query.id)

# Show location on map
@dp.callback_query_handler(lambda c: c.data == 'map')
async def show_location_on_map(call: types.CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    latitude = 56.824390  # Given latitude coordinates
    longitude = 60.605092  # Given longitude coordinates
    await bot.send_location(chat_id, latitude, longitude)

# Launching a bot to listen to incoming updates and process messages
if __name__ == '__main__':
    executor.start_polling(dp)