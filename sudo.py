import random
#walidacja w rzedzie
"""
zmiana 3 na zmienne
napisanie backtrackingu
zamiana sortowania na quicksort
napisanie testow jednostkowych
powtorka goscia prof
dokonczenie rozdzialu goscia prof
"""

class Sudoku():
    def __init__(self):
        #nie lista tabelek zer tylko lista klasy Square która będzie miala domyślnie ustawionego taba z 0
        self.sudo_tab = [Square() for x in range(9)]

    def get_used_in_column(self, n \
        ):
        # n to macierz trzeba iterować po jej szerokości
        list_used_set = []
        for j in range(3):
            used_set = set()
            for i in [1,4,7]:
                for k in range(3):
                    used_set.add(self.sudo_tab[i].croot[k][j])
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
    

    def test_backtrack(self, sbu, i, used_here):

        if i==9:
            return True
        numbers = [x for x in range(1, 10)]
        numbers = set(numbers).difference(sbu[i][2])
        if used_here:
            s=set(used_here)
            numbers = numbers.difference(s)
        numbers = list(numbers)
        if len(numbers)==0:
            print("zwracam fałsz")
            return False
        
        
        for x in numbers:
            self.sudo_tab[1].croot[sbu[i][0]][sbu[i][1]] = x
            print(i, x)
            i+=1
            used_here.append(x)
            return self.test_backtrack(sbu, i, used_here)





class Square():

    def __init__(self, unr=[], unc=[]):
        self.croot = [[0 for x in range(3)] for z in range(3)]

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



    # def sort_by_union(self,union_list):
    #     #nie inkrementujesz plus tu chodzi o len setu a nie
    #     #inicjalizacja zmiennych odpowiedzialnych za pętle
    #     n = len(union_list)
    #     i=0
    #     while(i<=n-1):
    #         #zadeklarowanie jako mini elementu o inteksie w którym chce wstawić najmniejszą wartość
    #         mini = union_list[i]
    #         indMin = i
    #         j=i+1
    #         while(j<n):
    #             #znajduje najmniejszy element z pozostałej listy
    #             if (len(union_list[j][2])<len(mini[2])):
    #                 mini=union_list[j]
    #                 indMin=j
    #             j+=1
            
    #         union_list[indMin] = union_list[i]
    #         union_list[i] = mini
    #         i+=1
    #     return union_list


         

app = Sudoku()
app.sudo_tab[0].create_unbound_place()
app.sudo_tab[4].create_unbound_place()
a = app.get_used_in_row(0)
b = app.get_used_in_column(1)
lisa = app.sudo_tab[1].create_list_union(a, b)
lisa = app.sudo_tab[1].sort_by_union(lisa)
s = []
app.test_backtrack(lisa, 0, s)
app.print_full_sudoku()
