import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,r'un $v$ tel que $u+v=0$ ?','encre','m')
rows=[(0,r'$0+0=0$','resultat','inversible'),(1,r'$1+v\geq1$','limite','pas d’inverse'),(2,r'$2+v\geq2$','limite','pas d’inverse'),(3,r'$3+v\geq3$','limite','pas d’inverse')]
for i,(u,s,r,t) in enumerate(rows):
    y=44-12*i
    box(ax,4,y,20,9,'sujet',label=f'$u={u}$'); arrow(ax,(24,y+4.5),(32,y+4.5),'fixe')
    box(ax,32,y,30,9,r,label=s); text(ax,75,y+4.5,t,r,'s')
save(fig,'44-261')
