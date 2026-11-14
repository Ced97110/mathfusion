import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,16,64,r'$(p,q)$','encre','m'); text(ax,34,64,r'$(r,s)$','encre','m')
cells={'p':(7,46,'sujet'),'r':(25,46,'varie'),'q':(7,31,'varie'),'s':(25,31,'sujet')}
for k,(x,y,r) in cells.items(): box(ax,x,y,18,12,r,label=f'${k}$')
text(ax,58,52,r'$+\,ps$','sujet','l',ha='left'); text(ax,58,38,r'$-\,qr$','varie','l',ha='left')
text(ax,44,20,r'$(ps-qr)\,e_1\wedge e_2$','resultat','l')
text(ax,44,9,r'$1\times1-2\times1=-1$','resultat','m')
save(fig,'76-119')
