# Floating-point-collatz
A continuous-domain Python simulation and boundary analysis of the 3x+1 Collatz Conjecture.


# Floating-Point Collatz: Exploding the 3x+1 Problem 💥

Most people look at the famous Collatz Conjecture (the $3x+1$ problem) strictly through the lens of pure mathematics using whole positive integers. 

I wanted to look at it differently: **What happens if we treat it like a state machine and feed it floating-point decimals?** I built a custom continuous-domain extension of the Collatz rules to see if decimals would still collapse into the famous 4-2-1 loop. After running the simulations, I mapped out the system's attractors and found some wild edge cases where the numbers literally explode to infinity.

## ⚙️ The Rules: Decimal Parity Rounding
To make the discrete $3x+1$ math work with continuous decimals, I wrote an algorithm with a strict boundary threshold at `0.5`. 

To find the "state" of a decimal number:
1. If the fractional part is **$> 0.5$**, round up to the nearest integer.
2. If the fractional part is **$\le 0.5$**, round down to the nearest integer.
3. 16.2 here .2 is less than .5 so we consider 16.2 as **EVEN**
4. 16.8 here .8 is greater than .5 so we consider 16.8 as **ODD**
5. 15.2 here .2 is less than .5 so we consider 15.2 as **ODD**
6. 15.8 here .8 is greater than .5 so we consider 15.8 as **EVEN**
   

Once we have that reference integer, we check its parity. 
* If Even $\rightarrow$ Divide the *original* decimal number by 2.
* If Odd $\rightarrow$ Multiply the *original* decimal number by 3, and add 1.

## 🚀 The Discoveries (Basins of Attraction)

By letting this run through a Python simulation, I found that every number falls into one of three distinct categories:

### 1. The Ghost Loop (Stable Attractor)
For almost all standard decimals (like `10.2`, `25.7`, or even `3.14`), the algorithm eventually drags the number into a floating-point version of the original 4-2-1 loop. Because of how the math stretches and compresses the fractions, the system hovers endlessly around `3.999...` $\rightarrow$ `1.999...` $\rightarrow$ `0.999...`

### 2. The Zero Sinkhole
If you input a pure decimal less than or equal to `0.5` (like `0.25`), it rounds down to 0 (Even). It divides by 2, becoming `0.125`, which also rounds to 0. It gets trapped in a permanent halving loop, shrinking infinitely down to zero. 

### 3. Divergence to Infinity (The Edge Case)
This is the most interesting find. I noticed that if a number sits perfectly on the `.5` knife-edge, the system breaks. 

**I mathematically proved that any odd number ending in exactly `.5` (like `15.5` or `7.5`) will explode to infinity.** Because an `Odd.5` number can be written algebraically as $2k + 1.5$, applying the $3x+1$ rule results in $6k + 5.5$. The output is *always* another `Odd.5` number. It never hits an even state to trigger a division, meaning it grows exponentially forever. 

## 💻 The Simulation Code
Here is the core Python logic used to test these boundary conditions. Note the algorithmic optimization: if the decimal is $> 0.5$, rounding up naturally flips the parity, so the code simply swaps the function calls to save compute time!

```python
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
```

## 🧠 Why I Built This
I'm Farman, a 4th-semester undergrad specializing in AI and robotics software engineering. 

When you train neural networks or design control loops for autonomous systems, the most dangerous bugs hide in the boundary conditions—a learning rate off by a micro-fraction can cause weights to explode to infinity or vanish to zero. I built this Floating-Point Collatz simulation to practice mapping system attractors, identifying unstable equilibrium points, and mathematically proving boundary logic. 

Feel free to clone the repo, run the script, and try to find new fractional orbits!
