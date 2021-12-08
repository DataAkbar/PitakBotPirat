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

""" --- Birinchi, Haydovchi kerak --- """
@dp.message_handler(Text(equals=["Haydovchi kerak"]))
async def haydovchi(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak)

""" Toshkentning tumanlari """
# --- Haydovchi kerak\Toshkent\
@dp.message_handler(Text(equals="Toshkent"))
async def toshkents(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?\nTumanlardan birini tanlang", reply_markup=toshkent)

# --- Haydovchi kerak\Toshkent\Yunusobod\
@dp.message_handler(Text(equals="Yunusobod"))
async def yunsobots(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

@dp.message_handler(Text(equals="Surxondaryo"))
async def surxondaryo(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=surxondaryo)

# --- Haydovchi kerak\Toshkent\Yashnobod\
@dp.message_handler(Text(equals="Yashnobod"))
async def yashnaobods(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Yakkasaroy\
@dp.message_handler(Text(equals="Yakkasaroy"))
async def yakkasaroys(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Shayxontohur\
@dp.message_handler(Text(equals="Shayxontohur"))
async def shoyxontohurs(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Chilonzor\
@dp.message_handler(Text(equals="Chilonzor"))
async def chilonzors(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Olmazor
@dp.message_handler(Text(equals="Olmazor"))
async def olmazors(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Sergeli 
@dp.message_handler(Text(equals="Sergeli"))
async def sergeli(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Mirobod
@dp.message_handler(Text(equals="Mirobod"))
async def mirobod(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Mirzo Ulug'bek
@dp.message_handler(Text(equals="Mirzo Ulug'bek"))
async def mirzo_ulugbek(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Bektemir
@dp.message_handler(Text(equals="Bektemir"))
async def bektemirs(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Uchtepa
@dp.message_handler(Text(equals="Uchtepa"))
async def uchtepas(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\Viloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Qibray
@dp.message_handler(Text(equals="Qibray"))
async def qibrays(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Piskent
@dp.message_handler(Text(equals="Piskent"))
async def piskents(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Parkent
@dp.message_handler(Text(equals="Parkent"))
async def parkents(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Bo'ka
@dp.message_handler(Text(equals="Bo'ka"))
async def boka(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Bekobod shahri
@dp.message_handler(Text(equals="Bekobod shahri"))
async def bekobod_sh(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# --- Haydovchi kerak\Toshkent\Angren shahri
@dp.message_handler(Text(equals="Angren shahri"))
async def angren(message: types.Message):
    await message.answer(f"Siz qaysi viloyatga borishingiz kerak?\nViloyatlardan birini tanlang", reply_markup=yunusobod)

# Orqaga qaytish
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=surxondaryo)

# """ \\\ Surxondaryo /// """
# @dp.message_handler(Text(equals="Surxondaryo"))
# async def surxondaryo(message: types.Message):
#     await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=surxondaryo)

# """--- Buxoro shaxarlari """
@dp.message_handler(Text(equals="Buxoro"))
async def buxoras(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=buxaro)

# Orqaga qaytish
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=yunusobod)

# --- Buhoro shahri
@dp.message_handler(Text(equals=["Buxaro shaxri"]))
async def buxor(message: types.Message):
    await message.answer(f"Siz necha odam bolib ketasizlar?", reply_markup=numbers)

# --- Nubers uchun
@dp.message_handler(Text(equals=["G'ijdivon"]))
async def buxor(message: types.Message):
    await message.answer(f"Siz necha odam bolib ketasizlar?", reply_markup=numbers)

# --- qoraqol
@dp.message_handler(Text(equals=["Qorako'l"]))
async def buxor(message: types.Message):
    await message.answer(f"Siz necha odam bolib ketasizlar?", reply_markup=numbers)

# --- Kogon
@dp.message_handler(Text(equals=["Kogon"]))
async def buxor(message: types.Message):
    await message.answer(f"Siz necha odam bolib ketasizlar?", reply_markup=numbers)

# --- Jondor
@dp.message_handler(Text(equals=["Jondor"]))
async def buxor(message: types.Message):
    await message.answer(f"Siz necha odam bolib ketasizlar?", reply_markup=numbers)

# --- Olot
@dp.message_handler(Text(equals=["Olot"]))
async def buxor(message: types.Message):
    await message.answer(f"Siz necha odam bolib ketasizlar?", reply_markup=numbers)

# ---- Peshku
@dp.message_handler(Text(equals=["Peshku"]))
async def buxor(message: types.Message):
    await message.answer(f"Siz necha odam bolib ketasizlar?", reply_markup=numbers)

# ---- Qorovul
@dp.message_handler(Text(equals=["Qorovulbozor"]))
async def buxor(message: types.Message):
    await message.answer(f"Siz necha odam bolib ketasizlar?", reply_markup=numbers)

# --- Romiton
@dp.message_handler(Text(equals=["Romiton"]))
async def buxor(message: types.Message):
    await message.answer(f"Siz necha odam bolib ketasizlar?", reply_markup=numbers)

# ---- Shofirkot
@dp.message_handler(Text(equals=["Shofirkor"]))
async def buxor(message: types.Message):
    await message.answer(f"Siz necha odam bolib ketasizlar?", reply_markup=numbers)

# ---- Vobkent
@dp.message_handler(Text(equals=["Vobkent"]))
async def buxor(message: types.Message):
    await message.answer(f"Siz necha odam bolib ketasizlar?", reply_markup=numbers)

# --- Kogon shahri
@dp.message_handler(Text(equals=["Kogon shahri"]))
async def buxor(message: types.Message):
    await message.answer(f"Siz necha odam bolib ketasizlar?", reply_markup=numbers)

# Orqaga qaytish
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=buxaro)

# --- auto tanlidi 
@dp.message_handler(Text(equals=["1"]))
async def buxor(message: types.Message):
    await message.answer(f"Qanday avtomobilda ketasiz", reply_markup=cars)

# --- auto tanlidi
@dp.message_handler(Text(equals=["2"]))
async def buxor(message: types.Message):
    await message.answer(f"Qanday avtomobilda ketasiz", reply_markup=cars)

# -- auto tanlidi
@dp.message_handler(Text(equals=["3"]))
async def buxor(message: types.Message):
    await message.answer(f"Qanday avtomobilda ketasiz", reply_markup=cars)

# --- auto tanlidi
@dp.message_handler(Text(equals=["4"]))
async def buxor(message: types.Message):
    await message.answer(f"Qanday avtomobilda ketasiz", reply_markup=cars)

# - auto tanlidi
@dp.message_handler(Text(equals=["To'liq salon"]))
async def buxor(message: types.Message):
    await message.answer(f"Qanday avtomobilda ketasiz", reply_markup=cars)

# Orqaga qaytish
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=numbers)

# --- Pitaka borishni tanlash
@dp.message_handler(Text(equals=["Cobalt"]))
async def buxor(message: types.Message):
    await message.answer(f"Pitakka borasizmi yoki shofyor oldingizga borsinmi?", reply_markup=pitak)

# --- Pitaka borishni tanlash
@dp.message_handler(Text(equals=["Lacetti, Gentra"]))
async def buxor(message: types.Message):
    await message.answer(f"Pitakka borasizmi yoki shofyor oldingizga borsinmi?", reply_markup=pitak)

# --- Pitaka borishni tanlash
@dp.message_handler(Text(equals=["Epica"]))
async def buxor(message: types.Message):
    await message.answer(f"Pitakka borasizmi yoki shofyor oldingizga borsinmi?", reply_markup=pitak)

# --- Pitaka boraman
@dp.message_handler(Text(equals=["Pitakka boraman"]))
async def buxor(message: types.Message):
    await message.answer(f"📞 Telefon raqam yuborish tugmasini bosing yoki boshqa ishlab turgan raqamingizni quyidagi ko‘rinishda yozing!", reply_markup=contact)

# --- Telefon ursin 
# @dp.message_handler(Text(equals=["Telefon raqam"]))
# async def buxor(message: types.Message):
#     await message.answer(f"", reply_markup=contact)

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
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak)

# Menuga qaytish 
@dp.message_handler(Text(equals=["Bosh sahifa"]))
async def accounts(message: types.Message):
    await message.answer(f"Tugmalardan ozingizga kerakini tanlang", reply_markup=menu)

""" Haydovchi kerak\Surxondaryo """
@dp.message_handler(Text(equals=["Surxondaryo"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=surxondaryo)


# Orqaga qaytish
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak) # Orqaga qaytish togri turipdi !


# ------------------------------------------------------------------------------------------------------------------------------------------

""" Haydovchi kerak\Xorazm """
@dp.message_handler(Text(equals=["Xorazm"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=xorazm)

# - Urganch
@dp.message_handler(Text(equals=["Urganch"]))
async def t_urganch(message: types.Message):
    await message.answer(f"Toshkentning qaysi tumaniga borasiz?", reply_markup=toshkent)

# - Urganch-Tumanlari
@dp.message_handler(Text(equals=["Bog'ot"]))
async def t_urganch(message: types.Message):
    await message.answer(f"Toshkentning qaysi tumaniga borasiz?", reply_markup=toshkent)

# - Urganch-tumanlari
@dp.message_handler(Text(equals=["Gurlan"]))
async def t_urganch(message: types.Message):
    await message.answer(f"Toshkentning qaysi tumaniga borasiz?", reply_markup=toshkent)

# - Urganch-Tumanlari
@dp.message_handler(Text(equals=["Xonqa"]))
async def t_urganch(message: types.Message):
    await message.answer(f"Toshkentning qaysi tumaniga borasiz?", reply_markup=toshkent)

# - Urganch-Tumanlari
@dp.message_handler(Text(equals=["Hazorasp"]))
async def t_urganch(message: types.Message):
    await message.answer(f"Toshkentning qaysi tumaniga borasiz?", reply_markup=toshkent)

# - Urganch-Tumanlari
@dp.message_handler(Text(equals=["Xiva"]))
async def t_urganch(message: types.Message):
    await message.answer(f"Toshkentning qaysi tumaniga borasiz?", reply_markup=toshkent)

# - Urganch-Tumanlari
@dp.message_handler(Text(equals=["Qo'shko'pir"]))
async def t_urganch(message: types.Message):
    await message.answer(f"Toshkentning qaysi tumaniga borasiz?", reply_markup=toshkent)

# - Urganch-Tumanlari
@dp.message_handler(Text(equals=["Shovot"]))
async def t_urganch(message: types.Message):
    await message.answer(f"Toshkentning qaysi tumaniga borasiz?", reply_markup=toshkent)

# - Urganch-Tumanlari
@dp.message_handler(Text(equals=["Qorovul (qishloq)"]))
async def t_urganch(message: types.Message):
    await message.answer(f"Toshkentning qaysi tumaniga borasiz?", reply_markup=toshkent)

# - Urganch-Tumanlari
@dp.message_handler(Text(equals=["Yangiariq"]))
async def t_urganch(message: types.Message):
    await message.answer(f"Toshkentning qaysi tumaniga borasiz?", reply_markup=toshkent)

# - Urganch-Tumanlari
@dp.message_handler(Text(equals=["Yangibozor (Yangibozor tumani)"]))
async def t_urganch(message: types.Message):
    await message.answer(f"Toshkentning qaysi tumaniga borasiz?", reply_markup=toshkent)

# - Urganch-Tumanlari
@dp.message_handler(Text(equals=["Pitnak"]))
async def t_urganch(message: types.Message):
    await message.answer(f"Toshkentning qaysi tumaniga borasiz?", reply_markup=toshkent)





# Orqaga qaytish
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak)


""" Haydovchi kerak\Buxoro """
@dp.message_handler(Text(equals=["Buxoro"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=buxaro)


# back
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak)


""" Haydovchi kerak\Andijon """
@dp.message_handler(Text(equals=["Andijon"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=andijon)


# --- Back
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak)


""" Haydovchi kerak\Farg'ona """
@dp.message_handler(Text(equals=["Farg'ona"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=fargona)


# --- Back
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak)


""" Haydovchi kerak\Jizzax """
@dp.message_handler(Text(equals=["Jizzax"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=jizzax)


# --- Back
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak)


""" Haydovchi kerak\Qoshqadaryo """
@dp.message_handler(Text(equals=["Qoshqidaryo"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=qoshqadaryo)


# --- Back
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak)


""" Haydovchi kerak/Namangan"""
@dp.message_handler(Text(equals=["Namangan"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=namangan)




# --- Back
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak)



""" Haydovchi kerak/Navoi"""
@dp.message_handler(Text(equals=["Navoi"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=navoi)


# --- Back
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak)



""" Haydovchi kerak\Sirdaryo """
@dp.message_handler(Text(equals=["Sirdaryo"]))
async def accounts(message: types.Message):
    pass
    # await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=sirdaryo)


# --- Back
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak)



""" Haydovchi kerak\Samarqand """
@dp.message_handler(Text(equals=["Samarkand"]))
async def accounts(message: types.Message):
    pass
    # await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=samarkand)


# --- Back
@dp.message_handler(Text(equals=["Orqaga"]))
async def accounts(message: types.Message):
    await message.answer(f"Siz qaysi viloyatta turibsiz?", reply_markup=Haydovchi_kerak)



""" Haydovchi kerak\Qoraqalpoqistan """ # Ohiri 
@dp.message_handler(Text(equals=["Qoraqalpoqistan"]))
async def accounts(message: types.Message):
    pass
    # await message.answer(f"Siz qaysi tumanda turibsiz?", reply_markup=qoraqalpoqiston)


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



# @dp.message_handler(Text(equals=["🔙 Orqaga"]))
# async def back(message: types.Message):
#     await message.answer("Tugmalardan ozingizga kerakini tanlang", reply_markup=menu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)