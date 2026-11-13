import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(98)
text(ax,46,94,'position → écriture','sujet','m')
xs=(8,28,48,68)
for x,hd,d in zip(xs,('1 000','100','10','1'),'4329'):
    box(ax,x,76,16,14,'sujet',label=f'{hd}\n{d}',size='l')
for x in xs: arrow(ax,(x+8,75),(x+8,69.5),'varie')
for x,v in zip(xs,('4 000','300','20','9')):
    box(ax,x,58,16,10,'sujet',label=v,size='m')
text(ax,46,53,'calcul, case par case','varie','m')
line(ax,[(4,47),(84,47)],'fixe',dash=True)
f=numberline(ax,10,80,27,4300,4400,10,labels=False,arrow_right=True)
disc(ax,f(4329),27,1.6,'sujet')
text(ax,f(4329),22,'4 329','sujet','s'); text(ax,80,22,'4 400','fixe','s')
brace(ax,f(4329),80,18,'autre',label='droite : ordre et distance')
arrow(ax,(f(4329),29),(10,29),'resultat',curve=0.4)
text(ax,3,38,'arrondi : environ 4 300','resultat','s',ha='left')
save(fig,'01-183')
