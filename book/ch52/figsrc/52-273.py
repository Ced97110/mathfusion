import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,44,47,r'Restes par 6, divisés par $\mathbb{Z}/6$ entier','sujet','m')
box(ax,4,14,80,22,'resultat',fill=True,dash=True)
for i in range(6):
    disc(ax,12+i*12.8,25,4.2,'sujet',label=str(i))
text(ax,44,40,'une seule classe','resultat','s')
text(ax,44,8,'0 = 1 : anneau nul','resultat','m')
save(fig,'52-273')
