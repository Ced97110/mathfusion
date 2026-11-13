import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
cx=[14,44,74]
text(ax,29,55,r"d'abord $(1\,3)$",'sujet','s'); text(ax,59,55,r'puis $(1\,2)$','varie','s')
rows=[(44,[1,3,3]),(32,[2,2,1]),(20,[3,1,2])]
for y,v in rows:
    for c,n,r in zip(cx,v,['sujet','fixe','resultat']): disc(ax,c,y,3,r,label=str(n),size='s')
    arrow(ax,(cx[0]+3.5,y),(cx[1]-3.5,y),'sujet'); arrow(ax,(cx[1]+3.5,y),(cx[2]-3.5,y),'varie')
text(ax,44,10,r'$(1\,2)(1\,3)=(1\,3\,2)$','resultat','l')
text(ax,44,3.5,r'autre ordre : $(1\,2\,3)$','limite','s')
save(fig,'47-063')
