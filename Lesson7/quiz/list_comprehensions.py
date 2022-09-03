# List Comprehensions

# Write a short Python program that for all numbers x between 0 and 99 prints
# x^3 (x*x*x), but only if x is even and x^3 < 20.
for x in range(100):
    if (x == 0) or (x%2 == 0 and pow(x, 3) < 20):
        print(str(pow(x, 3)),' (',str(x),'*',str(x),'*',str(x),')')