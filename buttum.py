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
        [KeyboardButton(text="Namangan"), KeyboardButton(text="Navoi")],
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
        [KeyboardButton(text="Yunusobod"), KeyboardButton(text="Yashnobod")],
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

# Toshkent ichidagi Yunusobod
yunusobod = ReplyKeyboardMarkup(
    keyboard=[
        
        [KeyboardButton(text="Buxoro"), KeyboardButton(text="Qoraqalpoqiston")],
        [KeyboardButton(text="Andijon"), KeyboardButton(text="Farg'ona")],
        [KeyboardButton(text="Jizzax"), KeyboardButton(text="Qoshqidaryo")],
        [KeyboardButton(text="Namangan"), KeyboardButton(text="Navoi")],
        [KeyboardButton(text="Sirdaryo"), KeyboardButton(text="Samarqand")],
        [KeyboardButton(text="Surxondaryo"), KeyboardButton(text="Xorazm")],
        [KeyboardButton(text="Bosh sahifa"),KeyboardButton(text="Orqaga")],
        
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)

# Toshkent ichidagi Yunusobod ichidagi buxoro
buxaro = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Buxaro shaxri"), KeyboardButton(text="G'ijdivon")],
        [KeyboardButton(text="Qorako'l"), KeyboardButton(text="Kogon")],
        [KeyboardButton(text="Jondor"), KeyboardButton(text="Olot")],
        [KeyboardButton(text="Peshku"), KeyboardButton(text="Qorovulbozor")],
        [KeyboardButton(text="Romiton"), KeyboardButton(text="Shofirkon")],
        [KeyboardButton(text="Vobkent"), KeyboardButton(text="Kogon shahri")],
        
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)

# --- Sonlar 
numbers = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1"), KeyboardButton(text="2"),KeyboardButton(text="3"),KeyboardButton(text="4")],
        [KeyboardButton(text="To'liq salon")],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],

    ],
    resize_keyboard=True,
)

# --- Cars
cars = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Cobalt"), KeyboardButton(text="Lacetti, Gentra")],
        [KeyboardButton(text="Epica")],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],

    ],
    resize_keyboard=True,
)

# -- Pitaka borish yoki shofyor oldiga kelishi
pitak = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Pitakka boraman")],
        [KeyboardButton(text="📍Kelib olib keting, lokatsiya yuboraman", request_location=True)],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],

    ],
    resize_keyboard=True,
)

contact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Telefon raqam", request_contact=True)],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True
)

# --- Toshkent ichidagi tumanlar uchun
# t_viloyatlar = ReplyKeyboardMarkup(
#     keyboard=[
        
#         [KeyboardButton(text="Buxoro"), KeyboardButton(text="Qoraqalpoqiston")],
#         [KeyboardButton(text="Andijon"), KeyboardButton(text="Farg'ona")],
#         [KeyboardButton(text="Jizzax"), KeyboardButton(text="Qoshqidaryo")],
#         [KeyboardButton(text="Namangan"), KeyboardButton(text="Navoi")],
#         [KeyboardButton(text="Sirdaryo"), KeyboardButton(text="Samarqand")],
#         [KeyboardButton(text="Surxondaryo"), KeyboardButton(text="Xorazm")],
#         [KeyboardButton(text="Bosh sahifa"),KeyboardButton(text="Orqaga")],
        
#     ],
#     resize_keyboard=True,
#     # one_time_keyboard=True,
# )  


# \\\ Surxondaryo ichidagi shaxar ///
surxondaryo = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Angor"), KeyboardButton(text="Termiz(sh)")],
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

# --- Xorazm shaxarlar
xorazm = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Urganch"), KeyboardButton(text="Bogʻot")],
        [KeyboardButton(text="Gurlan"), KeyboardButton(text="Xonqa")],
        [KeyboardButton(text="Hazorasp"), KeyboardButton(text="Xiva")],
        [KeyboardButton(text="Qoʻshkoʻpir"), KeyboardButton(text="Shovot")],
        [KeyboardButton(text="Qorovul (qishloq)"), KeyboardButton(text="Yangiariq")],
        [KeyboardButton(text="Yangibozor (Yangibozor tumani)"), KeyboardButton(text="Pitnak")],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)

# --- Andijondagi shaxarlar
andijon = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ulug'nor"),KeyboardButton(text="Oltinko'l")],
        [KeyboardButton(text="Paxtaobod"),KeyboardButton(text="shaxrixon")],
        [KeyboardButton(text="Marhamat"),KeyboardButton(text="Qo'rg'ontepa")],
        [KeyboardButton(text="Buloqboshi"),KeyboardButton(text="Xo'jaobod")],
        [KeyboardButton(text="Izbosgan"),KeyboardButton(text="Andijon shahri")],
        [KeyboardButton(text="Xonaobod shahri"),KeyboardButton(text="Andijon")],
        [KeyboardButton(text="Asaka"),KeyboardButton(text="Baliqchi")],
        [KeyboardButton(text="Bo'ston"),KeyboardButton(text="Jalaquduq")],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],        
    ]
)

