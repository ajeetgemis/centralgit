import xlrd as OR
import time
file_path="D:\chrome webdriver\WebLink - Item Inventory.xls"
sheet_name="sheet"
#xb=OX.load_workbook(file_path)
#xb=OR.load_workbook(file_path)
#xs=xb[sheet_name]
xb=OR.open_workbook(file_path)
xs=xb.sheet_by_name(sheet_name)
print(xs)
max_row=xs.nrows
max_column=xs.ncols
print("No.od row",max_row,"no of column",max_column)
list1=[]
#print(xs.cell(4,2).value)
try:
    for i in range(4,max_row+1):
        item1=xs.cell_value(i,1)
        item2=xs.cell_value(i,3)
        item2=xs.cell_value(i,4)
       # time.sleep(1)
        
        print(item1,item2)
except:
    pass
