a= int(input("Введите сторону а: "))
b= int(input("Введите сторону b: "))
c= int(input("Введите сторону c: "))
if a==b and a==c:
    print("Треугольник равносторонний")
elif a==b or a==c or b==c:
    print("Треугольник равнобедренный")
else:
    print("Треугольник разносторонний")