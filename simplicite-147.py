def erase(string):
    res=string.split(' ')
    rep=""
    size=(len(res))
    for i in range (size-1) :
        if (res[i]=='' or res[i]==' ') and res[i+1]!='':
            rep+=" "+res[i]
        if i>0 and (res[i]=='' or res[i]==' ') and res[i-1]!=' ':
            rep+=" "+res[i]
        else :
            rep+=""+res[i]
    rep+=""+res[size-1]
    return rep
