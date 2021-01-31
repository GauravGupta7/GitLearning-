# Naive Algorithm

"""def Fibonucci(n):
    if n<=1:
        return n
    else:
        return Fibonucci(n-1) + Fibonucci(n-2)

n = int(input("Enter the number"))
print(Fibonucci(n-1))"""



# Efficient Algorithm

"""l = [0,1]
n = int(input())

for i in range(2,n):
    l.append(l[i-1] + l[i-2])

print(l[n-1])"""