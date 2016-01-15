def zigzag(n):
    result = []
    prevEle = -1
    started = False
    prevRise = False
    for ele in n:
        if len(result) == 0 and started:
                if ele < prevEle:
                    result.append(0)
        if started:    
            if ele > prevEle:
                if prevRise:
                    result[len(result)-1] = result[len(result)-1] + 1
                else:
                    result.append(1)
                prevRise = True    
            else:
                if prevRise:
                    result.append(1)
                else:
                    if len(result) == 1:
                        result.append(1)
                    else:
                        result[len(result)-1] = result[len(result)-1] + 1
                prevRise = False    

        prevEle = ele
        started = True;
    return result
         

print zigzag([1,9,4,7,2,0,1,2,9])
