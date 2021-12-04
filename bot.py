from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from buttum import *#menu, Haydovchi_kerak, men_haydovchiman, toshkent, surxondaryo

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Salom {user}", reply_markup=menu)

""" --- Birinchi Haydovchi kerak --- """
@dp.message_handler(Text(equals=["Haydovchi kerak"]))
async def haydovchi(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak)

# """ Toshkentning shaxarlari """
@dp.message_handler(Text(equals="Toshkent"))
async def toshkents(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?\nTumanlardan birini tanlang", reply_markup=toshkent)

# --- Yunusobod
@dp.message_handler(Text(equals="Yunusobod"))
async def yunsobots(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Yashnobod
@dp.message_handler(Text(equals="Yashnobod"))
async def yashnaobods(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Yakkasaroy
@dp.message_handler(Text(equals="Yakkasaroy"))
async def yakkasaroys(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Shayxontohur
@dp.message_handler(Text(equals="Shayxontohur"))
async def shoyxontohurs(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Chilonzor
@dp.message_handler(Text(equals="Chilonzor"))
async def chilonzors(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Olmazor
@dp.message_handler(Text(equals="Olmazor"))
async def olmazors(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Sergeli 
@dp.message_handler(Text(equals="Sergeli"))
async def sergeli(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Mirobod
@dp.message_handler(Text(equals="Mirobod"))
async def mirobod(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Mirzo Ulug'bek
@dp.message_handler(Text(equals="Mirzo Ulug'bek"))
async def mirzo_ulugbek(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Bektemir
@dp.message_handler(Text(equals="Bektemir"))
async def bektemirs(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Uchtepa
@dp.message_handler(Text(equals="Uchtepa"))
async def uchtepas(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\Viloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Qibray
@dp.message_handler(Text(equals="Qibray"))
async def qibrays(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Piskent
@dp.message_handler(Text(equals="Piskent"))
async def piskents(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Parkent
@dp.message_handler(Text(equals="Parkent"))
async def parkents(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Bo'ka
@dp.message_handler(Text(equals="Bo'ka"))
async def boka(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Bekobod shahri
@dp.message_handler(Text(equals="Bekobod shahri"))
async def bekobod_sh(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# --- Angren shahri
@dp.message_handler(Text(equals="Angren shahri"))
async def angren(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=t_viloyatlar)

# \\\ Surxondaryo ///
@dp.message_handler(Text(equals="Surxondaryo"))
async def surxondaryo(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=surxondaryo)

# --- Buxoro shaxarlari
@dp.message_handler(Text(equals="Buxoro"))
async def buxoras(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=buxaro)

# --- Xorazm
@dp.message_handler(Text(equals="Xorazm"))
async def xorazms(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=xorazm)

# --- Andijon 
@dp.message_handler(Text(equals="Andijon"))
async def andijans(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=andijon)

# --- Farg'ona
@dp.message_handler(Text(equals="Farg'ona"))
async def fargonas(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=fargona)

# --- Jizzax
@dp.message_handler(Text(equals="Jizzax"))
async def jizzahs(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=jizzax)

# --- Qoshqidaryo
@dp.message_handler(Text(equals="Qoshqidaryo"))
async def qoshqadaryos(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=qoshqadaryo)

# --- Namangan 
@dp.message_handler(Text(equals="Namangan"))
async def namangans(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=namangan)

# --- Navoi
@dp.message_handler(Text(equals="Navoi"))
async def navois(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=navoi)

# --- Sirdaryo
@dp.message_handler(Text(equals="Sirdaryo"))
async def sirdaros(message: types.Message):
    pass
    # await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=)

# --- Samarqand
@dp.message_handler(Text(equals="Samarqand"))
async def samarkans(message: types.Message):
    pass
    # await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=samarqand)

# --- Qoraqalpoqistan
@dp.message_handler(Text(equals="Qoraqalpoqistan"))
async def qalpagistans(message: types.Message):
    pass
    # await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=qoraqalpoqistan)

# Orqaga qaytish
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Tugmalardan ozingizga kerakini tanlang", reply_markup=Haydovchi_kerak)

# Menuga qaytish 
@dp.message_handler(Text(equals=["Bosh sahifa"]))
async def accounts(message: types.Message):
    await message.answer(f"Tugmalardan ozingizga kerakini tanlang", reply_markup=menu)



""" --- Men haydovchiman --- """
@dp.message_handler(Text(equals=["Men haydovchiman"]))
async def contacts(message: types.Message):
    await message.answer(f"Qaysi yo'nalishda qatnaysiz?", reply_markup=men_haydovchiman)


# @dp.message_handler(Text(equals=["Obuna bo'lish"]))
# async def send_contact(message: types.Message):
#     msg = "<b>Hamkorlarimizga obuna bo'ling</b>\n@Motivatsiya_Official_TG\n<a href='https://t.me/BekoDev'><u>Python</u></a>"
#     await message.answer(msg, parse_mode='html')

# @dp.message_handler(Text(equals=["Qo'shimcha fikrlar"]))
# async def comments(message: types.Message):
#     msg = "Fikrlaringizni <a href='https://t.me/Bekzod_Rakhimov'>admin</a>ga jo'nating"
#     await message.answer(msg, parse_mode="html")


# @dp.message_handler(Text(equals=["Rasmlar"]))
# async def images(message: types.Message):
#     await message.answer_photo("https://api.modme.uz/uploads/RYXg4SOLokaorH91.jpg", caption="Data o'quv markazi ikonkasi")
#     await message.answer_photo(photo=open('/media/bekzod/Hard Disk6/Python Code/python_darslar/Python/bot/translatebot/tgbot.jpg', 'rb'), caption="Telegram BOT")



@dp.message_handler(Text(equals=["🔙 Orqaga"]))
async def back(message: types.Message):
    await message.answer("Tugmalardan ozingizga kerakini tanlang", reply_markup=menu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)