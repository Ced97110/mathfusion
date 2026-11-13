import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def grid(ax,x,y,cw,ch,nc,nr,role,fillrole=None,lw=0.4,fill=True,dash=False):
    for i in range(nc):
        for j in range(nr):
            ax.add_patch(Rectangle((x+i*cw,y+j*ch),cw,ch,ec=COL[role],fc=FILL[fillrole or role] if fill else "none",lw=lw,ls="--" if dash else "-",zorder=2))

fig,ax=canvas(76)
text(ax,38,68,'4 ×','encre','l',ha='right'); box(ax,40,64,8,8,'sujet'); text(ax,44,68,'q','sujet','l',weight='bold',style='italic')
text(ax,50,68,'= 24','encre','l',ha='left')
text(ax,44,59,'nom du nombre cherché','sujet','s')
arrow(ax,(44,56),(22,47),'varie'); arrow(ax,(44,56),(66,47),'varie')
text(ax,22,44,r'$q$ = 5','varie','m'); text(ax,66,44,r'$q$ = 6','varie','m')
grid(ax,11.5,22,3.5,3.5,5,4,'varie',lw=0.4); grid(ax,29,22,3.5,3.5,1,4,'limite',fill=False,dash=True,lw=0.8)
text(ax,22,16,'4 × 5 = 20','encre','m'); text(ax,22,10,'trop petit','limite','m')
grid(ax,55.5,22,3.5,3.5,6,4,'resultat',lw=0.4)
text(ax,66,16,'4 × 6 = 24','resultat','m'); text(ax,66,10,'juste','resultat','m')
save(fig,'03-042')
