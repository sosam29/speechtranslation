import pandas as pd
import numpy as np
df_kjv= pd.read_csv(r'~/Downloads/t_kjv.csv', usecols=['Book','Chapter','Verse','Text'])

df_hindi= pd.read_csv(r'~/Downloads/Hindi_bible_with_authors.csv', usecols=['Book','Chapter','Verse','Text'])
df_hindi[['Book','Chapter','Verse']]+=1
new_df = pd.merge(df_kjv, df_hindi,  how='left', left_on=['Book','Chapter','Verse'], right_on = ['Book','Chapter','Verse'])
# print(new_df.head())
new_df.to_csv('combined_kjv_hindi.csv', sep='\t', index=False)
