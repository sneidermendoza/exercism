def square(number):        
    assert 1 <= number <= 64, ("square must be between 1 and 64")

    a = 1
    for i in range(1,number):
        a = a + a
    return a
ValueError("square must be between 1 and 64") 

print(square(-1))
print("a")



