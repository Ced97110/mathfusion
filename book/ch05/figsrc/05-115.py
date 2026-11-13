import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
cols=[1,2,3,4,6,8,9,12,18,24,36]
d24=[1,2,3,4,6,8,12,24]; d36=[1,2,3,4,6,9,12,18,36]
com=[n for n in d24 if n in d36]
cc=4; cw=SIZE['m']*0.2124; cell=cc*cw; x0=(88-len(cols)*cell)/2
def mono(x,y,s):
    ax.text(x,y,s,color=COL['encre'],fontsize=SIZE['m'],family='DejaVu Sans Mono',ha='left',va='center',zorder=5)
def row(y,vals,role,lw=0.8):
    s=''
    for i,n in enumerate(cols):
        if n in vals:
            ax.add_patch(Rectangle((x0+i*cell+0.4,y-3.5),cell-0.8,7,ec=COL[role],fc=FILL[role],lw=lw,zorder=2))
        s+=f'{(str(n) if n in vals else ""):^{cc}}'
    mono(x0,y,s)
row(50,d24,'sujet'); row(30,d36,'autre'); row(10,com,'resultat')
i12=cols.index(12)
ax.add_patch(Rectangle((x0+i12*cell+0.4,6.5),cell-0.8,7,ec=COL['resultat'],fc='none',lw=2.0,zorder=3))
text(ax,2,59,'diviseurs de 24','sujet','s',ha='left')
text(ax,2,39,'diviseurs de 36','autre','s',ha='left')
text(ax,2,19,'diviseurs communs : le plus grand est 12','resultat','s',ha='left')
text(ax,44,71,r'gcd(24, 36) $=$ 12','resultat','l')
save(fig,'05-115')
