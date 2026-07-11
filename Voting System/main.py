from collections import Counter


vote_person_list = []
vote_list = {"BJP": 0, "CJP": 0, "CONGRESS": 0}
i = 0


while i < 10:
    name = input("Enter you name :")
    if name in vote_person_list :
        print("YOU have already given the vote")
    else:
        vote = int(input("1.BJP\n2.CJP\n3.CONGRESS\nENTER YOUR VOTE : "))
        if vote == 1:
            vote_list['BJP'] += 1
        if vote == 2:
            vote_list ['CJP'] += 1
        if vote == 3:
            vote_list['CONGRESS'] += 1
        if vote != 3 or vote != 2 or vote != 1:
            print("Enter valid number")
    vote_person_list.append(name)
    i += 1

counts = Counter(vote_list)
winner = counts.most_common(1)

print("\nThe most votes are of:")
for candidate, votes in winner:
    print(f"{candidate} have {votes}")