class GuiTerminal:
    def __init__(self):
        pass

    def get_len_board_from_user(self):

        good_value = False
        while not good_value:
            print("Please enter length of board")
            length = input()
            good_value = self.__validate_is_int__(length)

        return int(length)


    def get_num_bomb_from_user(self):

        good_value = False
        while not good_value:
            print("Please enter number of bomb")
            num = input()
            good_value = self.__validate_is_int__(num)

        return int(num)

    def __validate_is_int__(self, num):
        try:
            if type(num)==float:
                print("It must by integer")
                return True
            num = int(num)
            return num
        except ValueError:
            print("It must by a number")
            return False



