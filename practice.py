import pyboy
from pyboy import PyBoy
from pyboy.plugins.game_wrapper_pokemon_gen1 import GameWrapperPokemonGen1  

# Path to ROM
rom_path = "/home/cayres/projects/pyboy_practice/rom/PokemonRed.gb"

# Initialize PyBoy with SDL2 window (you can change this to another window backend)
pyboy = PyBoy(rom_path, window="SDL2")

# Access the game wrapper, which provides various methods to interact with the game
game_wrapper = pyboy.game_wrapper

def print_sprites():
    # Get the OAM (Object Attribute Memory) for sprites from pyboy directly
    oam_sprites = pyboy.memory[0xFE00:0xFE9F]
    
    # Print the length of the OAM memory to verify the size
    print(f"Size of OAM Sprites Memory: {len(oam_sprites)} bytes")
    print("First few bytes of OAM: ", oam_sprites[:160])  # Print the first 160 bytes for inspection

    print("\n--- Sprites ---")
    for i in range(0, len(oam_sprites), 4):
        # Each sprite consists of 4 bytes in the OAM
        # The format is: [Y Position, X Position, Tile Index, Attributes]
        if i + 3 < len(oam_sprites):
            y_pos = oam_sprites[i]  # Y-coordinate
            x_pos = oam_sprites[i+1]  # X-coordinate
            tile_id = oam_sprites[i+2]  # Tile identifier (Sprite Graphics)
            attributes = oam_sprites[i+3]  # Attributes (Flip, Priority, Palette, etc.)
            
            # Extract additional sprite information
            flipped_x = bool(attributes & 0x20)  # X flip
            flipped_y = bool(attributes & 0x40)  # Y flip
            on_screen = True if (x_pos != 0 and y_pos != 0) else False  # Simple check for visibility
            
            # Print sprite details
            print(f"Sprite Position: ({x_pos}, {y_pos}), Tile ID: {tile_id}, Flipped X: {flipped_x}, Flipped Y: {flipped_y}, On Screen: {on_screen}")
        else:
            print(f"Invalid sprite data at index {i}, skipping.")

while pyboy.tick(15, True):  # Render 30 frames at a time and only display final frame
    game_wrapper.post_tick()
    print_sprites()
    #print(game_wrapper) 
pyboy.stop()