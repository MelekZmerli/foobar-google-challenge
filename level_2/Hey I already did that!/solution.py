def getSortedID(n,l):
    temp = [i for i in str(n)]
    if l == 'x':
        temp.sort(reverse=True)
    else:
        temp.sort()
    return ''.join(temp)

def getZ(x,y,b):
    Z = 0
    x = int(x)

    # To store carry generated
    carry = 0
    # To keep track of power
    power = 1
 
    while (int(x) > 0) : # Substraction in base b
        n1 = x % 10
        n2 = int(y) % 10
        x = x // 10
        y = int(y) // 10
 
        temp = n1 - n2 + carry
 
        if (temp < 0) :
            carry = -1
            temp += b
 
        else :
            carry = 0
 
        Z += temp * power
        power = power * 10
 
    # Add 0s if length changed
    n = len(str(x)) - len(str(Z))
    Z = '0'*n + str(Z)
    return Z

def already_did(z,b,cycle):
    if z not in cycle:
        cycle.append(z)
        x = getSortedID(z,'x')
        y = getSortedID(z,'y')
        new_z = getZ(x,y,b)
        if new_z == z:
            return 1
        return already_did(new_z,b,cycle)
    return len(cycle) - cycle.index(z)



def solution(n,b):
    #Your code here
    cycle = []
    result = already_did(n,b,cycle)
    print(result)
