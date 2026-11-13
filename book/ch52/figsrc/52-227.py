import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
L=[(74,10,'sujet','PGCD(7, 12) = 1'),(58,10,'varie','7 est inversible'),(42,10,'sujet',r'$\varphi(12)=4$'),(24,14,'resultat','$7^{4}=2\\,401$\n$=200\\times12+1$')]
for i,(y,h,r,l) in enumerate(L):
    box(ax,2,y,44,h,r,label=l,size='s')
    if i: arrow(ax,(24,L[i-1][0]),(24,y+h+0.5),'sujet')
R=[(74,10,'PGCD(8, 12) = 4'),(58,10,'pas inversible'),(40,14,'$8^{4}=4\\,096$\nreste 4, pas 1')]
for i,(y,h,l) in enumerate(R):
    box(ax,50,y,36,h,'limite',label=l,size='s')
    if i: arrow(ax,(68,R[i-1][0]),(68,y+h+0.5),'limite')
save(fig,'52-227')
