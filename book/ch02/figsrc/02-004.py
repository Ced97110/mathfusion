import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
def rect(x,y,w,h,role,fill=True,dash=False,lw=0.5):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=lw,ls='--' if dash else '-',zorder=2))
def bar(x):
    for k in range(10): rect(x,40+2*k,2.5,2,'sujet')
text(ax,18,70,'avant','encre','m'); text(ax,68,70,'après','encre','m')
for x in [5+3.5*i for i in range(5)]: bar(x)
rect(18.5,39.5,3.5,21,'varie',False,True,0.8)
for x in (25,28): rect(x,40,2,2,'sujet')
text(ax,17.5,35,'5 dizaines, 2 unités','sujet','s')
arrow(ax,(32,48),(48,48),'varie')
text(ax,44,63,'1 dizaine → 10 unités','varie','s')
for x in [50+3.5*i for i in range(4)]: bar(x)
for r in range(2):
    for c in range(5): rect(66+3*c,40+3*r,2,2,'varie')
for x in (81,84): rect(x,40,2,2,'sujet')
text(ax,68,35,'4 dizaines, 12 unités','sujet','s')
text(ax,17.5,27,'50 + 2 = 52','resultat','s'); text(ax,68,27,'40 + 12 = 52','resultat','s')
text(ax,44,16,'même valeur, rien à rendre','resultat','s')
save(fig,'02-004')
