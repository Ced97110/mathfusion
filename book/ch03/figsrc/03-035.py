import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def grid(ax,x,y,cw,ch,nc,nr,role,fillrole=None,lw=0.4,fill=True,dash=False):
    for i in range(nc):
        for j in range(nr):
            ax.add_patch(Rectangle((x+i*cw,y+j*ch),cw,ch,ec=COL[role],fc=FILL[fillrole or role] if fill else "none",lw=lw,ls="--" if dash else "-",zorder=2))

fig,ax=canvas(90)
text(ax,2,86,'défaire une addition','encre','s',ha='left')
grid(ax,20,70,5,5,4,1,'fixe'); grid(ax,40,70,5,5,5,1,'varie')
brace(ax,20,65,76.5,'fixe',label='9 en tout',down=False)
brace(ax,20,40,68.5,'fixe',label='4')
brace(ax,40,65,68.5,'varie',label='? = 5')
text(ax,77,76,'4 + 5 = 9','encre','m'); text(ax,77,70,'9 − 4 = 5','encre','m')
text(ax,2,46,'défaire une multiplication','encre','s',ha='left')
grid(ax,20,14,5,5,6,3,'fixe'); grid(ax,20,29,5,5,6,1,'varie')
brace(ax,20,50,35.5,'varie',label='? = 6 par rangée',down=False)
text(ax,2,24,'4 rangées','encre','s',ha='left'); text(ax,35,10,'24 carreaux en tout','encre','s')
text(ax,71,30,'4 × 6 = 24','encre','m'); arrow(ax,(71,27),(71,23),'varie')
text(ax,71,20,'24 ÷ 4 = 6','resultat','l'); text(ax,71,10,'d ≠ 0 (ici d = 4)','limite','m')
save(fig,'03-035')
