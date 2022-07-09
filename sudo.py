import random
from operator import itemgetter
class Sudoku():
    def __init__(self):
        self.sudo_tab = [[[0 for x in range(0,3)]for y in range(0,3)]for z in range(0,9)]
        self.all_solution = []
    def is_equeal(self, sudoku2):
        wrong_index=[]
        i=0
        while(i<len(self.sudo_tab)):
            j=0
            while(j<len(self.sudo_tab[i])):
                k=0
                while(k<len(self.sudo_tab[j])):
                    if(self.sudo_tab[i][j][k]!=sudoku2.sudo_tab[i][j][k]):
                        wrong_index.append(27*(i//3)+((i%3)*3)+k+9*j)
                    k+=1
                j+=1
            i+=1
        return wrong_index
    def create_unbound_place(self, i=0):
        numbers = [x for x in range(1, 10)]
        for k in range(3):
            for j in range(3):
                r = random.randint(0, len(numbers)-1)
                a = numbers.pop(r)
                self.sudo_tab[i][j][k] = a
    def create_from_list(self, sudoku_list):
        for element in sudoku_list:
            x=0
            z=element[0]%3
            x=(element[0]//27)*3+((element[0]%9)//3)
            y=(element[0]%27)//9
            self.sudo_tab[x][y][z]=int(element[1])
    def print_big_row(self, num):
        n = num * 3
        for j in range(3):
            print("|", end=' ')
            for i in range(n-3, n):
                for k in range(3):
                    print(self.sudo_tab[i][j][k], end=' ')
                print("|", end=' ')
            print()
    def print_full_sudoku(self, separate_row=True):
        if(separate_row):print("-"*25)
        for i in range(1,4):
            self.print_big_row(i)
            if(separate_row):print("-"*25)
    def find_empty(self):
        for x in range(0,len(self.sudo_tab)):
            for y in range(0,len(self.sudo_tab[x])):
                for z in range(0,len(self.sudo_tab[x][y])):
                    if self.sudo_tab[x][y][z] == 0:
                        return [x,y,z]
        return False
    def is_in_other_solution(self, x, row, column, box):
        for solution in self.all_solution:
            if x == solution[box][row][column]:
                return True
        return False
    def is_ok(self, x, row, column, box):
        a=self.is_in_row(x, row, box)
        b=self.is_in_column(x, column, box)
        c=self.is_in_box(x, box)
        # d=self.is_in_other_solution(self, x, row, column, box)
        if a==True or b==True or c==True:
            return False
        else:
            return True
    def backtrack(self):
        position=self.find_empty()

        if(position==False):
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
    def find_all_solution(self):
        self.sudoku_start = self.sudo_tab
        flag = True
        while flag:
            self.sudo_tab=self.sudoku_start
            sol = self.backtrack()
            if(sol==False):
                flag=False
            self.all_solution.append(self.sudo_tab)
        

        


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
    def set_to_blank(self, num_of_blank):
        place_list = []
        for x, e in enumerate(self.sudo_tab):
            for y, f in enumerate(e):
                for z, g in enumerate(f):
                    place_list.append([x,y,z])
        for i in range(num_of_blank):
            ind_delete = random.randint(0, len(place_list)-1)
            dell = place_list[ind_delete]
            self.sudo_tab[dell[0]][dell[1]][dell[2]]=0
            place_list.pop(ind_delete)
    def get_values_location(self):
        val_loc = []
        index = 0
        for h in range(0,3):
            for x in range(0,3):
                for y in range(0,3):
                    for z in range(0,3):

                        val_loc.append({"index":index, "value":self.sudo_tab[h*3+y][x][z]})
                        index+=1                   
        return val_loc                  
