def assemblyURLParameter(**arges):
    ss=''
    j=0
    l=[]
    for k,v in arges.items():
        l.append(k+'='+v)  
    for i,v in enumerate(l):
        j=i+1
        linker='&'*j
        ss+=v+linker
    return ss[:len(ss)-j]

print(assemblyURLParameter(l='html',language='python',active='1',user='abc',password='123456'))
        