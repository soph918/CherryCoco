score = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0, 0]]
score_t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range (0, 10):
    p = i + 1
    if p < 10:
        score[i][0] = int(input("%d 라운드 첫번째 투구 점수는? " % p))
        if score[i][0] == 10:
            score[i][1] = 0
        else:
            score[i][1]= int(input("%d 라운드 두번째 투구 점수는? " % p))
    else:
        score[i][0] = int(input("%d 라운드 첫번째 투구 점수는? " % p))
        if score[i][0] == 10:
            score[i][1]= int(input("%d 라운드 두번째 투구 점수는? " % p))
            if score[i][1] == 10:
                score[i][2] = int(input("%d 라운드 세번쨰 투구 점수는? " % p))
            else:
                continue
        else:
            score[i][1]= int(input("%d 라운드 두번째 투구 점수는? " % p))
            score[i][2]= 0

for j in range (0, 10):
    k = j + 1
    l = j + 2
    if j < 8:
        if score[j][0] == 10 and score[k][0] == 10:
            score_t[j] = score[j][0] + score[k][0] + score[l][0]
        elif score[j][0] == 10:
            score_t[j] = score[j][0] + score[k][0] + score[k][1]
        elif score[j][0] + score[j][1] == 10:
            score_t[j] = score[j][0] + score[j][1] + score[k][0]
        else: 
            score_t[j] = score[j][0] + score[j][1]
    elif j == 8:
        if score[j][0] == 10:
            score_t[j] = score[j][0] + score[k][0] + score[k][1]
        elif score[j][0] + score[j][1] == 10:
            score_t[j] = score[j][0] + score[j][1] + score[k][0]
        else: 
            score_t[j] = score[j][0] + score[j][1]       
    else:
        score_t[j] = score[j][0] + score[j][1] + score[j][2]

print(score_t)
sum = sum(score_t)
print(sum)
