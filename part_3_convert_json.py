import cc_classes
import json
import cc_dat_utils


#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

def make_levels(files):
    with open(files) as reader:
        game_data = json.load(reader)
        levels = game_data["levels"]
    level_pack = cc_classes.CCLevelPack()
    for level in levels:
        new_level = cc_classes.CCLevel()
        level_number = level["level"]
        new_level.level_number = level_number
        time = level["time"]
        new_level.time = time
        chip_number = level["chip_number"]
        new_level.num_chips = chip_number
        upper_layer = level["upper_layer"]
        new_level.upper_layer = upper_layer
        map_title = level["map_title"]
        new_level.add_field(cc_classes.CCMapTitleField(map_title))
        monsters = level["monsters"]
        coordinates_list = []
        for x, y in monsters:
            coordinates = cc_classes.CCCoordinate(x, y)
            coordinates_list.append(coordinates)

        monster_field = cc_classes.CCMonsterMovementField(coordinates_list)
        new_level.add_field(monster_field)
        password = level["passwords"]
        password_field = cc_classes.CCEncodedPasswordField(password)
        new_level.add_field(password_field)
        level_pack.add_level(new_level)
    return level_pack



game_file = "data/test_game_data.json"

with open(game_file, "r") as reader:

    game_json_data = json.load(reader)

game_pack = make_levels(game_file)
cc_dat_utils.write_cc_level_pack_to_dat(game_pack, "C:/Users/ehern/Downloads/python/tworld-1.3.2-win32/sets/ejhernan.dat")