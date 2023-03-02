import random
from Field import Field


class Board:
    def __init__(self, len, num_bomb):
        self.height = len
        self.width = len
        self.board_arr = self.__generate_board__()
        self.num_bomb = num_bomb

    def __generate_board__(self):
        brd = []
        for x in range(0, self.height):
            line = []
            for y in range(0, self.height):
                line.append(Field())
            brd.append(line)
        return brd

    def __get_list_of_all_poss_position__(self):
        all_poss = []
        for idx_1, e in enumerate(self.board_arr):
            for idx_2, i in enumerate(e):
                all_poss.append(tuple([idx_1, idx_2]))
        return all_poss

    def set_mine(self):
        all_poss = self.__get_list_of_all_poss_position__()
        for n in range(0, self.num_bomb - 1):
            chosen_field_position = random.choice(all_poss)
            all_poss.pop(all_poss.index(chosen_field_position))
            self.board_arr[chosen_field_position[0]][chosen_field_position[1]].set_bomb()

    def is_bomb_on_position(self, x, y):
        return self.board_arr[y][x].is_bomb()

    def set_num_near_bomb_for_all_fields(self):
        all_neighbors = tuple([[0, 1], [1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1], [0, -1], [-1, 0]])
        for y, row in enumerate(self.board_arr):
            for x, field in enumerate(row):
                count = 0
                for neighboor in all_neighbors:
                    i = neighboor[0]
                    j = neighboor[1]
                    if self.board_arr[i][j].is_bomb():
                        count += 1
