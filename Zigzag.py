def zigzag(n):
    temp = []
    result = []
    while n:
        temp.append(n[0])
        for i in xrange(len(a)):
            try:
                if (n[i] > n[i + 1] and n[i] > n[abs(i - 1)]) or \
                        (n[i] < n[i + 1] and n[i] < n[abs(i - 1)]):
                    temp.append(n[i + 1])
                else:
                    break
            except IndexError:
                pass
        if len(result) <= len(temp):
            result = temp
        n.pop(0)
        temp = []
    return result
         

print zigzag([1,9,4,7,2,0,1,2,9])
