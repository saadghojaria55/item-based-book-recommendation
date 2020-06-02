# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:04:04 2020

@author: LENOVO
"""

import pandas as pd

books=pd.read_csv('dataset/books.csv',usecols=['book_id','goodreads_book_id','title'],dtype={'book_id': 'int32','goodreads_book_id':'int32', 'title': 'str'})
ratings=pd.read_csv('dataset/ratings.csv',usecols=['user_id', 'book_id', 'rating'],dtype={'user_id': 'int32', 'book_id': 'int32', 'rating': 'int32'})


from scipy.sparse import csr_matrix
# pivot ratings into movie features
df_book_features = ratings.pivot(
    index='book_id',
    columns='user_id',
    values='rating'
).fillna(0)
# convert dataframe of movie features to scipy sparse matrix
mat_book_features = csr_matrix(df_book_features.values)