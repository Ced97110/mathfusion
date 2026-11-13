import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
X=lambda c: 8+6*(c-2)
text(ax,8,62,'récurrence ordinaire','autre','m',ha='left'); text(ax,8,34,'récurrence forte','sujet','m',ha='left')
yt,yb=44,14
for c in range(2,13):
    cx=X(c)+3
    # haut
    if c==2: box(ax,X(c),yt,6,6,'resultat'); text(ax,cx,yt+3,'2','encre','s')
    elif c==11: box(ax,X(c),yt,6,6,'autre')
    elif c==12: box(ax,X(c),yt,6,6,'varie'); text(ax,cx,yt+3,'12','encre','s')
    elif c in (3,4): box(ax,X(c),yt,6,6,'limite',fill=False,dash=True)
    else: box(ax,X(c),yt,6,6,'fixe',fill=False)
    # bas
    if c==2: box(ax,X(c),yb,6,6,'resultat'); text(ax,cx,yb+3,'2','encre','s')
    elif c==12: box(ax,X(c),yb,6,6,'varie'); text(ax,cx,yb+3,'12','encre','s')
    else:
        box(ax,X(c),yb,6,6,'sujet')
        if c in (3,4): text(ax,cx,yb+3,str(c),'encre','s')
arrow(ax,(65,50),(71,50),'varie',curve=-0.6)
text(ax,58,57,'on suppose 11 seul','autre','s')
text(ax,24,40,'3 et 4 : pas couverts','limite','s')
brace(ax,8,68,12,'sujet','on suppose 2 à 11')
arrow(ax,(17,20),(71,20),'varie',curve=-0.35); arrow(ax,(23,20),(71,20),'varie',curve=-0.3)
save(fig,'01-160')
