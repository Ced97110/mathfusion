import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
steps=[(r'$(e_1+e_3)\wedge e_2$','sujet'),(r'$=e_1\wedge e_2+e_3\wedge e_2$','varie'),(r'$=e_{12}-e_{23}$','varie')]
for i,(t,r) in enumerate(steps):
    y=60-i*13; box(ax,8,y,72,9,r,label=t,size='m')
    if i<2: arrow(ax,(44,y),(44,y-4),'fixe')
arrow(ax,(44,21),(44,16),'resultat')
for i,(l,v) in enumerate([(r'$e_{12}$','1'),(r'$e_{13}$','0'),(r'$e_{23}$','−1')]):
    x=16+i*22; box(ax,x,3,20,12,'resultat',label=None)
    text(ax,x+10,11,v,'resultat','l'); text(ax,x+10,5.8,l,'fixe','s')
save(fig,'76-139')
