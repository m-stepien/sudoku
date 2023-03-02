from Board import Board
from GuiTerminal import GuiTerminal

gui = GuiTerminal()
ln_board = gui.get_len_board_from_user()
num_bomb = gui.get_num_bomb_from_user()
brd = Board(ln_board, num_bomb)
brd.set_mine()
