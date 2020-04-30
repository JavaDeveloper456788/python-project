# o(n) method uses the array values as indices by subtracting the minimum value from each array value.
# for each value in visited index, the value is multiplied by -1. If we encounter a previously encoutered element its index value sign would be negative
# also if we encounter an index value with positive sign that index value is missinh
# space complexity - o(n)
# time complexity - o(n)
# advantages - fast in execution
# disadvantages -uses extra space or requires original array modification.
def get_tuple_n(arr):
    l = arr.copy()
    m1 = min(l)
    m2 = max(l)
    for i in range(len(l)): 
        if l[abs(l[i])-m1] > 0: 
            l[abs(l[i])-m1] = -l[abs(l[i])-m1] 
        else: 
            repeat = abs(l[i])
              
    for i in range(len(l)): 
        if l[i]>0: 
            missing = i+m1
    return (missing, repeat)


# we sort the original list and iterate through the eorted list.
#If an element is not +1 of prev element then that is the missing number
# if element is same as prev element then that is the repeat number
# space complexity - o(n)
# time complexity - o(nlogn)
# advantages - easy to write and understand code
# disadvantages - higher time complexity and uses extra space or requires modification of original array
def get_tuple_nlogn(l):
    m1 = min(l)
    m2 = max(l)
    ls = sorted(l)
    flag = False
    for i in range(len(l)):
        if i+m1 != ls[i] and not flag:
            missing = i+m1
            flag = True
        if i>0 and ls[i]==ls[i-1]:
            repeat = ls[i]
    return(missing, repeat)


# starting from the minimum number and checking incrementally we check for each number in the list. If umber is not found it is missing
# to find repeat element we check for each element if it i present in an index after that element.
# time coplexity - o(n^2)
# space complexity - o(1)
# advantages - does not modify the array, does not use extra space
# disadvantages - high time complexity
def get_tuple_n2(l):
    m1 = min(l)
    m2 = max(l)
    length = len(l)
    for i in range(length):
        tmp = m1+i
        found = False
        for j in range(length):
            if l[j]==tmp:
                found = True
                break
        if not found:
            missing = tmp
    for i in range(length):
        tmp = l[i]
        for j in range(i+1, length):
            if l[j] == tmp:
                repeat = tmp
                break
    return (missing, repeat)