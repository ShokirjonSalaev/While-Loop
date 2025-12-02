# To'g'ri parol
togri_parol = "python123"

# Urinishlar hisoblagichi
urinishlar = 3

# Muvaffaqiyat bayrog'i
muvaffaqiyat = False

print("Tizimga kirish")
print("=" * 30)

while urinishlar > 0:
    # Foydalanuvchidan parol so'rash
    kiritilgan_parol = input(f"Parol kiriting ({urinishlar} urinish qoldi): ")

    # Parolni tekshirish
    if kiritilgan_parol == togri_parol:
        print("✅ Parol to'g'ri! Tizimga xush kelibsiz!")
        muvaffaqiyat = True
        break  # To'g'ri kiritildi, tsikldan chiqamiz
    else:
        urinishlar -= 1  # Urinishlarni kamaytirish

        if urinishlar > 0:
            print(f"❌ Parol noto'g'ri! Yana {urinishlar} urinish qoldi.")
        else:
            print("❌ Barcha urinishlar tugadi. Hisob bloklandi!")

# Agar parol to'g'ri kiritilmagan bo'lsa
if not muvaffaqiyat:
    print("Iltimos, keyinroq urinib ko'ring yoki adminstratorga murojaat qiling.")