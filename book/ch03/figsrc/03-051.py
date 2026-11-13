import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(75)
def solid(x,y,r,role):
    ax.add_patch(Circle((x,y),r,fc=COL[role],ec=COL[role],lw=0.5,zorder=3))
box(ax,4,30,80,36,'fixe',fill=False,dash=True,lw=0.6)
text(ax,44,61,r'$n$ = 14 points','fixe','m')
for x0 in (8,23,38):
    box(ax,x0,42,11,11,'resultat')
    for dx,y in [(3,45),(8,45),(3,50),(8,50)]: solid(x0+dx,y,1.3,'sujet')
brace(ax,8,49,40,'resultat',label=r'$q$ = 3 boîtes de $d$ = 4',down=True)
box(ax,58,42,11,11,'varie',fill=False,dash=True,lw=0.8)
for x in (61,66): solid(x,45,1.3,'varie')
for x in (61,66):
    ax.add_patch(Circle((x,50),1.3,fc='none',ec=COL['limite'],lw=0.7,ls='--',zorder=3))
text(ax,68,70.5,r'manque 2 pour une 4$^{\mathrm{e}}$ boîte','limite','s')
brace(ax,58,69,40,'varie',label=r'$r$ = 2 < $d$ = 4',down=True)
text(ax,30,20,'14 =','fixe','l'); text(ax,42,20,'4 × 3','resultat','l'); text(ax,53,20,'+ 2','varie','l')
text(ax,30,13,r'$n$','fixe','s'); text(ax,42,13,r'$d$ × $q$','resultat','s'); text(ax,53,13,r'+ $r$','varie','s')
save(fig,'03-051')
