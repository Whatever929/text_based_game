import random
from typing import Tuple, Dict, List


class Room(object):
    def __init__(self, size: Tuple, database=None) -> None:
        self.generate_room_content = self.room_content_generator()
        self.generate_room_arrangement = self.room_arrangement_generator()
        self.size = size
        self.map = self.generate_map(size)

    def generate_map(self, size: Tuple) -> Dict:
        map = {}
        # This one might be replaced by a map landscape generator.
        for i in range(1, size[0] + 1):
            for j in range(1, size[1] + 1):
                map[str(i) + " " + str(j)] = [next(self.generate_room_content),
                                        next(self.generate_room_arrangement)]
        key = str(random.randint(1, size[0])) + " " + str(random.randint(1, size[1]))
        map[key].append("Key")
        return map

    def room_content_generator(self) -> List:
        while True:
            room_content = []
            if random.random() < 0.1:
                room_content.append("Traps")
            if random.random() < 0.3:
                room_content.append("Items")
            if random.random() < 0.3:
                room_content.append("Monster")
            yield room_content

    def room_arrangement_generator(self) -> List:
        possible_arrangement = ["Lamp", "Corpse", "Window", "Traces of blood"]
        while True:
            room_arrangement = []
            if random.random() < 0.1 and possible_arrangement:
                arrangement = random.choice(possible_arrangement)
                room_arrangement.append(arrangement)
                possible_arrangement.remove(arrangement)
            yield room_arrangement

    def access_room(self, room_number: str) -> List:
        return self.map[room_number]

    def show_map(self) -> str:
        map_index = list(self.map)
        last_column = "1"
        last_row = "1"
        map = ""
        for i in map_index:
            i = i.split(" ")
            if i[0] != last_row:
                last_row = i[0]
                map += "\n"
                if i[1] != "1":
                    for i in range(int(i[1]) - 1):
                        map += "⨉ "
                    map += "☐ "
                    last_column = i[1]
                else:
                    last_column = i[1]
                    map += "☐ "
            else:
                if int(i[1]) != (int(last_column) + 1):
                    for i in range(int(i[1]) - int(last_column)):
                        map += "⨉ "
                    map += "☐ "
                    last_column = i[1]
                else:
                    map += "☐ "
                    last_column = i[1]
        return map

if __name__ == "__main__":
    room_a = Room((10, 15))
    for location, contents in room_a.map.items():
        print("The room {} has {}".format(location, contents))
    print(room_a.show_map())
