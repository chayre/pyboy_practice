from pyboy import PyBoy
pyboy = PyBoy('PokemonRed.gb')
while pyboy.tick():
    pass
pyboy.stop()