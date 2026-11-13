import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,44,70,'dans la liste : les places','encre','s')
vals=[(32,'sujet'),(68,'autre'),(29,'sujet'),(73,'autre')]
f=numberline(ax,8,78,26,10,90,20,labels=True,arrow_right=False)
for i,(v,r) in enumerate(vals):
    cx=12.5+i*21
    box(ax,cx-8.5,56,17,9,r,label=str(v)); arrow(ax,(cx,56),(f(v),27.8),r,lw=0.7)
    disc(ax,f(v),26,1.2,r)
brace(ax,f(29),f(32),18,'sujet',label='proches de 30'); brace(ax,f(68),f(73),18,'autre',label='proches de 70')
text(ax,44,6,'regroupement : par la valeur','encre','s')
save(fig,'10-047')
