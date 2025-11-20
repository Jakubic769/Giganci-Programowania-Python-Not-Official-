x = input("czy jesteś pełnoletni? napisz ile masz lat")
if x > 18 or x == 18:
    print("Weryfikacja zakonczona sukcesem")
elif x < 18:
    y = 18 - x
    print(f"nie jesteś jescze pełnoletni! brakuje ci {y} lat!")