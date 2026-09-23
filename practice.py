def count_alphabets_digits(s):
    d={'Digits':0,'Alphabets':0}
    for ch in s:
        if ch.isalpha():
            d['Alphabets']+=1
        elif ch.isdigit():
            d['Digits']+=1
        else:
            pass
    return(d)
d=count_alphabets_digits('JamesBond007')
print(d)
d=count_alphabets_digits('YashashreeParab815')
print(d)
