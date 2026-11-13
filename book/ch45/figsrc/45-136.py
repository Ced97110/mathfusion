import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
box(ax,2,2,84,50,'fixe',fill=False,r=2); text(ax,16,47,'groupe','fixe','m',weight='bold')
box(ax,6,8,48,32,'sujet',r=2); text(ax,30,36,r'$C(a)$','sujet','m',weight='bold'); text(ax,30,31.5,r'tous les $x$ tels que $ax=xa$','sujet','s')
disc(ax,14,19,4,'fixe',label=r'$a$'); disc(ax,42,19,4,'resultat',label=r'$b$')
text(ax,42,26.5,r'$ab=ba$','resultat','s')
disc(ax,70,19,4,'limite',label=r'$c$'); text(ax,70,26.5,r'$ac\neq ca$','limite','s')
save(fig,'45-136')
