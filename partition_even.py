#function to partition a tuple into even and odd
t=(1,2,3,4,5,6,7,8,9,10)
def even(t):
    even_tuple = tuple(x for x in t if x % 2 == 0)
    odd_tuple = tuple(x for x in t if x % 2 != 0)
    print(even_tuple,odd_tuple)
even(t)


        
            