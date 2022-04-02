if __name__ == '__main__':
    x = int(input('enter:'))
    y = int(input('enter:'))
    z = int(input('enter:'))
    n = int(input('enter:'))
    result = []
    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if i + j + k != n:
                    result.append([i , j, k])
    print(result)
                    
                    