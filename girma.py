# # 1- masala
#
# def kvadrat(son):
#     x = son ** 2
#     return x
# x = int(input("Sonni kiriting:"))
# print(f"{x} sonining kvadrati: {kvadrat(x)}")
from idlelib.colorizer import matched_named_groups




# 2- masala

# def takrorlash(matn, n):
#     return matn * n
# print(takrorlash("salom", 3))





 # 3-masala
# def juftmi(x):
#        if x % 2 == 0:
#            return f"javob: juft"
#        elif x % 2 == 1:
#            return f"javob: toq"
# x = int(input("X ni kiriting:"))
# print(juftmi(x))



# 4 masala
# def hisoblash(x,y,belgi):
#     if belgi  == "+":
#         return x + y
# x=int(input("X ni kiriting:"))
# y=int(input("Y ni kiriting:"))
# belgi=input("BELGI ni kiriting:")
# print(hisoblash(x,y,belgi))





 #5 - masala
# def uzunlik(matn):
#     hisob = 0
#     for harf in matn:
#         hisob += 1
#     return f"Uzunlik:{hisob}"
# matn =input("Matnni kiriting:")
#
# print(uzunlik(matn))



# 6 -masala
# def son_turi(son):
#
#     if son > 0:
#         return "musbat"
#     elif son < 0:
#         return "manfiy"
#     else:
#         return "nol"
# print(son_turi(42))
# print(son_turi(-7))





# 7 -masala
# def abs_qiymat(son):
#
#     if son < 0:
#         return -son
#     else:
#         return son
# print(abs_qiymat(-7))
# print(abs_qiymat(12))
# print(abs_qiymat(0))




# 8- masala
# def teskari_matn(matn):
#     return matn[::-1]
# print(teskari_matn("salom"))

# 2  modul
# 1 -masala

# def faktorial(n):
#
#     if n == 0 or son == 1:
#         return 1
#     else:
#         return n * faktorial(n -1)
# print(faktorial(5))




# 2 -masala
# def juft_sum(royxat):
#     yigindi = 0
#     for son in royxat:
#         if son % 2 == 0:
#             yigindi += son
#     return yigindi
# royxat = [1,2,3,4,6]
# print(juft_sum(royxat))
# 3- masala
# def unililar_soni(matn):
#     if matn == "":
#         return 0
#     birinchi = 1 if matn[0].lower() in "aeiou" else 0
#     return birinchi + unililar_soni(matn[1:])
# n = input("matnni kiriting:")
# print(unililar_soni(n))
# #

#
#
#
#
# # 4-masala
# def daraja(son, dar):
#
#     if dar == 0:
#         return 1
#
#
#     return son * daraja(son, dar - 1)
#
# print(daraja(2, 3))  # 8
# print(daraja(5,4))




#5 -masala

# def maksimal(royxat):
#     if len(royxat) == 1:
#         return royxat[0]
#     else:
#         return royxat[0] if royxat[0] > maksimal(royxat[1:]) else maksimal(royxat[1:])
#
#
# print(maksimal([4, 8, 2, 15, 7]))


# 6- masala


# def chiroyli_matn(matn):
#     if not matn:
#         return ""
#     natija = ""
#     yangi_soz = True
#     for harf in matn:
#         if yangi_soz:
#             natija += harf.upper()
#             yangi_soz = False
#         else:
#             natija += harf.lower()
#         if harf == " ":
#             yangi_soz = True
#     return natija
# print(chiroyli_matn("salom dunyo"))


# 7 -masala

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(6))
#


# 3 - bolim

 # 1-masala
