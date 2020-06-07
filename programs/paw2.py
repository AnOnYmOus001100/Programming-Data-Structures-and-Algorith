from math import log

#check if a positive number can be expressed as the sum of threesquares, then return True else False
def threesquares(m):
    start = int(log(m, 4))
    for i in range(start):
        for j in range(m):
            a = (4 ** i) * (8 * j + 7)
            if a == m:
                return False
    return True

#take a string as input and check if any characters is repeating,then return False else True
def repfree(s):
    a = set(s)
    return len(a) == len(s)


#take a list of numbers and check if it is a hill or valley, if so then return True else False
def hillvalley(l):
    if l == []:
        return False
    stop = -1
    i = 1
    found = 1
    if l[0] > l[1]:
        i = 1
        for i in range(i, len(l)):
            if l[i - 1] < l[i]:
                stop = i
                break
        if stop == -1:
            return False
        i = stop
        for i in range(i, len(l)):
            if l[i - 1] > l[i]:
                found = 0
                break
        return bool(found)
    elif l[0] < l[1]:
        for i in range(1, len(l)):
            if l[i - 1] > l[i]:
                stop = i
                break
        if stop == -1:
            return False
        for i in range(i, len(l)):
            if l[i - 1] < l[i]:
                found = 0
        return bool(found)
    else:
        return False
    
#call functions as desired
#check if a positive number can be expressed as the sum of threesquares, then return True else False
def threesquares(m):
    start = int(log(m, 4))
    for i in range(start):
        for j in range(m):
            a = (4 ** i) * (8 * j + 7)
            if a == m:
                return False
    return True

#take a string as input and check if any characters is repeating,then return False else True
def repfree(s):
    a = set(s)
    return len(a) == len(s)


#take a list of numbers and check if it is a hill or valley, if so then return True else False
def hillvalley(l):
    if l == []:
        return False
    stop = -1
    i = 1
    found = 1
    if l[0] > l[1]:
        i = 1
        for i in range(i, len(l)):
            if l[i - 1] < l[i]:
                stop = i
                break
        if stop == -1:
            return False
        i = stop
        for i in range(i, len(l)):
            if l[i - 1] > l[i]:
                found = 0
                break
        return bool(found)
    elif l[0] < l[1]:
        for i in range(1, len(l)):
            if l[i - 1] > l[i]:
                stop = i
                break
        if stop == -1:
            return False
        for i in range(i, len(l)):
            if l[i - 1] < l[i]:
                found = 0
        return bool(found)
    else:
        return False
    
#call functions as desired
#check if a positive number can be expressed as the sum of threesquares, then return True else False
def threesquares(m):
    start = int(log(m, 4))
    for i in range(start):
        for j in range(m):
            a = (4 ** i) * (8 * j + 7)
            if a == m:
                return False
    return True

#take a string as input and check if any characters is repeating,then return False else True
def repfree(s):
    a = set(s)
    return len(a) == len(s)


#take a list of numbers and check if it is a hill or valley, if so then return True else False
def hillvalley(l):
    if l == []:
        return False
    stop = -1
    i = 1
    found = 1
    if l[0] > l[1]:
        i = 1
        for i in range(i, len(l)):
            if l[i - 1] < l[i]:
                stop = i
                break
        if stop == -1:
            return False
        i = stop
        for i in range(i, len(l)):
            if l[i - 1] > l[i]:
                found = 0
                break
        return bool(found)
    elif l[0] < l[1]:
        for i in range(1, len(l)):
            if l[i - 1] > l[i]:
                stop = i
                break
        if stop == -1:
            return False
        for i in range(i, len(l)):
            if l[i - 1] < l[i]:
                found = 0
        return bool(found)
    else:
        return False
    
#call functions as desired
print(threesquares(6))
print(threesquares(143))
print(threesquares(1024))
