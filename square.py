a=[]
b=[]
for i in range(0,4):
	x,y=map(int,input().split())
	a.append(x)
	b.append(y)
p=((a[0]-a[1])**2+(b[0]-b[1])**2)**(0.5)
q=((a[1]-a[2])**2+(b[1]-b[2])**2)**(0.5)
r=((a[2]-a[3])**2+(b[2]-b[3])**2)**(0.5)
s=((a[3]-a[0])**2+(b[3]-b[0])**2)**(0.5)
if(p==q==r==s):
	print("yes")
else:
	print("no")
  
  