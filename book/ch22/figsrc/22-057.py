import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,'on divise chaque exposant par 2','varie','m')
rows=[(r'$\sqrt{x^6}$',r'$x^3$'),(r'$\sqrt{x^8}$',r'$x^4$'),(r'$\sqrt{a^{10}}$',r'$a^5$'),(r'$\sqrt{25m^2n^6}$',r'$5mn^3$')]
for i,(a,b) in enumerate(rows):
    y=44-i*14
    box(ax,4,y,38,10,role='sujet',label=a); arrow(ax,(44,y+5),(54,y+5),'varie'); box(ax,56,y,30,10,role='resultat',label=b)
save(fig,'22-057')
