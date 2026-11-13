import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def mw(s, size='l', weight='normal'):
    t=fig.text(0,0,s,fontsize=SIZE[size],fontweight=weight)
    w=t.get_window_extent(fig.canvas.get_renderer()).width
    t.remove(); return w*25.4/fig.dpi
# ligne du haut : deux parenthèses
text(ax,12,52,'10 +','encre','l')
text(ax,20,52,'(','autre','l',weight='bold')
text(ax,28,52,'30 −','encre','l')
text(ax,42,52,'(2 × 9)','encre','l')
text(ax,51,52,')','autre','l',weight='bold')
line(ax,[(47.5,49.5),(52,49.5)],'autre',lw=0.8)
text(ax,44,43,'deux ) voisines : compter','autre','s')
# ligne du bas : crochets pour le niveau extérieur
text(ax,12,28,'10 +','encre','l')
text(ax,20,28,'[','sujet','l',weight='bold')
text(ax,28,28,'30 −','encre','l')
text(ax,42,28,'(2 × 9)','encre','l')
text(ax,51,28,']','sujet','l',weight='bold')
box(ax,18,23.5,35,9,'sujet',fill=False)
Wq=mw('(2 × 9)')
box(ax,42-Wq/2-1.6,25,Wq+3.2,6.5,'fixe',fill=False)
text(ax,36,15,'[ ] dehors, ( ) dedans','fixe','s')
# résultats
text(ax,68,52,'= 22','resultat','l')
text(ax,68,28,'= 22','resultat','l')
save(fig,'04-050')
