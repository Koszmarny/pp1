film_titles = ['shrek 1', 'shrek 2','shrek 3','shrek 4']
file = open('07-FileHandling/films.txt','a')
for i in film_titles:
    file.write(i+'\n')
file.close