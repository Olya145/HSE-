print("Введите числа a, b, c")
a = int(input())
b = int(input())
c = int(input())
if a % b == c and a / b == c:
    print ("a даёт остаток c при делении на b и a разделить на b равно c")
elif a & b == c and a / b != c:
    print("a даёт остаток c при делении на b, но a разделить на b не равно c")
elif a % b != c and a / b == c :
    print("a не даёт остаток c при делении на b, но a разделить на b равно c")
else:
    print("a не даёт остаток c при делении на b и a разделить на b не равно c")
