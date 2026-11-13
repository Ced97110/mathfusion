import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
text(ax,22,68,'nombres habituels','sujet','m'); text(ax,64,68,r'$\mathbb{Z}/2$','autre','l')
text(ax,22,54,r'$2\times\frac{1}{2}=1$','resultat','l'); text(ax,22,44,'la moitié existe','resultat','s')
for i,(yy,v) in enumerate([(52,'0'),(36,'1')]):
    disc(ax,54,yy,3.5,'autre',label=v)
disc(ax,76,52,3.5,'autre',label='0'); disc(ax,76,36,3.5,'limite',fill=False,label='1')
arrow(ax,(58,52),(72,52),'varie'); arrow(ax,(58,36),(72,52),'varie')
text(ax,65,58,r'$\times 2$','varie','m')
text(ax,76,28,'rien n’arrive','limite','s')
text(ax,44,16,r'$\frac{1}{2}$ n’existe pas : 2 = 0','limite','m')
text(ax,44,7,'2 n’est pas inversible','limite','s')
save(fig,'72-101')
