import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
cw,ch=3.9,6
X=lambda c:6+cw*(c-2)
rows=[(12,52,(3,4)),(15,38,(3,5)),(21,24,(3,7))]
def cell(c,y,role,fill_role,z=2,lw=0.8,ec=None):
    ax.add_patch(Rectangle((X(c),y),cw,ch,fc=FILL[fill_role],ec=COL[ec or role],lw=lw,zorder=z))
for n,y,fac in rows:
    for c in range(2,n): cell(c,y,'resultat','resultat')
    cell(n,y,'sujet','sujet',2.1)
    text(ax,X(n)+cw/2,y+3,str(n),'sujet','s')
    for f in fac:
        cell(f,y,'varie','varie',2.3)
        text(ax,X(f)+cw/2,y+3,str(f),'varie','s')
    cell(n-1,y,'limite','resultat',2.6,1.4)
    if n in fac: pass
    # les facteurs sont toujours avant le précédent : on les redessine avec leur nombre
    for f in fac:
        if f==n-1: raise SystemExit('facteur = précédent')
cx=X(11)+cw/2
text(ax,cx,64,'11 : pas utilisé','limite','s')
arrow(ax,(cx,62.5),(cx,59),'limite',lw=0.9)
for y,role,s in ((11,'resultat','rangs avant : supposés vrais'),(3,'varie','facteurs : ceux qui servent')):
    ax.add_patch(Rectangle((6,y),cw,cw,fc=FILL[role],ec=COL[role],lw=0.8,zorder=2))
    text(ax,12,y+2,s,role,'s',ha='left')
save(fig,'01-158')
