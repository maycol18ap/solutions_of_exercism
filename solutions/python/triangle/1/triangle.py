def equilateral(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    if (a==0) and (b==0) and (c==0):
        return False
    if(a==b) and (b==c) and (c==a):
        return True
    elif(a==0) and (b==0) and (c==0):
        return False
    else:
        return False


def isosceles(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    is_valid = (a + b >= c) and (b + c >= a) and (a + c >= b)
    all_positive = (a > 0) and (b > 0) and (c > 0)
    
    if not (is_valid and all_positive):
        return False
    
    return (a == b) or (b == c) or (a == c)

def scalene(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    if not (a + b >= c and b + c >= a and a + c >= b and a > 0):
        return False
    
    return a != b and b != c and a != c
        