# --- Buxorodagi shaharlar
# buxaro = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Buxoro"),KeyboardButton(text="G'ijdivon")],
#         [KeyboardButton(text="Qorako'l"),KeyboardButton(text="Kogon")],
#         [KeyboardButton(text="Jondor"),KeyboardButton(text="Olot")],
#         [KeyboardButton(text="Peshku"),KeyboardButton(text="Qorovulbozor")],
#         [KeyboardButton(text="Romiton"),KeyboardButton(text="Shofirkon")],
#         [KeyboardButton(text="Vobkent"),KeyboardButton(text="Kogon shahri")],
#         [KeyboardButton(text="Buxaro shaxri")],
#         [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],
#     ],
#     resize_keyboard=True,
#     # one_time_keyboard=True,
# )

# --- Farg'onadagi shaharlar
fargona = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Uchko'pir"),KeyboardButton(text="Yozyovon"),KeyboardButton(text="Qo'qon shahar")],
        [KeyboardButton(text="Qo'shtepa"),KeyboardButton(text="Dang'ara"),KeyboardButton(text="Beshariq")],
        [KeyboardButton(text="Toshloq"),KeyboardButton(text="Buvayda"),KeyboardButton(text="Furqat")],
        [KeyboardButton(text="Bog'dod"),KeyboardButton(text="Marg'ilon shahar"),KeyboardButton(text="Quva")],
        [KeyboardButton(text="Rishton"),KeyboardButton(text="Quvasoy shahar"),KeyboardButton(text="So'x")],
        [KeyboardButton(text="Farg'ona shahri"),KeyboardButton(text="Farg'ona"),KeyboardButton(text="Oltiariq")],
        [KeyboardButton(text="O'zbekiston")],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)

# --- Jizzaxdagi shaxarlar
jizzax = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Do'stlik"),KeyboardButton(text="G'allaorol"),KeyboardButton(text="Forish")],
        [KeyboardButton(text="Baxmal"),KeyboardButton(text="Arnasoy"),KeyboardButton(text="Dashobad shaxri")],
        [KeyboardButton(text="Zafarobod"),KeyboardButton(text="Yangiobod"),KeyboardButton(text="Paxtakor")],
        [KeyboardButton(text="Zomin"),KeyboardButton(text="Zomi shahri"),KeyboardButton(text="Mirzacho'l")],
        [KeyboardButton(text="Jizzax"),KeyboardButton(text="Jizzax shahri")],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)

# --- Namangandagi shaharlar
namangan = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Namangan shahri"),KeyboardButton(text="Chartoq"),KeyboardButton(text="Chust")],
        [KeyboardButton(text="Kasansoy"),KeyboardButton(text="Mingbuloq"),KeyboardButton(text="Namangan")],
        [KeyboardButton(text="To'raqo'rg'on"),KeyboardButton(text="Norin"),KeyboardButton(text="Uchqo'rg'on")],
        [KeyboardButton(text="Pop"),KeyboardButton(text="Yangiqo'rg'on"),KeyboardButton(text="Uychi")],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)

# ---- Navoidagi shaharlar
navoi = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Zarafshon shahri"),KeyboardButton(text="Navoi shahri")],
        [KeyboardButton(text="Karmana"),KeyboardButton(text="Konimex")],
        [KeyboardButton(text="Navbahor"),KeyboardButton(text="Qiziltepa")],
        [KeyboardButton(text="Nurota"),KeyboardButton(text="Tomdi")],
        [KeyboardButton(text="Uchquduq"),KeyboardButton(text="Xatarchi")],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],
    ],
)

# --- Qashqadaryodagi shaharlar
qoshqadaryo = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Mirishkor"),KeyboardButton(text="Chiroqchi"),KeyboardButton(text="Kitob")],
        [KeyboardButton(text="Dehqonobod"),KeyboardButton(text="G'uzor"),KeyboardButton(text="Kasbi")],
        [KeyboardButton(text="Kason"),KeyboardButton(text="Yakkabog'"),KeyboardButton(text="Muborak")],
        [KeyboardButton(text="Nishon"),KeyboardButton(text="Qamashi"),KeyboardButton(text="Qarshi")],
        [KeyboardButton(text="Qarshi shahar"),KeyboardButton(text="Shahrisabz shahri")],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],
    ],
)


""" ---- MEn Haydovchiman niki ---- """
men_haydovchiman = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Andijon-Toshkent-Andijon")],
        [KeyboardButton(text="Farg'ona-Toshkent-Farg'ona")],
        [KeyboardButton(text="Buxoro-Toshkent-Buxoro")],
        [KeyboardButton(text="Jizzax-Toshkent-Jizzax")],
        [KeyboardButton(text="Namangan-Toshkent-Namangan")],
        [KeyboardButton(text="Navoi-Toshkent-Navoi")],
        [KeyboardButton(text="Qashqidaryo-Toshkent-Qashqidaryo")],
        [KeyboardButton(text="Qoraqalpoqiston-Toshkent-Qoraqalpaqiston")],
        [KeyboardButton(text="Samarqand-Toshkent-Samarqand")],
        [KeyboardButton(text="Sirdayo-Toshkent-Sirdaryo")],
        [KeyboardButton(text="Surxondaryo-Toshkent-Surxondaryo")],
        [KeyboardButton(text="Xorazm-Toshkent-Xorazm")],
        [KeyboardButton(text="Bosh sahifa"), KeyboardButton(text="Orqaga")],
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)
