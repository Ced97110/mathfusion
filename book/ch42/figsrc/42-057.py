import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
box(ax,6,44,32,24,'sujet'); box(ax,50,44,32,24,'autre')
text(ax,22,72,'A','sujet','xl',weight='bold'); text(ax,66,72,'B','autre','xl',weight='bold')
for x,r in [(22,'sujet'),(66,'autre')]:
    text(ax,x,60,'gourde',r,'m'); text(ax,x,51,'carte',r,'m')
text(ax,44,56,'=','varie','xl',weight='bold')
text(ax,44,39,r'cas $A=B$ : les sens diffèrent','varie','s')
box(ax,4,22,80,11,'resultat'); text(ax,44,29,'Judson : inclus, égal permis','resultat','s'); text(ax,44,25,r'$A\subset B$ : vrai','resultat','s')
box(ax,4,6,80,11,'limite'); text(ax,44,13,'livre : inclus ET différent','limite','s'); text(ax,44,9,r'$A\subset B$ : faux','limite','s')
save(fig,'42-057')
