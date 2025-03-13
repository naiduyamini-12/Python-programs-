a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
    print("a is the smallest value")
elif b < a and b < c:
    print("b is the smallest value")
elif c < a and c < b:
    print("c is the smallest value")
elif a == b == c:
    print("a,b,c are smaller values")
elif a == b and a < c:
    print("a and b are the smallest values")
elif a == c and a < b:
    print("a and c are the smallest values")
elif b == c and b < a:
    print("b and c are the smallest values")
