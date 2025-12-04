def hisoblash(x,y,belgi):
    if belgi == "-":
        return f"Ayirma:  {x - y}"
    elif belgi == "+":
        return f"Yigindi:   {x + y}"
    elif belgi == "*":
        return f"Kopaytma:   {x * y}"
    elif belgi == "/":
        return f"Bolinma:   {x / y}"
    elif belgi == "%":
        return f"Foiz:   {x * y / 100}"
    elif belgi == "²":
        return f"Kvadrati:   {x ** y}"
    elif belgi == "√":
        return f"Kvadrati:   {x ** 0.5}"
x=int(input("X ni kiriting:"))
y=int(input("Y ni kiriting:"))
belgi=input("BELGI ni kiriting:")
print(hisoblash(x,y,belgi))
