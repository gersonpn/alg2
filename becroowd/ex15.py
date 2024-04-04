a, b, c = map(int, input().split())


maior_ab = (a + b + abs(a - b)) // 2
maior = (maior_ab + c + abs(maior_ab - c)) // 2


if a > b and a > c:
  print(a,"eh o maior")
elif b > a and b > c:
  print(b,"eh o maior")
else:
  print(c,"eh o maior")

print(maior)