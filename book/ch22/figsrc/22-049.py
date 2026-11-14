import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,22,57,'sans la convention','fixe','m'); text(ax,66,57,'avec la convention','sujet','m')
for i in range(3):
    y=42-i*12
    box(ax,4,y,36,8,role='fixe',label=r'$\sqrt{x}$ avec $x\geq 0$',size='s')
    box(ax,48,y,36,8,role='sujet',label=r'$\sqrt{x}$')
text(ax,22,10,'condition répétée','fixe','s')
box(ax,48,5,36,10,role='resultat',label=r'$x\geq 0$ supposé',size='s')
save(fig,'22-049')
