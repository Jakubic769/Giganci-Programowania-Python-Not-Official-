
def add(a, b):
    return a + b

#true albo false czy jest palidron czy cos (kajak ze jest tak samo od tylu czy cos XD)

def if_palindrom(word):
    return word == word[::-1]

def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Nie dziel przez 0")

def test_divide(capsys):
    funkcje.divide(4, 2)
    out, err = capsys.readouterr()
    assert out == '2.0\n'
