def encoder(input_str):
    out_str = ''
    tmp_str = ''
    try:
        for st in input_str:
            if tmp_str == '':
                tmp_str = st
            if st in tmp_str:
                tmp_str += st
            else:
                out_str += tmp_str[0]+str(len(tmp_str))
                tmp_str = st
        out_str += tmp_str[0]+str(len(tmp_str))    
    except Exception as e:
        print("encoder having some truble: {} plesase check your input string".format(e))            
    return out_str
 
def findinteger(input_str,i):
    try:
        stx = input_str[i]
        if i == (len(input_str)-1):
            return stx
        if input_str[i+1].isnumeric():
            stx += findinteger(input_str,i+1)
    except Exception as e:
        print(e)         
    return stx 

# st = 'b30c6a4d15' #'a5b3c2d1a2'
def decoder(input_str):
    substring = ''
    out_str = ''
    try:
        for i in range(len(input_str)):            
            if not input_str[i].isnumeric():
                substring = input_str[i]
            else:
                num = int(findinteger(input_str,i))
                out_str += num * substring
                substring =''
    except Exception as e:
        print("decoder having some truble: {} plesase check your input string".format(e))
    return out_str


string_arry = ["abbbbbbbbbb", "bbbccccccddddddddddddddd", "abbbcdddd", "aaaabbbccc", "aaaabbbccdaa"]

for st in string_arry:
    print("input string: {}".format(st))
    print("encoded string: {}".format(encoder(st)))
    print("decoded string: {}".format(decoder(encoder(st))))
    print("------------------------------------------------------------------")
