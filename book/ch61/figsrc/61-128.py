import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,2,6,44,44,'fixe',label=None,dash=True)
text(ax,24,56,r'$K$ : une infinité','fixe','s')
import itertools
for i,j in itertools.product(range(5),range(4)):
    disc(ax,8+i*8,14+j*9,2.0,'fixe')
text(ax,24,12,'…','fixe','m') if False else None
box(ax,58,18,28,28,'sujet',label=None)
for i in range(3): disc(ax,66+i*8,34,2.6,'sujet'); 
for i in range(3): text(ax,66+i*8,28,rf'$a_{i}$','sujet','s')
text(ax,72,56,r'$L$ : degré fini','resultat','s')
box(ax,56,16,32,32,'resultat',fill=False,lw=1.2)
text(ax,72,12,'3 coefficients','sujet','s')
arrow(ax,(47,28),(55,28),'varie'); text(ax,51,35,'on garde','varie','s') if False else None
save(fig,'61-128')
