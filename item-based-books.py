import pandas as pd
ratings=pd.read_csv('dataset/ratings.csv')
ratings.head()
books=pd.read_csv('dataset/books.csv',usecols=["book_id","goodreads_book_id","title"])
books.head()
ratings=pd.merge(books,ratings)
ratings.head()
userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
userRatings.head()