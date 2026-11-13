import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(66)
sq=6.5; c2=37; c3=58
text(ax,c2+sq,60,'premier 2','encre','s'); text(ax,c3+sq,60,'premier 3','encre','s')
def row(y,n2,n3,role):
    for i in range(n2): rect(ax,c2+i*sq,y,sq,sq,role)
    for i in range(n3): rect(ax,c3+i*sq,y,sq,sq,role)
row(44,2,1,'sujet'); text(ax,2,47.25,r'$12 = 2^2\times 3$','sujet','s',ha='left')
row(34,1,2,'autre'); text(ax,2,37.25,r'$18 = 2\times 3^2$','autre','s',ha='left')
line(ax,[(2,29),(86,29)],'fixe',dash=True)
row(18,1,1,'resultat'); text(ax,2,21.25,'PGCD : plus petit','resultat','s',ha='left'); text(ax,80,21.25,r'$=6$','resultat','m')
row(6,2,2,'resultat'); text(ax,2,9.25,'PPCM : plus grand','resultat','s',ha='left'); text(ax,80,9.25,r'$=36$','resultat','m')
save(fig,'05-133')
