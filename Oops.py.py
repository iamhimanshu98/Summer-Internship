# Object Oriented Programming
# Some basic operations on list using multiple methods

class Num :
    def __init__ (self) :
        self.random_number = [52, 14, 25, 36, 96, 85, 74, 47, 58, 69, 25, 6, 45, 63, 67, 81, 9, 1, 7, 1, 2, 13, 1, 45, 44]
    
    def even_odd_counter(self) :
        print ("Even numbers: ", end="")
        count=0
        for i in self.random_number :
            if i%2 == 0 :
                print(i, "", end="")
                count+=1
        print("Total even numbers: ",count)

        print ("Odd numbers: ", end="")
        count=0
        for i in self.random_number :
            if i%2 != 0 :
                print(i, "", end="")
                count+=1
        print("Total odd numbers: ",count)

    def avg_finder(self):
        _sum = 0
        num = self.random_number
        count = 0
        for i in num :
            _sum += i
            count += 1
        print("average :",round(_sum/count,2))

    def num_finder(self, n) :
        for i,j in enumerate(self.random_number) :
            if (j == n) :
                print("Item is present at index:", i)

obj = Num()
obj.even_odd_counter()
obj.avg_finder()
obj.num_finder(n=14)
