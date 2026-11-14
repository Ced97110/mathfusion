import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,r'$p=5$ : $a^p$ et $a$ même reste','encre','m')
for y,a,pw,r in [(38,2,'32',2),(14,5,'3\\,125',0)]:
    box(ax,2,y,14,12,'sujet',label=rf'$a={a}$',size='s')
    arrow(ax,(16,y+6),(22,y+6),'varie')
    box(ax,22,y,26,12,'fixe',label=rf'${a}^5={pw}$',size='s')
    arrow(ax,(48,y+6),(54,y+6),'varie')
    box(ax,54,y,32,12,'resultat',label=rf'reste ${r}$ = reste de $a$',size='s')
save(fig,'52-095')
