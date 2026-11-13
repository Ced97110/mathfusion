import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cell(ax,x,y,w,h,role,fill=True,lw=0.6): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=lw,zorder=2))
fig,ax=canvas(66)
for i in range(5):
    for j in range(3): cell(ax,18+i*10,28+j*7,10,7,'sujet')
for j in range(3): text(ax,10,28+j*7+3.5,f'{j+1}','encre','s')
text(ax,10,53,'personne','fixe','s')
brace(ax,18,68,50,'sujet',label='5 tablettes',down=False)
text(ax,78,38.5,'5 tiers','resultat','s')
text(ax,43,22,'15 parts en tout','fixe','s')
box(ax,6,5,76,10,'limite',label=r'$3 \div 0$ : aucun résultat')
save(fig,'06-066')
