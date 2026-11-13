import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
cx,cy,u=22,34,15
disc(ax,cx,cy,u,'sujet')
def sq(s,role,lw=1.2,dash=False): ax.add_patch(Rectangle((cx-s/2,cy-s/2),s,s,ec=COL[role],fc='none',lw=lw,ls='--' if dash else '-',zorder=3))
sq(u,'limite'); sq(2*u,'limite'); sq(1.7725*u,'resultat',lw=1.8)
c=1.7725*u; yb=cy-u-4
arrow(ax,(cx-c/2,yb),(cx+c/2,yb),'resultat',both=True); text(ax,cx,yb-3.5,'côté $c$','resultat','s')
rows=((58,'cercle de rayon 1 cm','aire ≈ 3,14 cm²','sujet'),(47,'carré de côté 1 cm','aire 1 : trop petit','limite'),(36,'carré de côté 2 cm','aire 4 : trop grand','limite'),(25,'carré de même aire :','côté $c$ entre 1 et 2','resultat'))
for y,a,b,r in rows:
    text(ax,48,y,a,r,'s',ha='left'); text(ax,48,y-4,b,r,'s',ha='left')
save(fig,'61-010')
