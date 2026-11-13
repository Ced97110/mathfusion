import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(54)
parts=[('PPCM',22,'sujet','plus petit\nmultiple commun'),('(4, 6)',20,'fixe','les deux\nnombres'),('= 12',18,'resultat','le résultat')]
x=12; tot=sum(p[1] for p in parts)+4; x=(W-tot)/2
for t,w_,r,m in parts:
    box(ax,x,34,w_,11,r,label=t,size='xl')
    arrow(ax,(x+w_/2,33),(x+w_/2,23),r)
    text(ax,x+w_/2,16,m,r,'s')
    x+=w_+2
brace(ax,(W-tot)/2,x-2,47,'fixe',label='une ligne, pas une phrase',down=False)
save(fig,'05-129')
