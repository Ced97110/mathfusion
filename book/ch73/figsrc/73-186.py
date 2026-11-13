import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
def sq(x0,tag):
    P={1:(x0,18),2:(x0+22,18),3:(x0+22,40),4:(x0,40)}
    for a,b in [(1,2),(2,3),(3,4),(4,1)]: line(ax,[P[a],P[b]],'fixe')
    return P
L=sq(8,'a'); R=sq(54,'b')
line(ax,[L[1],L[3]],'sujet',lw=1.3); line(ax,[L[2],L[4]],'autre',lw=1.3)
line(ax,[R[1],R[3]],'sujet',lw=1.3,dash=True); line(ax,[R[2],R[3]],'limite',lw=1.5); line(ax,[R[2],R[4]],'autre',lw=1.3)
arrow(ax,(R[1][0]+3,15),(R[2][0]-3,15),'varie',curve=0.5,both=True)
for P in (L,R):
    for k,(x,y) in P.items(): disc(ax,x,y,2.4,'fixe',label=str(k),size='s')
text(ax,19,10,'{1, 3} et {2, 4} gardés','sujet','s'); text(ax,19,5,'par les 8 symétries','sujet','s')
text(ax,65,10,'échange de 1 et 2','varie','s'); text(ax,65,5,'{1, 3} → {2, 3} : rompu','limite','s')
[p.set_zorder(3.5) for p in ax.patches if isinstance(p,Circle)]
save(fig,'73-186')
