t= 10,20.6,30,30,30,40,'hello','vishal'
t1= (10,40,10,50,67,6.7,6.9,'hello')

print(t,t1,sep='\n')
print(len(t))

#tuple methods
#count method
print(f"no of occ of 30: {t.count(30)}")
print(f"no of l in hello in tuple t : {t[6].count('l')}")

#index method
print(f"index of 30: {t.index(30)}")
print(f"index of h in hello : {t[6].index('l')}")
