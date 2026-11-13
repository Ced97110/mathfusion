import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,23,61,'que 2 et 5','resultat','l',weight='bold')
text(ax,65,61,'un autre facteur','limite','l',weight='bold')
L=[('4 = 2 × 2',2),('5 = 5',1),('8 = 2 × 2 × 2',3)]; R=[('3 = 3',1),('6 = 2 × 3',2),('11 = 11',1)]
for i in range(3):
    y=42-i*18
    for (lab,n),x,role in ((L[i],3,'resultat'),(R[i],45,'limite')):
        box(ax,x,y,40,14,role,label=lab)
        for k in range(n): disc(ax,x+36-k*0.0-(n-1-k)*5.2-0.0,y+3.0,1.8,role)
save(fig,'08-083')
