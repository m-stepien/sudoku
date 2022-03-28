import random
#walidacja w rzedzie
"""
zmiana 3 na zmienne
napisanie backtrackingu
zamiana sortowania na quicksort
napisanie testow jednostkowych
"""

class Sudoku():
    def __init__(self):
        self.sudo_tab = [Square() for x in range(9)]

    def get_used_in_column(self, n ,box_ind\
        ):
        # n to macierz trzeba iterować po jej szerokości
        list_used_set = []
        for j in range(3):
            used_set = set()
            for i in [1,4,7]:
                for k in range(3):
                    used_set.add(self.sudo_tab[box_ind].croot[k][j])
            used_set=used_set.difference({0})
            list_used_set.append(used_set)
        return list_used_set
    def get_used_in_row(self, n):
        # n liczone od jeden z powodu sprawdzania podzielności w przypadku z 0 nie zadziała poprawnie
        list_used_set = []
        for j in range(3):
            used_set = set()
            for i in range(3*n, 3*n+3):
                for k in range(3):
                    used_set.add(self.sudo_tab[i].croot[j][k])
            used_set=used_set.difference({0})
            list_used_set.append(used_set)
        return list_used_set

#tutaj trójka musi byc zastąpiona wysokością prostokątów wewnętrznych
        r = n//3
        for i in range(3):
            used_set.add(self.sudo_tab[r].croot[n][i])
        used_set.difference({0})
        return used_set
    def print_row(self, num):
        n = num * 3
        for j in range(3):
            print("|", end=' ')
            for i in range(n-3, n):
                for k in range(3):
                    print(self.sudo_tab[i].croot[j][k], end=' ')
                print("|", end=' ')
            print()


    def print_full_sudoku(self, separate_row=True):
        if(separate_row):print("-"*25)
        for i in range(1,4):
            self.print_row(i)
            if(separate_row):print("-"*25)
    
    def find_empty(self):
        for x in range(0,len(self.sudo_tab)):
            for y in range(0,len(self.sudo_tab[x].croot)):
                for z in range(0,len(self.sudo_tab[x].croot[y])):
                    if self.sudo_tab[x].croot[y][z] == 0:
                        print(x,y,z)
                        return [x,y,z]
        return False
    def test_backtrack(self):
        position=self.find_empty()
        if(position==False):
            return True
        else:
            box, row, column = position








class Square():

    def __init__(self, unr=[], unc=[]):
        self.croot = [[0 for x in range(3)] for z in range(3)]
        self.sbu = None

    def create_unbound_place(self):
        numbers = [x for x in range(1, 10)]
        for i in range(3):
            for j in range(3):
                r = random.randint(0, len(numbers)-1)
                a = numbers.pop(r)
                self.croot[i][j] = a


    def create_list_union(self, use_num_row=[], use_num_column=[]):
        li = []
        record = []
        sorted_index = []
        y = 0
        while(y < 3):
            i = 0
            while(i < 3):
                union = set(use_num_row[y]).union(set(use_num_column[i]))
                record = [y, i, union]
                li.append(record)
                i+=1
            y+=1
        return li

    def sort_by_union(self,union_list):
        #nie inkrementujesz plus tu chodzi o len setu a nie
        #inicjalizacja zmiennych odpowiedzialnych za pętle
        n = len(union_list)
        i=0
        while(i<=n-1):
            #zadeklarowanie jako mini elementu o inteksie w którym chce wstawić najmniejszą wartość
            mini = union_list[i]
            indMin = i
            j=i+1
            while(j<n):
                #znajduje najmniejszy element z pozostałej listy
                if (len(union_list[j][2])>len(mini[2])):
                    mini=union_list[j]
                    indMin=j
                j+=1
            
            union_list[indMin] = union_list[i]
            union_list[i] = mini
            i+=1
        return union_list
    def get_used_here(self):
        used = []
        for i in range(3):
            for j in range(3):
                used.append(self.croot[i][j])
        used = set(used)
        return used

app = Sudoku()
app.sudo_tab[0].create_unbound_place()
app.sudo_tab[1].create_unbound_place()
app.sudo_tab[2].create_unbound_place()
app.sudo_tab[4].create_unbound_place()
app.sudo_tab[5].create_unbound_place()
app.sudo_tab[6].create_unbound_place()
app.sudo_tab[7].create_unbound_place()
app.sudo_tab[3].croot[2][0]=3
app.print_full_sudoku()
ret = app.test_backtrack()
