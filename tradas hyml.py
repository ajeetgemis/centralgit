import pandas as pd
file_path="D:\\tata_nrw\\TCF_Drop_Data.xls"
with open(file_path,'r') as file:
    f1=file.read()
    pd1=pd.read_html(f1)
    print(pd1)
    
    
    
    #f1.splitlines
    
    #f2=f1.replace('</tr><tr>','')
    #f3=f2.replace('<td class="text">','')
    #f4=f3.replace('</td>',',')
    #f4=f4.replace('<td>','')
    #print(f4)
    
   
