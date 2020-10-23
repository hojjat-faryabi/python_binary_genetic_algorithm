def binArrayToInt(arr):
    temp = ''
    for i in arr:
        temp += str(i)
    return(int(temp, 2))