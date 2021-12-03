from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Haydovchi kerak"), KeyboardButton(text="Pochta yuborish")],
        [KeyboardButton(text="Men haydovchiman"), KeyboardButton(text="Ma'lumotlar")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)

"""___ Haydovchi kerak ninki ___ """
Haydovchi_kerak = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Toshkent"), KeyboardButton(text="Surxondaryo")],
        [KeyboardButton(text="Xorazm"), KeyboardButton(text="Buxoro")],
        [KeyboardButton(text="Andijon"), KeyboardButton(text="Farg'ona")],
        [KeyboardButton(text="Jizzax"), KeyboardButton(text="Qoshqidaryo")],
        [KeyboardButton(text="Namamngan"), KeyboardButton(text="Navoi")],
        [KeyboardButton(text="Sirdaryo"), KeyboardButton(text="Samarqand")],
        [KeyboardButton(text="Qoraqalpoqiston")],
        [KeyboardButton(text="Bosh sahifa", reply_markup=menu)],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)

# -- \\\ Toshkentni ichidagi shaharlar ///
toshkent = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Yunusobod"), KeyboardButton(text="Yshnobod")],
        [KeyboardButton(text="Yakkasaroy"), KeyboardButton(text="Shayxontohur")],
        [KeyboardButton(text="Chilonzor"), KeyboardButton(text="Olmazor")],
        [KeyboardButton(text="Sergeli"), KeyboardButton(text="Mirobod")],
        [KeyboardButton(text="Mirzo Ulug'bek"), KeyboardButton(text="Bektemir")],
        [KeyboardButton(text="Uchtepa"), KeyboardButton(text="Qibray")],
        [KeyboardButton(text="Piskent"), KeyboardButton(text="Parkent")],
        [KeyboardButton(text="Bo'ka"), KeyboardButton(text="Bekobod shahri")],
        [KeyboardButton(text="Angren shahri")],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)

# \\\ Surxondaryo ///
surxondaryo = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Angor"), KeyboardButton(text="Termiz sh")],
        [KeyboardButton(text="Bandixon"), KeyboardButton(text="Boysun")],
        [KeyboardButton(text="Denov"), KeyboardButton(text="Jarqo'rg'on")],
        [KeyboardButton(text="Muzrobot"), KeyboardButton(text="Oltinsoy")],
        [KeyboardButton(text="Qiziriq"), KeyboardButton(text="Qumqo'rg'on")],
        [KeyboardButton(text="Sariosiyo"), KeyboardButton(text="Sherobod")],
        [KeyboardButton(text="Sho'rchi"), KeyboardButton(text="Termiz")],
        [KeyboardButton(text="Uzun")],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)


""" ---- MEn Haydovchiman niki ---- """
men_haydovchiman = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Andijon-Toshkent-Andijon"), KeyboardButton(text="Farg'ona-Toshkent-Farg'ona")],
        [KeyboardButton(text="Buxoro-Toshkent-Buxoro"), KeyboardButton(text="Jizzax-Toshkent-Jizzax")],
        [KeyboardButton(text="Namangan-Toshkent-Namangan"), KeyboardButton(text="Navoi-Toshkent-Navoi")],
        [KeyboardButton(text="Qashqidaryo-Toshkent-Qashqidaryo"), KeyboardButton(text="Qoraqalpoqiston-Toshkent-Qoraqalpaqiston")],
        [KeyboardButton(text="Samarqand-Toshkent-Samarqand"), KeyboardButton(text="Sirdayo-Toshkent-Sirdaryo")],
        [KeyboardButton(text="Surxondaryo-Toshkent-Surxondaryo"), KeyboardButton(text="Xorazm-Toshkent-Xorazm")],
    
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)


andijon=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ulug'nor"),KeyboardButton(text="Oltinko'l")],
        [KeyboardButton(text="Paxtaobod"),KeyboardButton(text="shaxrixon")],
        [KeyboardButton(text="Marhamat"),KeyboardButton(text="Qo'rg'ontepa")],
        [KeyboardButton(text="Buloqboshi"),KeyboardButton(text="Xo'jaobod")],
        [KeyboardButton(text="Izbosgan"),KeyboardButton(text="Andijon shahri")],
        [KeyboardButton(text="Xonaobod shahri"),KeyboardButton(text="Andijon")],
        [KeyboardButton(text="Asaka"),KeyboardButton(text="Baliqchi")],
        [KeyboardButton(text="Bo'ston"),KeyboardButton(text="Jalaquduq")],        
    ]
)