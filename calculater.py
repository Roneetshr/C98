def calculate(numb1,numb2):
    numbers = input("This sum will be multiplyed: ")
    ans = 0
    for line in numbers:
        ans = ans + numb1*numb2
    print("The answer is")
    print(ans)

calculate(13,24)
        
