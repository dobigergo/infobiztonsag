
def euklidesz(a,b):
	if a < b:
		a,b=b,a
	r=[[a,b],[0]]
	q=0
	while r[0][len(r[0])-1] != 0:
		q=int(a/b)
		r[0].append(a%b)
		r[1].append(int(a/b))
		a=b
		b=r[0][len(r[0])-1]
	return r
	
def euklideszp(a):
	x=[1,0]
	y=[0,1]
	for i in range(len(a[0])-3):
		x.append(x[len(x)-1]*a[1][len(x)-1]+x[len(x)-2])
		y.append(y[len(y)-1]*a[1][len(y)-1]+y[len(y)-2])
	
	return y[len(y)-1]
	
print(euklidesz(4658923553523,254124222)," ",euklideszp(euklidesz(4658923553523,254124222)))

def s_and_m(g,e,n):
	bin_e=bin(e)
	list_bin_e=list(bin_e)
	list_bin_e.pop(0)
	list_bin_e.pop(0)
	mod=1
	tmp=g
	for i in range(len(list_bin_e)):
		if list_bin_e[len(list_bin_e)-1-i]=='1':
			mod*=tmp
		tmp=(tmp**2)%215		
	return mod%n

print(s_and_m(12712543312,7531213515,2151531))





