otam = {
    "ismi": "Rashid",
    "tug'ilgan_yil": 1984,
    "tug'ilgan_viloyat": "Xorazm",
}
print(f"Otamning ismi {otam['ismi']}, u {otam["tug'ilgan_yil"]}-yilda {otam["tug'ilgan_viloyat"]}da tug'ilgan")

taomlar = {
    "Otam": "osh",
    "Onam": "shashlik",
    "Buvim": "manti",
    "Bobom": "somsa",
    "Opam": "lag'mon",
    "Singlim": "shorva",
}
print(f"Otam {taomlar['Otam']}ni yaxshi ko'radi")

izohli_lugat = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "boolean": "Mantiqiy qiymat",
    "tuple": "O'zgarmas ro'yxat",
}
print(izohli_lugat["integer"])

kalit_soz = input("Kalit so'zni kiriting: ")
print(izohli_lugat.get(kalit_soz, "Bunday kalit so'z mavjud emas"))

my_dict = {"A": 1, "B": 2}
my_dict["C"] = 3
print("1) my_dict:", my_dict)

if "B" in my_dict:
    del my_dict["B"]
print("2) del orqali o'chirilgandan keyin:", my_dict)

kalitlar = list(my_dict.keys())
qiymatlar = list(my_dict.values())
print("3) Kalitlar:", kalitlar)
print("   Qiymatlar:", qiymatlar)

print("4) lug'at ichidagi juftliklar:")
for k, v in my_dict.items():
    print(f"   {k}: {v}")

colors = ["qizil", "yashil", "ko'k", "sariq", "qora"]
fromkeys_dict = dict.fromkeys(colors, "rang")
print("5) fromkeys() bilan:", fromkeys_dict)

kvadrat = {x: x * x for x in range(1, 11)}
print("6) kvadratlar:", kvadrat)

