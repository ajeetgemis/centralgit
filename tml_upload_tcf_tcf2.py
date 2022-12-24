import pandas as pd
import mysql.connector as connector
from sqlalchemy import create_engine
from tkinter import Tk
from tkinter import *
import glob,os,shutil
import time


class tata_trolley:
    def __init__(self,root):
        file_path="D:\\tata_nrw\\"
        move_path="D:\\tata_nrw\\New folder"
        
        engine=create_engine('mysql+pymysql://root:redhat@localhost/tata_sequence_upload')
        conn=connector.connect(host='localhost',port='3306',database='tata_sequence_upload',user='root',password='redhat')
        for file_path in glob.glob(file_path+'/*.xls',recursive=False):
            #with open(file_path,'r')as file:
             #   htmlread=file.read()
                #print(htmlread)
              #  pd1=pd.read_html(htmlread,header=0)
               # df=pd.DataFrame(pd1[0])
            df=pd.DataFrame(pd.read_html(file_path)[0])
            df.columns=df.iloc[0]
           # df=df[1:]
            print(df.columns)
            df_newcolumn=[]
            for c in df.columns:
                df_newcolumn.append(c.replace(' ','_'))
            #print(df_newcolumn)
            df.columns=df_newcolumn
            print(df.columns)
            temp_table_name='temp_'+os.path.basename(file_path).split('_')[0].lower()
            main_table_name='tata_'+os.path.basename(file_path).split('_')[0].lower()
            print(temp_table_name)
            df.to_sql(con=engine,name=temp_table_name,if_exists='append',index=False)
            cur=conn.cursor()
            query="INSERT IGNORE  INTO {} (vin_number,biw_number,vehicle_code,vin_date,vin_time) SELECT VIN_NUMBER,BIW_NUMBER,VEHICLE_CODE,VIN_DATE,VIN_TIME FROM {}".format(main_table_name,temp_table_name)
            cur.execute(query)
            conn.commit()
            query="truncate table {}".format(temp_table_name)
            #query="select vin_number,blw_number,vehicle_code,vehicle_description,vin_date,vin_time from blw_temp"
            cur.execute(query)
            conn.commit()

            query="select COUNT(*)  from tata_tcf1 where trolley_number IS NULL"
            cur.execute(query)
            result=cur.fetchone()
            print(type(result[0]))
           # print(result)
            while result[0] >8:
                query="SELECT * FROM tata_tcf1  where trolley_number is null ORDER BY CONCAT (vin_date,vin_time) ASC LIMIT 8"
                cur.execute(query)
                result=cur.fetchall()
                #list1=[]
                list1=list(result)
                print(type(list1))
                #list1.append(result)
                print(len(list1))
                trnum=102
                for item in range(len(list1)):
                   print(list1[item+1][0])
                   time.sleep(3)
                   query="update tata_tcf1 set trolley_number=%s where vin_number=%s"
                   values=(trnum,list1[item+1][0])
                   cur.execute(query,values)
                   conn.commit()
                   
                  
                    
                
                continue
           # shutil.move(file_path,os.path.join(move_path))
           
       
            
            
            
                

            
            #continue
                
"""
            exit()    
            df=pd.DataFrame(pd1[0])
            #df.columns = DF.iloc[0]
            df.rename({'SRNO':'SR_NO','VIN NUMBER':'VIN_NUMBER','BIW NUMBER':'BIW_NUMBER','VEHICLE CODE':'VEHICLE_CODE','VEHICLE DESCRIPTION':'VEHICLE_DESCRIPTION','VIN DATE':'VIN_DATE','VIN TIME':'VIN_TIME'},inplace=True,axis=1)
            df.to_sql(con=engine,name='blw',if_exists='append',index=False)
            readdata=pd.read_sql('blw',engine)
            print(readdata)
            #csv=df.to_csv(header=False,index=False)
            #print(csv)
            cur=conn.cursor()
            query="INSERT IGNORE  INTO main_blw (vin_number,biw_number,vehicle_code,part_description,vin_date,vin_time) SELECT VIN_NUMBER,BIW_NUMBER,VEHICLE_CODE,VEHICLE_DESCRIPTION,VIN_DATE,VIN_TIME FROM blw"
            cur.execute(query)
            conn.commit()
            query="truncate table blw"
            #query="select vin_number,blw_number,vehicle_code,vehicle_description,vin_date,vin_time from blw_temp"
            cur.execute(query)
            conn.commit()
            #result=cur.fetchall()
            #print(result)
            self.root=root
            self.root.geometry('600x400+100+100')
            self.root.title('Tata SCAn')

            def fun1():
                fgscanframe=Toplevel(self.root)
                fgscanframe.geometry('800x800+100+100')
                fgscanframe.title('Tata SCAn')
                
                
            menubar=Menu(self.root)        
           # menubar.add_cascade(label="FI",menu=menubar)    
            file=Menu(menubar,tearoff=0)
            production=Menu(menubar,tearoff=0)
            fgscan=Menu(menubar,tearoff=0)
            report=Menu(menubar,tearoff=0)
            maintance=Menu(menubar,tearoff=0)
            self.root.config(menu=menubar)
            menubar.add_cascade(label="FILE",menu=file)        
            menubar.add_cascade(label="DAIMLER_SCAN_STATION",menu=production)
            menubar.add_cascade(label="ASHOK_LEYLAND_SCAN_STATION",menu=fgscan)
            menubar.add_cascade(label="REPORT",menu=report)
            menubar.add_cascade(label="MAINTNANCE",menu=maintance)
            
            fgscan.add_separator()
            fgscan.add_command(label="DAIMLER_SCAN_STATION",command=fun1)
"""
if __name__=='__main__':
    root=Tk()
    tr=tata_trolley(root)
    root.mainloop()
    

