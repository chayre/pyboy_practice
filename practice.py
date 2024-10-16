import pyboy
from pyboy import PyBoy
from pyboy.plugins.game_wrapper_pokemon_gen1 import GameWrapperPokemonGen1  

rom_path = "/home/cayres/projects/pyboy_practice/rom/PokemonRed.gb"
pyboy = PyBoy(rom_path, window="SDL2")
game_wrapper = pyboy.game_wrapper

while pyboy.tick():  # 3c49
    game_wrapper.post_tick()
    print(game_wrapper) 
pyboy.stop()