with open("text-file-analyse.txt",'r') as file: 
    data = file.read()

x = data.split()
print(x)

word_dict = {}

for i in x:
    word_count = x.count(i)
    word_dict[i] = word_count

print(word_dict)

counts = list(word_dict.values())
max = counts
counts.sort(reverse=True)

for word in word_dict:
    if word_dict[word] == counts[0]:
        common_word = word
        print(f"The most common word is : {common_word} ")