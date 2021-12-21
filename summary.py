from bs4 import BeautifulSoup
import re
filename = "D:/Programing and Tech/Python/Projects/Programming Based/Wow Labz/assignment.html"

def clean(text):
    text = str(text)
    text = re.sub(r'^https?:\/\/.*[\r\n]*', ' ', text, flags=re.MULTILINE)
    text = re.sub(r'[\w\.-]+@[\w\.-]+', ' ', text, flags=re.MULTILINE)

    # Diwali Cleaning
    text = re.sub(r"\[[0-9]*\]", "", text)
    #text = text.replace('[','')
    #text = text.replace(']','')
    text = text.replace('\u200b',' ')
    text = re.sub('<.*?>+','',text) #remove everything inside <> brackets
    #text = re.sub('–',' ',text) #Remove – from text
    text = re.sub(r"^\s+","",text) #Remove random space from the start and end of text
    text = re.sub(r"\s+[a-zA-Z]\s+"," ", text) #Remove random characters
    text = re.sub(r"\s+",' ',text) #Remove random spaces from text
    return text

with open(filename, encoding='utf8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')  

#Infobox 
vcard = soup.find_all('table',re.compile('infobox'))
th = vcard[0].find_all('th')
td = vcard[0].find_all('td')

data = []
for ele1,ele2 in zip(th,td):
    data.append((clean(ele1),clean(ele2)))

#Summary
summ = soup.find_all('p')[:3]
summ = [str(i) for i in summ[1:]]
summ = ' '.join(summ)
summ = clean(summ)

# Display the outputs
print('Printing Summary:- \n')
print(summ)
print('\nPrinting Information:-')
for a,b in data:
    print(a,':\t',b)
