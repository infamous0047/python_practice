# Swap function
def swap():
    a = 50
    b = 60
    # temp = b
    # b = a
    # a = temp
    a = a + b
    b = a - b
    a = a - b
    # a, b = b, a
    print(b, a)

swap()
