import math

while True:
    a = float(input("Input side A: "))
    b = float(input("Input side B: "))
    c = float(input("Input side C: "))

    if a <= 0 or b <= 0 or c <= 0 or (a+b<=c) or (b+c<=a) or (c+a<=b):
        print("Invalid input")
        break

    if a == b == c:
        print("Equilateral Triangle")
    elif a==b or b==c or a==c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
    
    s = (a + b + c) / 2
    area = math.sqrt(s*((s-a)*(s-b)*(s-c)))
    print(f'Identify the type: {area}')