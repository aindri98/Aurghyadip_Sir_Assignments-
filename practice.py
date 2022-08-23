def function4(**myArgs):
    print(myArgs)
    print(myArgs["fname"] + " " + myArgs["lname"])
    print(myArgs["state"])

function4(fname = 'Aurghyadip', lname = "Kundu", state = 'WB', district = 'Kolkata')

def function3(fname, lname):
    print(fname + " " + lname)
function3(lname = "Kundu", fname = "Aurghyadip")
def checkPrime(num):
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                return False
    elif num < 1:
        return False
    return True

def nextPrime(num):
    n = num + 1
    while True:
        if checkPrime(n):
            return n
        else:
            n += 1


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    next_prime = nextPrime(n)
    print(f"Next prime number is : {next_prime}")