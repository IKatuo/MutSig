import re
import pandas as pd
df=pd.read_excel('/Users/sunyuqi/Desktop/病理科/ruijinbingli/key.xls')
filtered_df=df['病理诊断']
key_col=[]
for i in filtered_df:
    i=re.findall('“(.*?)”',i)
    str_all = ','.join(i)
    key_col.append(str_all)
key=pd.DataFrame(key_col,columns=['key'])
print(key)
key.to_csv('/Users/sunyuqi/Desktop/病理科/ruijinbingli/key.txt', sep='\t',index=False, header = True)
