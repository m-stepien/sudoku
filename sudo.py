import random
#walidacja w rzedzie


class Sudoku():
    def __init__(self):
        pass


class Square():

    def __init__(self, unr=[], unc=[]):
        self.croot = self.full_num(use_num_row=unr, use_num_column=unc)

    def full_num(self, use_num_row=[], use_num_column=[]):
        croot = [[0 for x in range(3)] for z in range(3)]
        y = 0
        numbers = [x for x in range(1, 10)]
        if use_num_row or use_num_column:
            li_union=self.create_list_union(use_num_row=use_num_row, use_num_column=use_num_column)
            print(li_union)
            print("_____________________________________")
            li_union=self.sort_by_union(li_union)
            print("________________________")
            print(li_union[0][0],li_union[0][1])
            print("________________________")
            i=0
            used_here=set()
            while(i<len(li_union)):
                numbers = [x for x in range(1, 10)]
                numbers = set(numbers).difference(li_union[i][2])
                numbers = numbers.difference(used_here)
                numbers = list(numbers)
                r = random.randint(0, len(numbers)-1)
                used_here.add(numbers[r])
                print(i)
                croot[li_union[i][0]][li_union[i][1]]=numbers[r]
                i+=1

            
        else:
            while(y < 3):

                i = 0

                while(i < 3):

                    r = random.randint(0, len(numbers)-1)
                    a = numbers.pop(r)
                    croot[y][i] = a
                    i += 1

                y += 1
        return croot

    def print_croot(self):
        # tutaj by wypadalo ladniej wypisywac
        for q in self.croot:
            print(q)

    def give_row(self, ind):
        rw = self.croot[ind]
        return rw

    def give_col(self, ind):
        cl = []
        for x in self.croot:
            cl.append(x[ind])
        return cl

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
            print(mini)
            indMin = i
            j=i+1
            while(j<n):
                #znajduje najmniejszy element z pozostałej listy
                print(i, j)
                if (len(union_list[j][2])<len(mini[2])):
                    mini=union_list[j]
                    indMin=j
                j+=1
            
            union_list[indMin] = union_list[i]
            union_list[i] = mini
            i+=1
        return union_list

p1 = Square()
p5 = Square()
ar_row = []
ar_row.append(p1.give_row(0))
ar_row.append(p1.give_row(1))
ar_row.append(p1.give_row(2))
ar_col=[]
ar_col.append(p5.give_col(0))
ar_col.append(p5.give_col(1))
ar_col.append(p5.give_col(2))
p2 = Square(ar_row, ar_col)

p2.print_croot()
