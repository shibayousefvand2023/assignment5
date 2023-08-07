num_Even = '*'
num_Odd = '#'


def Raster_function (row , col):
    for i in range (row):
        for j in range (col):
            if i == 0:
                print(num_Even , end="")
            else:
                print(num_Odd , end="")



n = int(input('row_num:'))
m = int(input('col_num:'))
print(n*m)
Raster_function(n , m)

