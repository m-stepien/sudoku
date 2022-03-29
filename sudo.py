import random

class Sudoku():
    def __init__(self, row=3, col=3):
        self.sudo_tab = [[[0 for x in range(0,3)]for y in range(0,3)]for z in range(0,9)]

    #spoko
    def create_unbound_place(self, i=0):
        numbers = [x for x in range(1, 10)]
        for k in range(3):
            for j in range(3):
                r = random.randint(0, len(numbers)-1)
                a = numbers.pop(r)
                self.sudo_tab[i][j][k] = a

    #spoko
    def print_big_row(self, num):
        n = num * 3
        for j in range(3):
            print("|", end=' ')
            for i in range(n-3, n):
                for k in range(3):
                    print(self.sudo_tab[i][j][k], end=' ')
                print("|", end=' ')
            print()

    #spoko
    def print_full_sudoku(self, separate_row=True):
        if(separate_row):print("-"*25)
        for i in range(1,4):
            self.print_big_row(i)
            if(separate_row):print("-"*25)
    #spoko
    def find_empty(self):
        for x in range(0,len(self.sudo_tab)):
            for y in range(0,len(self.sudo_tab[x])):
                for z in range(0,len(self.sudo_tab[x][y])):
                    if self.sudo_tab[x][y][z] == 0:
                        return [x,y,z]
        return False
    def is_ok(self, x, row, column, box):
        a=self.is_in_row(x, row, box)
        b=self.is_in_column(x, column, box)
        c=self.is_in_box(x, box)
        if a==True or b==True or c==True:
            return False
        else:
            return True
    def backtrack(self):
        position=self.find_empty()

        if(position==False):
            self.print_full_sudoku()
            return True
        else:
            box, row, column = position

        for x in range(1,10):
            ok =self.is_ok(x, row,column,box)
            if ok==True:
                self.sudo_tab[box][row][column]=x
                if(self.backtrack()):
                    return True
            
                self.sudo_tab[box][row][column]=0
        return False



   
    def is_in_box(self, x, n):
        for i in range(3):
            for j in range(3):
                if x==self.sudo_tab[n][i][j]:
                    return True
        return False
    def is_in_column(self,x, column, box):
        if box in [0,3,6]:
            rg = [0,3,6]
        elif box in [1,4,7]:
            rg =[1,4,7]
        else: 
            rg=[2,5,8]
        for j in range(3):
            for i in rg:
                for j in range(3):
                    if x == self.sudo_tab[i][j][column]:
                        return True
            return False
    def is_in_row(self, x, row, box):
        if box//3==0:
            rg = range(0,3)
        elif box//3==1:
            rg=range(3,6)
        else:
            rg=range(6,9)
        for i in rg:
            for j in range(3):
                if x==self.sudo_tab[i][row][j]:
                    return True
        return False




app = Sudoku()

app.create_unbound_place(0)
app.create_unbound_place(4)

app.print_full_sudoku()
app.backtrack()
