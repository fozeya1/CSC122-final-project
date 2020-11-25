def concat_even(n):
    even_number = [str(i) for i in n if i % 2 == 0]
    return ''.join(even_number)
print(concat_even([1,2,3,4,5,6])) 