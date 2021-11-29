import re

ON="((((s3.5|s7.4)&(!s4.7))|((s7.4|s4.6)&(s4.5))&(s4.1)&(s4.10))|(kus))&(s3.2)"

# pattern="(.*)[&](.*)"
# matchobj=re.search(pattern,ON)
#
# print(matchobj[1])
# print(matchobj[2])

# # on1="((((s3.5||s7.4)&(!s4.7))||((s7.4||s4.6)&(s4.5))&(s4.1)&(s4.10))||(kus))"
# pattern1="(.*)[&|\|](.*)"
# matchobj1=re.search(pattern1,ON)
# print(matchobj1[1])
# print(matchobj1[2])

ON5="((s3.5||s7.4)&(!s4.7))||(s7.4||s4.6)"
str1="&"
str2=r"||"
pattern1="(.*)["+str2+"](.*)"
matchobj1=re.search(pattern1,ON5)
print(matchobj1[1])
print(matchobj1[2])