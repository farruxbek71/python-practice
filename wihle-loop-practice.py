# Takrorlanish operatorlari 
# 1. for loop 
# 2. while loop

# 1 dan 10 gacha sonlar ketma-ketligini chiqaring
# for son in range(1,11):
#     print(son)

# son = 1
# while son < 11:
    # print(son)
    # son += 1
    
# Infinity loop - cheksiz tsikl
# while True: # Cheksiz tsikl
#     print("Infinity loop") 

# while va input
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat=input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# break sindirish operatori
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: 
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# continue(davom etish) operator
# for son in sonlar:
    # if son == 7:
        # continue

    # print(f"{son} ning kvadrati {son**2} ga teng")
# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)
# 1
# savol = "Yoqtirgan kitobingizni kiriting"
# savol += "(hamma kitoblarni kiritgandan keyin 'exit' deb yozing): "
# while True:
#     kitoblar = input(savol)
#     if kitoblar == 'exit':
#         break
# print("So'rov to'xtadi")

# 2.
# savol = "Yoshingiz nechida? Yoshingizni kiriting, sizga chipta narxini chiqarib beraman: "

# while True:
#     print("Agar 'exit' va 'quit' deb yozsangiz, dastur to'xtaydi")
#     yosh = input(savol)
#     if yosh == 'exit' or yosh == 'quit':
#         print("Dastur to'xtadi")
#         break
#     yosh = int(yosh)
#     if yosh<7:
#         print("Sizga 2000 so'm")
#     elif yosh>=7 and yosh < 18:
#         print("Sizga 3000 so'm")
#     elif yosh>=18 and yosh < 65:
#         print("Sizga 10000 so'm")
#     else:
#         print("Sizga Bepul")

