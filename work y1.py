


def functiona(m,x,b):
    """
        this function use for create number
    """

    # this is comment2
    return m*x+b

class ClassA(object):
    """
        description
    """
    def __init__(self):
        print("this is constructor")

if __name__ == '__main__':
    #! user / 600510577
    f=(float)(input("input temperature in fahrenheit: "))
    c=5*(f-32)/9
    print(f , "degree fahrenheit is ",c,"degree celsius ")

    y = functiona(10,10,0)
    print(y)
    print(functiona(10,10,0))
