import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,43,74,r'$f$','varie','xl',ha='right')
text(ax,43,74,r'$(y)$','sujet','xl',ha='left')
arrow(ax,(39,68),(26,60),'varie'); arrow(ax,(47,68),(62,60),'sujet')
text(ax,24,55,r'$f$ donne un nombre','varie','s')
text(ax,64,55,r'$y$ est un contrôle','sujet','s')
for x,v in ((4,2),(48,3)):
    text(ax,x+19,40,f'$y$ = {v}','sujet','s')
    arrow(ax,(x+19,37),(x+19,31),'sujet')
    box(ax,x,18,38,12,'varie',label=f'$f$({v}) = ?',size='s')
text(ax,44,8,'une inconnue pour chaque $y$','varie','s')
save(fig,'80-260')
