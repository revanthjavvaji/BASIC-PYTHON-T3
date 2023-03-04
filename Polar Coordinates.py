# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

z = complex(input())

r = abs(z)
phi = cmath.phase(z)

print(round(r, 3))
print(round(phi, 3))
