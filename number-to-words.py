x = input("Enter a number:")



def num(x,dg):
    x = str(x)
    if x == '0': return "Zero"
    chk = 0
    for i in x:
        chk+= int(i)
    if chk == 0: return ''
    
    y = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',\
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',\
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',\
        19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',\
        50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',\
        90: 'ninety', 100: 'hundred', 1000: 'thousand',\
        100000: 'lakh', 10000000: 'crore',0:''}
    
    if int(x) in y and int(x)<100: return y[int(x)].title()
    z = len(x)
    
    c = [1,1,100,1000,1000,100000,100000,10000000,10000000,10000000]
    a = [];b = []

    
    for i in range(z+1):
        try:
            a.append(x[i]+ '0'*len(x[(i+1):]))
        except Exception: pass    
    
    a.reverse()
    a = [int(i) for i in a]
    d = c[:len(a)]

    for i,j in zip(a,d):b.append(i//j)
        
    op = []
    er = 3
    rt = er + 2

    for i in range(len(b)):
        if i == 0:
            op.append(b[:er])
            continue
        ty = b[er:rt]
        op.append(ty)
        er += 2
        rt += 2

    for i in op[::-1]:
        if not i: op.pop()
    ans = []

    jdk = {1:'hundred', 2 : 'thousand',3 : 'lakhs', 4: 'crore'}

    
    
    
    for i,j in zip(op,range(1,len(op)+1)):
        io = 0
        for k in range(2):
            if len(i)>= 2: io += i[k]
            elif len(i)== 1:
                io += i[k]
                break
       
        if io in y:
            if j!=1:
                if sum(i)!= 0: ans.append(y[io] + ' ' + jdk[j])
                elif sum(i)== 0: ans.append(y[io])
                
            elif j==1 and len(i)== 3:
                if i[2] !=0 : ans.append( y[i[2]]+ ' ' + jdk[j]+ ' '+ y[io])
                elif i[2] ==0 : ans.append( y[i[2]]+ ' '+ y[io])

                
        else:
            for l,n in zip(i,range(len(i))):
                if n == len(i)-2 and j!=1 and l!=0:
                    ans.append(jdk[j])
                    ans.append(y[l])
                elif n == len(i)-1 and j==1 and l!=0 and len(i) == 3:
                    
                    ans.append(jdk[j])
                    ans.append(y[l])   
                else: ans.append(y[l])
           
            
    ans.reverse()
    fin = ''
    if dg == 0: print(x)
    for i in ans:
        if i: fin+= i.strip() + ' '
    return fin.title() 
        

if len(x)>9:
    x1 = x[:-7]
    x2 = x[-7:]
    nw2 = num(x1,1)
    nw1 = num(x2,1)
    print(x)
    print(nw2 + 'Crore'+ ' '+ nw1)
elif len(x)<=9: print(num(x,0))

    
    
    
    
    

    













