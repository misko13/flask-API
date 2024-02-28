def divide(dividend, divisor) -> float:
    if divisor == 0:
        print("Divide by 0!")
        return
    
    return(dividend / divisor)


grades = [44,55,66,77,88]

print("Wellcome to the avarage grade program")

average = divide(sum(grades) , len(grades))

print(f"The anerage grade is {average}. ")