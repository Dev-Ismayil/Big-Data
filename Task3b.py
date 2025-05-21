# 1
def salam():
    print("Salam, Dünya!")

# 2
def kub_hesabla(n):
    return n ** 3

# 3
def birlesdir(soz1, soz2):
    return f"{soz1} {soz2}"

# 4
def cap_et(lst):
    for item in lst:
        print(item)

# 5
def toplam(*args):
    return sum(args)

# 6
def ortalama(*args):
    if len(args) == 0:
        return "Rəqəm yoxdur"
    return sum(args) / len(args)

# 7
def adlar_rəqəmlər(**kwargs):
    for ad, reqem in kwargs.items():
        print(f"ad: {ad}, rəqəm: {reqem}")

# 8
def tip_yoxla(dəyər):
    if isinstance(dəyər, str):
        print("mətn")
    elif isinstance(dəyər, (int, float)):
        print("rəqəm")
    else:
        print("başqa")

# 9
def yas_kateqoriya():
    yas = int(input("Yaşınızı daxil edin: "))
    if yas < 18:
        print("Gənc")
    else:
        print("Yetkin")

# 10
def soz_uzunluq():
    soz = input("Söz daxil edin: ")
    print(len(soz))
