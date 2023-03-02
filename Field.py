class Field:
    def __init__(self):
        self.bomb = False
        self.num_bomb_near = 0
        self.flag = False
        self.exposed = False

    def is_bomb(self):
        return self.bomb

    def set_bomb(self):
        self.bomb = True

    def set_flag(self):
        self.flag = True

    def unset_flat(self):
        self.flag = False

    def set_num_bomb_near(self, num_bomb_near):
        self.num_bomb_near = num_bomb_near
