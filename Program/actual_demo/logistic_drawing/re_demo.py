import re

def process_str(input_str_demo=None):
    pattern = "[(](.*)[)][&|\|][(](.*)[)]"
    matchobj = re.search(pattern, input_str_demo)
    return matchobj

ON="((((s3.5|s7.4)&(!s4.7))|((s7.4|s4.6)&(s4.5))&(s4.1)&(s4.10))|(kus))&(s3.2)"
pattern=["&","|"]
index_demo=[]
d=dict()
i=1
def getStrInfo(str,target):
    count = 0
    for index,value in enumerate(str):
        if target == value:
            count += 1
            index_demo.append(index)
for target in pattern:
    getStrInfo(ON,target)
index_demo.sort()
index_demo_use=index_demo
# print(index_demo)

def seperate_str(str,index):
    str1=str[:index]
    str2=str[index+1:]
    str1=str1[1:-1]
    str2=str2[1:-1]
    return str1,str2

def find_order(str,i,index_demo_use):
    for a in index_demo_use:
        str1,str2=seperate_str(str,a)
        if str2.count("(")==str2.count(")"):
            d[i]=[a,str1,str2]
            if "&" in str2 or "|" in str2:
                print("please handle")
                print(str2)
                print()
    i+=1
    find_order(d[i-1][1],i,index_demo_use)
find_order(ON,i,index_demo_use)
print(d)

# for i in index_demo_use:
#     str1,str2=seperate_str(ON,i)
#     str1=str1[1:-2]
#     if str2.count("(")==str2.count(")"):
#         d[1]=[i,str1,str2]
#
# index_demo_use.remove(d[1][0])
#
# for i in index_demo_use:
#     str1,str2=seperate_str(d[1][1],i)
#     str1=str1[1:-2]
#     if str2.count("(")==str2.count(")"):
#         d[2]=[i,str1,str2]
#     else:
#         print(str2.count("("),str2.count(")"))
#
# print(d)


