a = float(input("Sisesta esimese külje pikkus: "))
b = float(input("Sisesta teise külje pikkus: "))
c = float(input("Sisesta kolmanda külje pikkus: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Kolmnurk on võrdkülgne.")
    elif a == b or b == c or a == c:
        print("Kolmnurk on võrdhaarne.")
    else:
        print("Kolmnurk on erikülgne.")
else:
    print("Selliste külgedega kolmnurk ei eksisteeri.")
