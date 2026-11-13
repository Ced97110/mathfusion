import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
f=numberline(ax,10,76,12,-5,5,step=5)
text(ax,23,42,'sans hypothèse','fixe','s'); text(ax,65,42,r'hypothèse : $x\geq 0$','resultat','s')
box(ax,4,22,38,14,role='fixe',fill=False,dash=True,label=r'$\sqrt{x^2}=|x|$')
box(ax,46,22,38,14,role='resultat',label=r'$\sqrt{x^2}=x$')
save(fig,'22-055')
