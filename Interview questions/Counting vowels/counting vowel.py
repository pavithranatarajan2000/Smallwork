a=input() 
a=a.upper()
vowel=0
consonant=0
for i in a:
  if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
    vowel=vowel+1
  elif(i>'A' and i<='Z'):
    consonant+=1
print("Number of vowels in the string is ",vowel)
print("Number of consonants in the string is ",consonant)


