import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
items=[(r'$v$','encre'),(r'$Bv+y$','sujet'),(r'$A(Bv+y)+x$','sujet'),(r'$ABv+Ay+x$','varie'),(r'$(AB,\ Ay+x)$','resultat')]
side=['départ',r'appliquer $(B,\,y)$',r'appliquer $(A,\,x)$',r'étape clé : $A$ linéaire','arrivée : un couple']
ys=[78,60,42,24,6]
for (t,r),y in zip(items,ys): box(ax,6,y,44,9,r,label=t,size='m',lw=1.6 if r=='varie' else 0.8)
for i in range(4):
    r='varie' if i==2 else 'fixe'; arrow(ax,(28,ys[i]-0.5),(28,ys[i+1]+9.5),r,lw=1.6 if i==2 else 1.0)
text(ax,54,ys[0]+4.5,side[0],'fixe','s',ha='left'); text(ax,54,ys[4]+4.5,side[4],'resultat','s',ha='left')
text(ax,32,(ys[0]+ys[1]+9)/2,side[1],'sujet','s',ha='left'); text(ax,32,(ys[1]+ys[2]+9)/2,side[2],'sujet','s',ha='left')
text(ax,32,(ys[2]+ys[3]+9)/2,side[3],'varie','s',ha='left',weight='bold')
text(ax,54,ys[3]+4.5,r'$A(Bv+y)=ABv+Ay$','varie','s',ha='left')
save(fig,'73-109')
