import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
def bx(x,y,ec,fc,lab,lw=0.8):
    ax.add_patch(FancyBboxPatch((x+.8,y+.8),12.4,8.4,boxstyle='round,pad=0.8',lw=lw,ec=COL[ec],fc=FILL[fc],zorder=2))
    text(ax,x+7,y+5,lab,'encre' if ec=='limite' else ec,'l')
for x,l in ((13,'centaines'),(27,'dizaines'),(41,'unités')): text(ax,x,58,l,'encre','s')
bx(6,42,'sujet','sujet','5'); bx(20,42,'limite','sujet','0',1.4); bx(34,42,'limite','sujet','3',1.4)
disc(ax,13,42,1.6,'varie'); arrow(ax,(14.5,41),(26,34.6),'varie'); arrow(ax,(8,41.2),(8,34.8),'fixe',lw=0.7); arrow(ax,(46,41.2),(46,34.8),'fixe',lw=0.7); text(ax,68,38,'1 centaine → 10 dizaines','varie','s')
bx(6,24,'varie','varie','4'); bx(20,24,'varie','varie','10'); bx(34,24,'sujet','sujet','3')
disc(ax,31,24,1.6,'varie'); arrow(ax,(32.2,22.8),(40.5,16.6),'varie'); arrow(ax,(22,23.2),(22,16.8),'resultat',lw=0.9); arrow(ax,(8,23.2),(8,16.8),'fixe',lw=0.7); text(ax,68,20,'1 dizaine → 10 unités','varie','s')
bx(6,6,'resultat','resultat','4'); bx(20,6,'resultat','resultat','9',1.4); bx(34,6,'resultat','resultat','13')
save(fig,'02-055')
