#coding: utf-8
import pandas as pd
from tqdm import tqdm

# After finish the classify, output this entry to a excel
def get_frame(alpha):
    df = pd.DataFrame(columns=['假名', '日文', '意思', '类型'])
    print("---Start generating dataframe---')
    for i, j in tqdm(vars(alpha).items()):
        name = list(j)[0]
        entry_list = list(j.values())[0]
        # 添加标识字段
        df = df.append({'假名': name, '日文': '', '意思': '', '类型': ''}, ignore_index=True)
        for entry in entry_list:
            japanese_words = entry['日文']
            kana = entry['假名']
            chinese = entry['意思']
            wordType = entry['类型']

            # 判断是否有类型
            if isinstance(wordType, str) and wordType != '专有词':
                df = df.append({'假名': kana, '日文': japanese_words, '意思': chinese, '类型': wordType}, ignore_index=True)
            elif isinstance(wordType, str) is False:
                df = df.append({'假名': kana, '日文': japanese_words, '意思': chinese, '类型': ''}, ignore_index=True)

        df = df.append({'假名': '', '日文': '', '意思': '', '类型': ''}, ignore_index=True)
    print('---Generating dataframe Finish---')
    return df