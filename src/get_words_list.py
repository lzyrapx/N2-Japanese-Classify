#coding: utf-8

import pandas as pd
from tqdm import tqdm
import logging

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# get all entry from excel, and add it to a list
def get_all_words(excel_path):
    pd_frame = pd.read_excel(excel_path)
    word_list = []
    logger.info("....Get all entry from excel. Running...")
    for i in tqdm(range(len(pd_frame))):
        word_dict = {}
        japanese_words = pd_frame.iloc[i]["日文"]
        kana = pd_frame.iloc[i]["假名"]
        pronunciation = pd_frame.iloc[i]["发音"]
        chinese = pd_frame.iloc[i]["中文"]
        wordType = pd_frame.iloc[i]["类型"]
        
        # excel 有效行
        if isinstance(kana, float) == False:
            word_dict["日文"] = japanese_words
            word_dict["假名"] = kana
            word_dict["发音"] = pronunciation
            word_dict["中文"] = chinese
            word_dict["类型"] = wordType
            word_list.append(word_dict)
    
    logger.info("....Get all entry from excel. Finish...")
    return word_list

if __name__ == "__main__":
    excel_path = "/home/tusimple/N2-Japanese-Classify/word/japanese_words.xlsx"
    ans = get_all_words(excel_path)





        