import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
X=[28,46,64]
text(ax,8,72,'$x$','sujet','l')
for x,l in zip(X,('1','$+2i$','$+2k$')): text(ax,x,72,l,'sujet','l')
text(ax,10,48,'numérateur','varie','s')
for x,l,ro in zip(X,('1','$-2i$','$-2k$'),('fixe','varie','varie')): text(ax,x,48,l,ro,'l')
arrow(ax,(X[0],68),(X[0],52),'fixe')
for x in X[1:]: arrow(ax,(x,68),(x,52),'varie')
text(ax,X[0]+7,60,'garder','fixe','s',ha='left'); text(ax,55,60,'signe changé','varie','s')
box(ax,14,28,60,10,'sujet',label=r'$N=1+4+0+4=9$')
arrow(ax,(44,27),(44,19),'fixe'); text(ax,48,23,'diviser par 9','fixe','s',ha='left')
box(ax,14,3,60,16,'resultat',label=r'$x^{-1}=\frac{1-2i-2k}{9}$',size='l')
save(fig,'51-190')
