from re_demo import process_str

if __name__=="__main__":
    d = dict()
    i=1
    input_data="((((s3.5|s7.4)&(!s4.7))|((s7.4|s4.6)&(s4.5))&(s4.1)&(s4.10))|(kus))&(s3.2)"
    data=process_str(input_data)
    while(i):
        d[i]=data[2]
        str_1=data[1]
        data=process_str(str_1)
        i+=1
        if data==None:
            d[i]=str_1
            break
    print(d)
