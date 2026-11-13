import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
x0,L=4,80
def bar(n,y,role):
    w=L/n
    for i in range(n):
        ax.add_patch(Rectangle((x0+i*w,y),w,6,fc=FILL[role],ec=COL[role],lw=0.5,zorder=2))
bar(23,56,'sujet'); bar(9,44,'autre')
text(ax,x0,65,'945 × 23 = 21 735','sujet','m',ha='left')
text(ax,x0,40,'2 415 × 9 = 21 735','autre','m',ha='left')
line(ax,[(x0+L,43),(x0+L,63)],'fixe',dash=True)
text(ax,44,53,'même longueur : écart 0','resultat','s')
cw=22; xs=[3,33,63]
couples=['(−5, 2)','(18, −7)','(41, −16)']
roles=['sujet','varie','varie']
for x,c,r in zip(xs,couples,roles): box(ax,x,12,cw,9,r,label=c)
for i in range(2):
    a=xs[i]+cw/2; b=xs[i+1]+cw/2
    arrow(ax,(a,22),(b,22),'varie',curve=-0.45)
    text(ax,(a+b)/2,32.5,'+ 23 et − 9','varie','s')
text(ax,44,6,'tous donnent 105','resultat','m')
save(fig,'05-147')
