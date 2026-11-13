import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
y=34
f=numberline(ax,6,40,y,0,50,step=5,labels=False,role='sujet',arrow_right=False)
text(ax,f(0),y-4,'0','sujet','s'); text(ax,f(50),y-4,'50','sujet','s')
brace(ax,f(0),f(50),y-6.5,'sujet',label='la table de 5 s’arrête')
line(ax,[(42,y),(72,y)],'limite',dash=True)
text(ax,57,y+4,'hors de la table','limite','s')
disc(ax,76,y,1.8,'resultat')
text(ax,76,y+5,'1 000 003','resultat','s')
box(ax,4,4,80,10,'resultat',label='1 000 003 = 5 × 200 000 + 3',size='m')
arrow(ax,(76,y-2.2),(76,14.5),'resultat')
text(ax,6,17.5,'la règle vaut pour tous','resultat','s',ha='left')
save(fig,'05-034')
