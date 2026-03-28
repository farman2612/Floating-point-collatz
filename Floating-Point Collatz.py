def odd(n):
    return (n * 3) + 1
    
def even(n):
    return n / 2
    
def test_collatz_decimal(n: float):
    original = int(n)       
    final = n - original    # Isolate the decimal part
    
    # Boundary condition: Fraction > 0.5
    if final > 0.5:
        if original % 2 == 0:
            n = odd(n)
        else:
            n = even(n)   
            
    # Boundary condition: Fraction <= 0.5
    else:
        if original % 2 == 0:
           n = even(n) 
        else:
            n = odd(n)
            
    return n          

# Example: Testing the unstable edge case that shoots to infinity
num = 15.5
for i in range(100):
    num = test_collatz_decimal(num)
    print(num)
