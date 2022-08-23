def calculation(a,b,c):
    arr= [int(a),int(b),int(c)]
    arr.sort()
    return arr[1]
    
if __name__ == '__main__':
    a, b, c = input("Enter three numbers: ").split()
    median= calculation(a, b, c)
    print(f" median value:{median}")