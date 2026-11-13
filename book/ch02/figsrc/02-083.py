import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,36,50,'4','varie','l',weight='bold'); text(ax,44,50,'×','encre','l'); text(ax,52,50,'3','sujet','l',weight='bold')
text(ax,32,50,'nombre de sacs','varie','s',ha='right'); text(ax,56,50,'nombre répété','sujet','s',ha='left')
brace(ax,3,83,38,role='varie',label=None,down=False)
for x in (3,24,45,66):
    box(ax,x,26,17,10,'varie',fill=False,r=2)
    for d in (3.5,8.5,13.5): disc(ax,x+d,31,2,'sujet')
    text(ax,x+8.5,20,'3','sujet','m')
for x in (22,43,64): text(ax,x,20,'+','encre','m')
brace(ax,8,79,16.5,role='resultat',label=None,down=True)
text(ax,44,9,'= 12 billes','resultat','l')
save(fig,'02-083')
