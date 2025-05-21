# 1
def hesabla():
    try:
        a = float(input("Birinci rəqəmi daxil edin: "))
        b = float(input("İkinci rəqəmi daxil edin: "))
        emel = input("Əməliyyatı daxil edin (toplama, çıxma, vurma, bölmə): ")
        
        if emel == "toplama":
            print("Nəticə:", a + b)
        elif emel == "çıxma":
            print("Nəticə:", a - b)
        elif emel == "vurma":
            print("Nəticə:", a * b)
        elif emel == "bölmə":
            if b == 0:
                print("0-a bölmək olmaz!")
            else:
                print("Nəticə:", a / b)
        else:
            print("Yanlış əməliyyat daxil edilib.")
    except ValueError:
        print("Rəqəmləri düzgün daxil edin.")
    except TypeError:
        print("Tip xətası baş verdi.")
    finally:
        print("Hesablama bitdi.")

# 2
def bolunenler_11():
    return [i for i in range(1, 51) if i % 11 == 0]

# 3
def ilk_herfler(siyahi):
    return [soz[0] for soz in siyahi]

# 4
def seher_kod_dict(seherler, kodlar):
    return dict(zip(seherler, kodlar))

# 5
km_to_mil = lambda km: km * 0.621371
dəyərlər = [1, 5, 10, 20, 50]
mil_siyahi = list(map(km_to_mil, dəyərlər))

# 6
qiymətlər = [100, 200, 300, 400]
vergi_qiymətlər = list(map(lambda x: x * 1.18, qiymətlər))

# 7
list1 = [3, 7, 12]
list2 = [2, 4, 6]
ikiqat_cem = list(map(lambda x, y: (x * 2) + (y * 2), list1, list2))

# 8
from functools import reduce
qiymətlər2 = [150, 80, 220, 45]
minimum = reduce(lambda a, b: a if a < b else b, qiymətlər2)
