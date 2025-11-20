import funkcje as funkcje

#def test_add():
#    assert funkcje.add(2, 4) == 6
#    assert not funkcje.add(2, 3) == 6

# uruchiamy w konsoli: python -m pytest test_with_pytest.py
# szablon:             python -m <nazwa modułu> <nazwa programu>

def test_if_palindrom():
    assert funkcje.if_palindrom("kamilslimak") # == True
    assert not funkcje.if_palindrom("kamyk") # == True
