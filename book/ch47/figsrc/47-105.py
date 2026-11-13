import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,51,r'$\overline{M}$ : ensemble des classes','sujet','l')
box(ax,2,12,84,32,'sujet',fill=False,dash=True)
for x,l in [(6,'multiples\nde 3'),(33,'classe\nde 1'),(60,'classe\nde 2')]:
    box(ax,x,17,22,22,'sujet',label=l)
text(ax,44,6,'modulo 3 : trois éléments','fixe','m')
save(fig,'47-105')
