import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
f=numberline(ax,6,84,28,1700,1710,1,labels=False,arrow_right=False)
arrow(ax,(84,28),(86,28),'fixe',lw=0.9)
for v,r in ((1704,'encre'),(1706,'sujet'),(1708,'encre')):
    text(ax,f(v),24,f'{v:,}'.replace(',',' '),r,'s')
disc(ax,f(1704),28,1.2,'resultat'); text(ax,f(1704),18,'426 places','resultat','s')
disc(ax,f(1708),28,1.2,'limite'); text(ax,f(1708),18,'427 places : trop','limite','s')
brace(ax,f(1704),f(1708),13,'varie',label='une place de plus : + 4 €',size='s')
disc(ax,f(1706),28,1.0,'sujet'); arrow(ax,(f(1706),44),(f(1706),30),'sujet')
text(ax,f(1706),47,'caisse : 1 706 €','sujet','s')
brace(ax,f(1704),f(1706),30,'resultat',down=False)
text(ax,45,34.5,'reste : 2 €','resultat','s')
save(fig,'03-005')
