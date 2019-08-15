#coding: utf-8

from src.get_words_list import get_all_words
from src.alphabet import Alpha

excel_path = '/home/tusimple/N2-Japanese-Classify/word/japanese_words.xlsx'

# get all entry from excel
word_list = get_all_words(excel_path)

# build the word table
alpha = Alpha()




