import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def grid(ax,x,y,cw,ch,nc,nr,role,fillrole=None,lw=0.4,fill=True,dash=False):
    for i in range(nc):
        for j in range(nr):
            ax.add_patch(Rectangle((x+i*cw,y+j*ch),cw,ch,ec=COL[role],fc=FILL[fillrole or role] if fill else "none",lw=lw,ls="--" if dash else "-",zorder=2))

fig,ax=canvas(76)
text(ax,36,64,'24 =','encre','l',ha='right'); text(ax,41,64,'4','autre','l'); text(ax,47,64,'×','encre','l'); text(ax,53,64,'6','sujet','l',weight='bold')
text(ax,41,71,r'$d$','autre','s'); text(ax,53,71,r'$q$','sujet','s')
brace(ax,38,56,60,'fixe',label='deux facteurs de 24')
grid(ax,32,18,4,4,6,4,'fixe'); text(ax,44,38,'24 carreaux','encre','s')
line(ax,[(32,18),(32,34)],'autre',lw=2); text(ax,29,26,'4 : donné','autre','m',ha='right')
line(ax,[(32,18),(56,18)],'sujet',lw=2); brace(ax,32,56,16.5,'sujet',label='6 : manquant',size='m')
save(fig,'03-043')
