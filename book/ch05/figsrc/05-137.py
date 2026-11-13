import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(64)
cw=8.5; X=[18+10*c for c in range(5)]
def row(y,spec):
    for c,(t,r,d) in enumerate(spec):
        box(ax,X[c],y,cw,8,r,fill=not d,label=t,size='m',dash=d)
r90=[('2','sujet',0),('3','sujet',0),('3','sujet',0),('5','sujet',0),(None,'limite',1)]
r630=[('2','autre',0),('3','autre',0),('3','autre',0),('5','autre',0),('7','varie',0)]
rg=[(None,'resultat',0)]*4+[(None,'limite',1)]
rp=[(None,'resultat',0)]*4+[(None,'varie',0)]
y=[46,34,16,4]
row(y[0],r90); text(ax,15,y[0]+4,'90','sujet','m',ha='right')
row(y[1],r630); text(ax,15,y[1]+4,'630','autre','m',ha='right')
line(ax,[(2,29),(86,29)],'fixe',dash=True)
row(y[2],rg); text(ax,69,y[2]+4,'PGCD = 90','resultat','s',ha='left')
row(y[3],rp); text(ax,69,y[3]+4,'PPCM = 630','resultat','s',ha='left')
text(ax,X[4]+cw/2-18,60,'le 7 est dans 630 seulement','varie','s')
save(fig,'05-137')
