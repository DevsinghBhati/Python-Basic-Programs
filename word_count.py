word = 0
vowel = 0
char = 0
consonants = 0
upperletter = 0
lowerletter = 0

text = input("Enter a word: ")

wordlist = text.split()

vowellist = [ 'A' , 'E' , 'I' , 'O' , 'U', 'a' , 'e' , 'i' , 'o' , 'U']

for i in text:
    if( i != ' '):
        if(i in vowellist):
            vowel += 1
        if( i == i.upper()):
            upperletter += 1
        if( i == i.lower()):
            lowerletter += 1
        char += 1

consonants = char - vowel
word = len(wordlist)

print("Words : ",word)
print("Vowel : ",vowel)
print("Characters : ",char)
print("Total capital latters : " , upperletter)
print("Total small latters : " , lowerletter)
print("Total constonants are : ",consonants)
