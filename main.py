def salomlash(ism,fam):
    text = f"Assalomu alaykum hurmatli {ism} {fam}, jamoamizga xush kelibsiz!"
    return text
ism = input("Ismingizni kiriting:  ").title()
fam = input("Familyangizni kiriting: ").title()
print(salomlash(ism, fam))
