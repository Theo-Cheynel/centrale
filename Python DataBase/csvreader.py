import csv

with open('movies.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    i = 0
    l = []
    next(spamreader, None)
    for row in spamreader:
        id = row[0].split(",")[0]
        if row[-1][0] == '(' :
            title = " ". join([row[0].split(",")[1]] + row[1:-1])            
            date = int(row[-1][1:5])
            genres = row[-1].split(",")[1].split("|")
        else :
            title = " ". join([row[0].split(",")[1]] + row[1:-2])            
            date = int(row[-2][1:5])
            genres = row[-1].split(",")[1].split("|")
        i += 1
        l.append({'key':int(id), 'title':title,'date':date, 'genre':genres[0]})
        if int(id) >= 1000:
            break
            
"""
with open('ratings.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    i = 0
    l=[]
    next(spamreader, None)
    for row in spamreader:
        a = int(row[0].split(',')[0])
        b = int(row[0].split(',')[1])
        rating = int(float(row[0].split(',')[2]))
        if b<=1000:
            l.append({'user_rating':a, 'movie_rated':b, 'rating':rating})
        i+= 1
        if i == 100836:
            break
            """
            
for i in l :
    print("        create(key="+str(i['key'])+ ", title= '''"+i['title']+"''', director='', date=" +str(i['date'])+ ", genre='''"+i['genre']+  "''')")
