import pandas as pd

print("Hello")
Left_Tabl: object = pd.read_excel('C:/PROJECT/Jgtxfnrb2/Excel_Data/Левый.xlsx')
Right_Tabl: object = pd.read_excel('C:/PROJECT/Jgtxfnrb2/Excel_Data/Правый.xlsx')
print(Left_Tabl.head(1))
print(Right_Tabl.head(2))
Left_Tabl.to_excel('C:/PROJECT/Jgtxfnrb2/Excel_Data/Левый2.xlsx')
print(Left_Tabl.columns.to_list)
print(Left_Tabl.columns.to_list)
