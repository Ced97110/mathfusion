import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
disc(ax,44,56,6,'sujet',label=r'$\mathbb{H}$',size='xl')
arrow(ax,(38.5,52),(22,39),'sujet'); arrow(ax,(49.5,52),(66,39),'sujet')
box(ax,2,10,38,28,'sujet'); box(ax,48,10,38,28,'sujet')
text(ax,21,33,'somme de 4 termes','sujet','s')
text(ax,21,22,r'$\alpha_0+\alpha_1i+\alpha_2j+\alpha_3k$','sujet','s')
text(ax,67,33,'tableau complexe','sujet','s')
for r,row in enumerate((('$a$','$b$'),(r'$-\bar{b}$',r'$\bar{a}$'))):
    for c,l in enumerate(row): text(ax,59+c*16,25-r*8,l,'sujet','m')
text(ax,44,24,'$=$','encre','l')
text(ax,44,4,'mêmes objets, deux écritures','encre','s')
save(fig,'51-184')
