import pandas as pd
import matplotlib.pyplot as pl
df = pd.read_csv("C:\\Users\\asus\\OneDrive\\Documents\\Aditya py file\\IMDB n Rotten tomatoes-All.csv")
print('''Hi there,
Welcome to MSP
We're glad you choose our program for suggestions on movies and TV shows.
''')
k = 'y'
while k == 'y' or k == 'Y' :
    print('''
Following are the genres we can suggest you with :
1. Action
2. Adventure
3. Drama
4. Rom-Com
5. Sci-fi
6. Crime
7. Thriller        and
8. Horror
''' )
    g = int(input("Enter the genre no. you'd like to watch : "))
    print()
    s = eval(input('''Enter the max no. of seasons you want : 
(0 for movies) : '''))
    print()
    i = 1
    if i ==1 :
        if g == 1:
            genre = 'Action'
        elif g == 2 :
            genre = 'Adventure'
        elif g == 3 :
            genre = 'Drama'
        elif g == 4 :
            genre = 'Rom-Com'
        elif g == 5 :
            genre = 'Sci-fi'
        elif g == 6 :
            genre = 'Crime'
        elif g == 7 :
            genre = 'Thriller'
        elif g == 8 :
            genre = 'Horror'
        print()
    if s != 0 :
        print('Here are the top rated', genre, 'TV Shows.')
        df1 = df[df['Genre']==genre]
        df2 = df1[df1['No. of Seasons'] <= s]
        df3 = df2.sort_values('IMDB', ascending = True)
        df4 = df3[['Name', 'IMDB', 'Rotten Tomatoes', 'No. of Seasons']]
        df5 = df4.to_string(index=False)
        print(df5)
        print('''
        
Following are the graph types in which we can compare the results of your query :
Type1 - Line Chart
Type2 - Vertical Bar Graph
Type3 - Horizontal Bar Graph''')
        G = input('Enter the preferred graph type (e.g. Type1) : ')
        if G == 'Type1':
            pl.plot(df4['IMDB'], df4['Name'], marker='d', markersize=10)
            pl.xlabel('IMDB Ratings')
            pl.ylabel('TV Shows')
            pl.title('IMDB Ratings of TV Shows')
            pl.show()
            pl.plot(df4['Rotten Tomatoes'], df4['Name'], marker='d', markersize=10)
            pl.xlabel('Rotten Tomatoes Ratings')
            pl.ylabel('TV Shows')
            pl.title('Rotten Tomatoes Ratings of TV Shows')
            pl.show()
        elif G == 'Type2':
            pl.bar(df4['Name'], df4['IMDB'])
            pl.xlabel('TV Shows')
            pl.ylabel('IMDB Ratings')
            pl.title('IMDB Ratings of TV Shows')
            pl.show()
            pl.bar(df4['Name'], df4['Rotten Tomatoes'])
            pl.xlabel('TV Shows')
            pl.ylabel('Rotten Tomatoes Ratings')
            pl.title('Rotten Tomatoes Ratings of TV Shows')
            pl.show()
        elif G == 'Type3':
            pl.barh(df4['Name'], df4['IMDB'])
            pl.xlabel('IMDB Ratings')
            pl.ylabel('TV Shows')
            pl.title('IMDB Ratings of TV Shows')
            pl.show()
            pl.barh(df4['Name'], df4['Rotten Tomatoes'])
            pl.xlabel('Rotten Tomatoes Ratings')
            pl.ylabel('TV Shows')
            pl.title('Rotten Tomatoes Ratings of TV Shows')
            pl.show()
        else : 
            print('Invalid input!!')
    else :
        print('Here are the top rated', genre, 'Movies.')
        DF1 = df[df['No. of Seasons'].isnull()]
        DF2 = DF1[DF1['Genre']==genre]
        DF3 = DF2.sort_values('IMDB', ascending = True)
        DF4 = DF3[['Name', 'IMDB', 'Rotten Tomatoes']]
        DF5 = DF4.to_string(index=False)
        print(DF5)
        print('''
        
Following are the graph types in which we can compare the results of your query :
Type1 - Line Chart
Type2 - Vertical Bar Graph
Type3 - Horizontal Bar Graph''')
        G = input('Enter the preferred graph type (e.g. Type1) : ')
        if G == 'Type1':
            pl.plot(DF4['IMDB'], DF4['Name'], marker='d', markersize=10)
            pl.xlabel('IMDB Ratings')
            pl.ylabel('Movies')
            pl.title('IMDB Ratings of Movies')
            pl.show()
            pl.plot(DF4['Rotten Tomatoes'], DF4['Name'], marker='d', markersize=10)
            pl.xlabel('Rotten Tomatoes Ratings')
            pl.ylabel('Movies')
            pl.title('Rotten Tomatoes Ratings of Movies')
            pl.show()
        elif G == 'Type2':
            pl.bar(DF4['Name'], DF4['IMDB'])
            pl.xlabel('Movies')
            pl.ylabel('IMDB Ratings')
            pl.title('IMDB Ratings of Movies')
            pl.show()
            pl.bar(DF4['Name'], DF4['Rotten Tomatoes'])
            pl.xlabel('Movies')
            pl.ylabel('Rotten Tomatoes Ratings')
            pl.title('Rotten Tomatoes Ratings of Movies')
            pl.show()
        elif G == 'Type3':
            pl.barh(DF4['Name'], DF4['IMDB'])
            pl.xlabel('IMDB Ratings')
            pl.ylabel('Movies')
            pl.title('IMDB Ratings of Movies')
            pl.show()
            pl.barh(DF4['Name'], DF4['Rotten Tomatoes'])
            pl.xlabel('Rotten Tomatoes Ratings')
            pl.ylabel('Movies')
            pl.title('Rotten Tomatoes Ratings of Movies')
            pl.show()
        else :
            print('Invalid input!!')
    k = input('''Do you wish to use Msp again ???
(press y for yes and any other key for no) ''')
else :
    print() 
    print('Thanks for using our program. We wish you a great time :)') 