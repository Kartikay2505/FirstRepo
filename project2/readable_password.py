import random
from types import WrapperDescriptorType
wordlist=[]
spl_char =["@","!","#","$","%","^","&","*"]
with open("wikipedia.txt",'r') as file:
    data=file.readlines()
    for line in data :
        words=line.split()
        for item in words:
            if len(words) > 5 :
                wordlist.append(item.capitalize())
                
word=random.choice(wordlist)
splc=random.choice(spl_char)
num=str(random.randint(10,99))

password= word + splc + num
print(password)
                
             