from esercizio import benvenuto

def test_messaggio_base():
    assert benvenuto("Mario", 25) == "Ciao Mario, hai 25 anni!"

def test_nome_diverso():
    assert benvenuto("Sara", 30) == "Ciao Sara, hai 30 anni!"

def test_eta_zero():
    assert benvenuto("Luca", 0) == "Ciao Luca, hai 0 anni!"
