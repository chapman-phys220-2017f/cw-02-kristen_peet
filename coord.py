#!/user/bin/env python3

def coord_for(n, a, b):
    h=(b-a)/n
    for_list = []
    for i in range (n+1):
        list.append(a+i*h)
    return list

def coord_while(n, a, b):
    h=(b-a)/n
    while_list = []
    while ((a+i) <= b):
        while_list.append(a)
        a = a+h
    return while_list

def coord_comp(n, a, b):
    h=(b-a)/n
    comp_list = [(a+(i*h)) for i in range (n+1)]
    return comp_list


if _name_ == "_main_":
    n = (input("interval number: ")
    a = (input("lower bound: ")
    b = (input("upper bound: ")
    for_list = coord_for(n, a, b)
    while_list = coord_while(n, a, b)
    comp_list = coord_comp(n, a, b)
    print("for loop: ", for_list)
    print("while loop: ", while_list)
    print("list comprehension: ", comp_list)
