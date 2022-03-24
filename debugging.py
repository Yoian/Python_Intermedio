# def divisors(num):
#     divisores=[]
#     for i in range(1, num + 1):
#         if num % 1 == 1:
#             divisores.append(i)

#     #divisors = [i for i in range (1, num + 1) if num % 1 == 1]

#     return divisores
def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors

def run():
    num = int(input("Ingresa un número: "))
    print(divisors(num))
    print("Terminó mi programa")


if __name__ == "__main__":
    run()