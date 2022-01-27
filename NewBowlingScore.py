score = [[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0]]
score_t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
round = 0
r = 0 
p = r + 1

for r in range (0, 10):
    p = r + 1
    score[r][0] = int(input("%d라운드 1투구 점수는? :" % p))
    if score[r][0] == 10:
        score[r][1] = 0
        score_t[r] = 30
    else:
        score[r][1] = int(input("%d라운드 2투구 점수는? :" % p))
        if score[r][0] + score[r][1] == 10:
            score_t[r] = score[r][0] + 10
        else:
            score_t[r] = score[r][0] + score[r][1]
    
print(score_t)
sum = sum(score_t)
print(sum)
