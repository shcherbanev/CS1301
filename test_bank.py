try:
    from test_bank.bank import value
except:
    from bank import value

def test_hello():
    assert value("hello") == 0

def test_hello_upper():
    assert value("HELLO") == 0

def test_h_preceding():
    assert value("hard") == 20

def test_h_preceding_upper():
    assert value("HARD") == 20

def test_else():
    assert value("bla") == 100

def test_else_upper():
    assert value("BLA") == 100