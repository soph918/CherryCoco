# 3이나 5의 배수 합 구하기

i = 1
result = 0

while i < 1000 : 
    if i % 3 == 0 or i % 5 == 0:
        result += i
    i += 1

print(result)
