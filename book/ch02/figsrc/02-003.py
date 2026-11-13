import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
def rect(x,y,w,h,role,fill=True,dash=False):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.6,ls='--' if dash else '-',zorder=2))
rect(4,54,23,24,'fixe',False); rect(29,54,13,24,'fixe',False)
text(ax,15.5,82,'5 dizaines','sujet','s'); text(ax,35.5,82,'2 unités','sujet','s')
for x in [5.5+4.5*i for i in range(5)]:
    for k in range(10): rect(x,56+2*k,3,2,'sujet')
for x in (31,36): rect(x,56,3,3,'sujet')
for i in range(7): rect(46+4*i,56,3,3,'limite',False,True)
text(ax,60,62,'7 unités à retirer','limite','s')
text(ax,60,50,'7 > 2 : impossible','limite','m')
line(ax,[(4,44),(84,44)],'fixe',dash=True)
box(ax,6,30,52*1.4,5,'sujet',label='52 dans la caisse',size='s')
box(ax,6,20,27*1.4,5,'varie',label='27 à rendre',size='s')
text(ax,62,22.5,'le total suffit : 52 > 27','resultat','s')
text(ax,44,9,'manque : colonne, pas total','encre','s')
save(fig,'02-003')
