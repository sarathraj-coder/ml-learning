base = 10
height = 2
area = 1 / 2 * (base * height)
print("Area of triangle is ", area)

if area > 10:
    print("Area is larger than 10")
elif area < 10:
    print("area is less than 10")
else:
    print("area is 10")

input: str = input("Enter a number")
print(input)


x = [1, 2, 3, 4, 5]
def sum(x):
    sum = 0
    for a in x:
        sum = sum + a
    print(sum)
    return sum

print(sum(x))

d = {"n":1,"p":3}
print(d["n"])
d["i"]=99
print(d)
del d["n"]
print(d)


