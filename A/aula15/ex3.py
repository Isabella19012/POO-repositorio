try:
    a= int(input("A = "))
    b=int(input("B = "))
    print(a/b)
except ValueError as erro:
    print(erro)
finally:
    print("OK")
print("fim")