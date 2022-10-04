import csv
'''
Our task was to separate the rows where email and phone number
is matched with another google sheet with their mode of participation. As I was in hurry
and had tried multiple times, I couldn't find the way to do
the same using google sheet itself, hence I decided to download
the sheets into csv and then manipulate the files using python
and then upload the csv back to google sheets
'''

root = []

email_ph = '''
Here we had emails and phone nos
of participants separated by tab

For obvious reasons I had to hide those
'''.split('\n')

x=[]
for i in email_ph:
    x.append(i.split("\t"))
email_ph = x

dictionary = {}

for i in email_ph[:-1]:
    dictionary[i[0]] = i[1]


with open("./Downloads/Mode of Participation - Sheet8.csv") as csvfile:
    rows = csv.reader(csvfile, delimiter=",")
    for row in rows:
        root.append(row)

final = []
for i in root:
    if i[4] in dictionary:
        i+=[dictionary[i[4]]]


with open('final.csv', "w", newline="") as csvfile:
    file = csv.writer(csvfile, delimiter=",")
    for i in root:
        file.writerow(i)
