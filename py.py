#1-masala
# def salomlash(ism,fam):
#    text = f"Assalomu alaykum hurmatli {ism} {fam}, jamoamizga xush kelibsiz!"
#    return text
# ism = input("Ismingizni kiriting:  ").title()
# fam = input("Familyangizni kiriting: ").title()
# print(salomlash(ism, fam))




#2-masala

# def maksimal(royxat):
#     if len(royxat) == 1:
#         return royxat[0]
#     else:
#         return royxat[0] if royxat[0] > maksimal(royxat[1:]) else maksimal(royxat[1:])
#
#
# print(maksimal([4, 8, 2, 15, 7]))





##3-msala
# def teskari_matn(matn):
#     return matn[::-1]
# print(teskari_matn("salom"))




# # 4 masala
# def hisoblash(x,y,belgi):
#     if belgi  == "+":
#         return x + y
# x=int(input("X ni kiriting:"))
# y=int(input("Y ni kiriting:"))
# belgi=input("BELGI ni kiriting:")
# print(hisoblash(x,y,belgi))
#





#5-masala


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




#6 -masala
# def juftmi(x):
#        if x % 2 == 0:
#            return f"javob: juft"
#        elif x % 2 == 1:
#            return f"javob: toq"
# x = int(input("X ni kiriting:"))
# print(juftmi(x))



# ##7-masala
# def harf_sanash(matn):
#     lugat={}
#     for harf in matn: lugat[harf]=lugat.get(harf,0)+1
#     return lugat
# print(harf_sanash("hello"))
# print(harf_sanash("python"))




# 8-masala
# def palindrommi(matn):
#      return matn==matn[::-1]
# print(palindrommi("abba"))
# print(palindrommi("level"))
# print(palindrommi("python"))
# print(palindrommi("1221"))




#9-masala
# def kvadrat(son):
#     x = son ** 2
#     return x
# x = int(input("Sonni kiriting:"))
# print(f"{x} sonining kvadrati: {kvadrat(x)}")



 ##10-masala
# def musbat_sonlar(sonlar): return [x for x in sonlar if x>0]
# print(musbat_sonlar([1,-2,3,-4,5]))
# print(musbat_sonlar([-5,-3]))
# print(musbat_sonlar([5,10,15]))



#11-masala

# def faktorial(n):
#
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * faktorial(n -1)
# print(faktorial(5))




 ##11-masala
# def faktorial(son):
#     natija=1
#     for i in range(1,son+1): natija*=i
#     return natija
# print(faktorial(5))
# print(faktorial(1))
# print(faktorial(10))
# ##12-masala
# def lugat_birlash(lugat1,lugat2):
#     for k in lugat2: lugat1[k]=lugat2[k]
#     return lugat1
# print(lugat_birlash({'a':1,'b':2},{'c':3,'d':4}))
# print(lugat_birlash({'a':10},{'a':20,'b':30}))
# ##13-masala
# def fibonacci(n):
#     ketma_ketlik=[0,1]
#     for i in range(n-2): ketma_ketlik.append(ketma_ketlik[-1]+ketma_ketlik[-2])
#     return ketma_ketlik[:n]
# print(fibonacci(10))
# print(fibonacci(5))
# print(fibonacci(1))
# ##14-masala
# def tekisla(ichki_list):
#     natija=[]
#     for el in ichki_list:
#         if type(el)==list: natija+=tekisla(el)
#         else: natija.append(el)
#     return natija
# print(tekisla([1,[2,3],[4,[5,6]]]))
# print(tekisla([[1,2],[3,[4,5]]]))
# ##15-masala
# def anagrammi(s1,s2): return sorted(s1)==sorted(s2)
# print(anagrammi("listen","silent"))
# print(anagrammi("hello","world"))
# print(anagrammi("abc","cba"))
# ##16-masala
# def dublikat_ochir(lst):
#     natija=[]
#     for x in lst:
#         if x not in natija: natija.append(x)
#     return natija
# print(dublikat_ochir([1,2,3,3,4,5,5]))
# print(dublikat_ochir(['a','b','a','c']))
# ##17-masala
# def eng_kop_takror(lst):
#     m=lst[0]; c=lst.count(m)
#     for x in lst:
#         if lst.count(x)>c: m=x; c=lst.count(x)
#     return m
# print(eng_kop_takror([1,2,3,3,3,2]))
# print(eng_kop_takror(['a','b','a','a']))
# ##18-masala
# def zip_birlash(ro_yxat1,ro_yxat2):
#     natija=[]
#     for i in range(min(len(ro_yxat1),len(ro_yxat2))): natija.append((ro_yxat1[i],ro_yxat2[i]))
#     return natija
# print(zip_birlash(["Ali","Vali","Hasan"],[20,21,19]))
# ##19-masala
# def yigindi_son(n):
#     natija=0
#     for i in range(n+1): natija+=i
#     return natija
# print(yigindi_son(1000000))
# ##20-masala
# def fib_gen(n):
#     a,b=0,1
#     for _ in range(n): yield a; a,b=b,a+b
# for x in fib_gen(10): print(x,end=" ")
# print()
# ##21-masala
# def merge_sort(lst):
#     if len(lst)<=1: return lst
#     m=len(lst)//2
#     chap=merge_sort(lst[:m])
#     ong=merge_sort(lst[m:])
#     natija=[]; i=j=0
#     while i<len(chap) and j<len(ong):
#         if chap[i]<ong[j]: natija.append(chap[i]); i+=1
#         else: natija.append(ong[j]); j+=1
#     return natija+chap[i:]+ong[j:]
# print(merge_sort([64,34,25,12,22,11,90]))
# ##22-masala
# fib_xotira={}
# def fib_mem(n):
#     if n in fib_xotira: return fib_xotira[n]
#     if n<=1: return n
#     fib_xotira[n]=fib_mem(n-1)+fib_mem(n-2)
#     return fib_xotira[n]
# print(fib_mem(50))
# print(fib_mem(70))











