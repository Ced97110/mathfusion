import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def grid(ax,x,y,cw,ch,nc,nr,role,fillrole=None,lw=0.4,fill=True,dash=False):
    for i in range(nc):
        for j in range(nr):
            ax.add_patch(Rectangle((x+i*cw,y+j*ch),cw,ch,ec=COL[role],fc=FILL[fillrole or role] if fill else "none",lw=lw,ls="--" if dash else "-",zorder=2))

fig,ax=canvas(80)
text(ax,24,74,r'$n$ ÷ $d$ = $q$','sujet','l'); arrow(ax,(38,74),(50,74),'fixe')
text(ax,66,74,r'$n$ = $d$ × $q$','sujet','l')
c=2.2
for (x,rows,cols,xc,yc,xr,yr),(n,d,q,cx) in zip([(8.4,4,6,15,41,6.9,34.4),(40.7,6,3,44,45.4,39.2,36.6),(66.4,15,6,73,65.4,65,46.5)],[(24,4,6,15),(18,6,3,44),(90,15,6,73)]):
    grid(ax,x,30,c,c,cols,rows,'varie')
    ax.add_patch(Rectangle((x,30),cols*c,rows*c,ec=COL['varie'],fc='none',lw=0.9,zorder=3))
    text(ax,xc,yc,str(cols),'varie','s'); text(ax,xr,yr,str(rows),'varie','s',ha='right')
    text(ax,cx,24,f'{n} ÷ {d} = {q}','encre','m'); text(ax,cx,17,f'{d} × {q} = {n}','resultat','m')
save(fig,'03-036')
