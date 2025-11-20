a = float(input("podaj pierwszy bok trójkąta"))
b = float(input("podaj drugi bok trójkąta"))
c = float(input("podaj trzeci bok trójkąta"))

if a >= b and a >= c:
        najdluzszy_bok = a
        print(f"Najdłuższy bok to: {najdluzszy_bok} (pierwszy bok)")
elif b >= a and b >= c:
        najdluzszy_bok = b
        print(f"Najdłuższy bok to: {najdluzszy_bok} (drugi bok)")
else:
        najdluzszy_bok = c
        print(f"Najdłuższy bok to: {najdluzszy_bok} (trzeci bok)")

if a + b > c and a + c > b and b + c > a:
    obwod = a + b + c
    print(f"Obwód trójkąta wynosi: {obwod}")

    if a == b == c:
        print("Trójkąt jest równoboczny.")
    elif a == b or b == c or a == c:
        print("Trójkąt jest równoramienny.")
    else:
        print("Trójkąt jest różnoboczny.")

    if (a**2 + b**2 == c**2):
        print("Trójkąt jest prostokątny.")
        
    elif a**2 + b**2 > c**2:
        print("Trójkąt jest ostrokątny.")
        
    else:
        print("Trójkąt jest rozwartokątny.")
        
else:
     print("Podane boki nie mogą tworzyć trójkąta.")
     
        