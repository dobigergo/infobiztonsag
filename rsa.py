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
	
print(euklidesz(100,519)," ",euklideszp(euklidesz(100,519)))