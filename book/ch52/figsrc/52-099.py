import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
xs=[16,44,72]
for x,r,l in zip(xs,['autre','sujet','fixe'],['(6)','(3)','ℤ']):
    box(ax,x-9,50,18,9,r,label=l)
for a,b in ((25,35),(53,63)):
    arrow(ax,(a,54.5),(b,54.5),'fixe')
text(ax,30,59.5,r'$\subset$','fixe','s'); text(ax,58,59.5,r'$\subset$','fixe','s')
text(ax,16,44,'pas maximal','limite','s'); text(ax,44,44,'maximal','resultat','s')
box(ax,2,14,30,10,'sujet',label="3 et 4 dans l'idéal",size='s')
arrow(ax,(33,19),(40,19),'varie')
box(ax,41,14,24,10,'varie',label=r'$4-3=1$')
arrow(ax,(66,19),(70,19),'varie')
box(ax,71,14,15,10,'resultat',label='tout ℤ',size='s')
text(ax,44,30,'ajouter un entier hors de (3)','fixe','s')
save(fig,'52-099')
