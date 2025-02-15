def calculate_love_score(name1, name2):
    name1=(name1.upper()+name2.upper())
   # print(name1)

    first_name="TRUE"
    second_name="LOVE"
    score1=0
    score2=0
    for i in range(len(name1)):
        for x in range(len(first_name)):
            if(first_name[x]==name1[i]):
                score1 +=1
        for x in range(len(second_name)):
            if(second_name[x]==name1[i]):
                score2 +=1

    score= str(score1)+str(score2)
    print(score)
    #print(f"your love score is {score}")

calculate_love_score("Kanye West", "Kim Kardashian")
#calculate_love_score("usama","Ayesha")
