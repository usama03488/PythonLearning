Student_Score=[100,199,205,80,50,290,120]

highestscore=0
for score in Student_Score:
    if(highestscore<score):
        highestscore=score

print(f"Highest score is {highestscore}")

total=0
for score in range(1,101):
    total +=score

print(f"total score is {total}")