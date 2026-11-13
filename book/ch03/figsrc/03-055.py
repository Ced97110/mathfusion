import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
def cell(x,y,fc,ec,ls='-',lw=0.5):
    ax.add_patch(Rectangle((x,y),5,6,fc=fc,ec=ec,lw=lw,ls=ls,zorder=2))
for i in range(14): cell(9+5*i,60,FILL['fixe'],COL['fixe'])
text(ax,44,71,r'$n$ = 14 objets','fixe','s')
for i in range(14):
    if i<12: cell(9+5*i,40,FILL['varie'],COL['varie'],ls='--')
    else: cell(9+5*i,40,FILL['sujet'],COL['sujet'])
for x in (29,49): line(ax,[(x,40),(x,46)],'varie',lw=1.8)
brace(ax,9,69,48,'varie',label=r'retirés : $d$ × $q$ = 4 × 3 = 12',down=False)
brace(ax,69,79,38,'sujet',label=r'reste $r$ = 2',down=True)
for x in (69,79): line(ax,[(x,60),(x,46)],'fixe',lw=0.5,dash=True)
text(ax,44,22,r'$r$ = $n$ − $d$ × $q$','sujet','l')
text(ax,44,12,'2 = 14 − 12','resultat','l')
text(ax,44,4,'le reste est une différence','encre','s')
save(fig,'03-055')
