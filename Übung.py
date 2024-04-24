def T(n):
    if(n==0 or n==1):return 0
    else:
        if(n==2):return 1
        else:return T(n-1)+T(n-2)+T(n-3)

#for i in range(4,11):
 #   print(T(i)/T(i-1))

ls=[1,2,3,2,5,8,6]

def d(ls):
    ds=[]
    for i in range(0,len(ls)):
        if(i==0):ds.append(1);continue
        if ls[i]>ls[i-1]:ds.append(1)
        else: ds.append(-1)
    return ds

def shuffle(ls):
    ls_l=[]
    ls_r=[]
    x=len(ls)
    if(x%2==0):
        for i in range(int(x/2)):
            ls_l.append(ls[i])
            ls_r.append(ls[int(i+x/2)])
    else:
        for i in range (int((x+1)/2)):
            ls_l.append(ls[i])
        for i in range(int((x+1)/2),x):
            ls_r.append(ls[i])

    print(ls_l,ls_r)
    ls_ges=[]
    for i in range (int(x/2)):
        ls_ges.append(ls_l[i])
        ls_ges.append(ls_r[i])
        if x%2==1 and i==int(x/2-1):ls_ges.append(ls_l[i+1])
    return ls_ges

def shuffle_ord(n):
    k=1
    liste=[i for i in range(n)]
    liste1=shuffle(liste)
    while(liste1!=liste):
        liste1=shuffle(liste1)
        k+=1
    return k

print(shuffle(ls))

            
