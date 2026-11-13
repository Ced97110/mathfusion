import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
def mw(s, size='l', weight='normal'):
    t=fig.text(0,0,s,fontsize=SIZE[size],fontweight=weight)
    w=t.get_window_extent(fig.canvas.get_renderer()).width
    t.remove(); return w*25.4/fig.dpi
# étape 0 : état de départ, le groupement intérieur repéré
spw=mw('a a')-mw('aa')    # largeur d'une espace
A0='10 + [30 −'; B0='(2 × 9)'; C0=']'
WA=mw(A0); WB=mw(B0); WC=mw(C0)
L0=30-(WA+spw+WB+WC+0.6)/2
xB=L0+WA+spw
text(ax,L0,80,A0,'encre','l',ha='left')
text(ax,xB,80,B0,'encre','l',ha='left')
text(ax,xB+WB+0.6,80,C0,'encre','l',ha='left')
box(ax,xB-0.9,76,WB+1.5,8,'varie',fill=False)
text(ax,73,80,'2 groupements','fixe','s')
# étape 1
arrow(ax,(30,75),(30,65),'varie')
text(ax,48,70,'2 × 9 = 18','varie','s')
full1='10 + [30 − 18]'
W1=mw(full1); L1=30-W1/2
S1=L1+W1-mw('[30 − 18]')  # début de « [30 − 18] »
E1=L1+W1
text(ax,30,60,full1,'encre','l')
box(ax,S1-0.8,56,E1-S1+1.6,8,'varie',fill=False)
text(ax,73,60,'1 groupement','fixe','s')
# étape 2
arrow(ax,(30,55),(30,45),'varie')
text(ax,48,50,'30 − 18 = 12','varie','s')
text(ax,30,40,'10 + 12','encre','l')
text(ax,69,40,'aucun groupement : arrêt','fixe','s')
# étape 3
arrow(ax,(30,35),(30,25),'varie')
text(ax,48,30,'10 + 12 = 22','varie','s')
text(ax,30,18,'22','resultat','l',weight='bold')
save(fig,'04-054')
