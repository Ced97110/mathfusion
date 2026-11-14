import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,38,52,'premier','sujet','m',weight='bold'); text(ax,71,52,'se factorise','autre','m',weight='bold')
text(ax,2,38,'nombres','fixe','m',ha='left'); text(ax,2,14,'polynômes','fixe','m',ha='left')
cells=[(20,30,'sujet','7','facteurs : 1 et 7'),(56,30,'autre','12',r'$3\times4$'),
       (20,6,'sujet',r'$x^2+1$','constantes et lui-même'),(56,6,'autre',r'$x^2-9$',r'$(x+3)(x-3)$')]
for x,y,r,e,n in cells:
    w=33 if x==20 else 30
    box(ax,x,y,w,16,r); text(ax,x+w/2,y+10.5,e,r,'l'); text(ax,x+w/2,y+4,n,r,'s')
save(fig,'18-097')
