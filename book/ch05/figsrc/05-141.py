import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(80)
text(ax,44,75,'nombre ÷ diviseur → reste','encre','m')
rows=[('252','198','54'),('198','54','36'),('54','36','18'),('36','18','0')]
ys=[62,47,32,17]; w_=18
for n,(y,(a,b,r)) in enumerate(zip(ys,rows)):
    box(ax,6,y,w_,8,'sujet',label=a)
    box(ax,28,y,w_,8,'resultat' if n==3 else 'autre',label=b)
    box(ax,54,y,w_,8,'resultat' if n==2 else ('fixe' if n==3 else 'varie'),label=r)
    arrow(ax,(46.5,y+4),(53.5,y+4),'varie')
    if n<3:
        arrow(ax,(37,y-0.5),(15,y-6.5),'fixe'); arrow(ax,(63,y-0.5),(37,y-6.5),'fixe')
box(ax,16,3,56,8,'resultat',label='PGCD = 18, dernier reste ≠ 0')
save(fig,'05-141')
