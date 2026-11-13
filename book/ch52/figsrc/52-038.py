import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
line(ax,[(44,6),(44,70)],'fixe',dash=True)
text(ax,23,70,'multiples de 4 : absorbent','resultat','s'); text(ax,65,70,'impairs : n’absorbent pas','limite','s')
box(ax,13,48,20,10,'sujet',label=r'$8\in I$'); arrow(ax,(23,48),(23,30),'varie'); text(ax,31,39,'× 5','varie','s')
box(ax,13,18,20,10,'resultat',label=r'$40\in I$')
box(ax,55,48,20,10,'sujet',label=r'$3\in I$'); arrow(ax,(65,48),(65,30),'varie'); text(ax,73,39,'× 2','varie','s')
box(ax,55,18,20,10,'limite',label=r'$6\notin I$')
save(fig,'52-038')
