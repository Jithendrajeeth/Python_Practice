n= 15
temp = n
power = len(str(n))
tot= 0
while n > 0:
    digit = n %10
    tot += digit**power
    n//=10

if tot == temp:
    print("armstrong")
else:
    print("not armstrong")