import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(62)
o=(44,8)
line(ax,[(4,32),(84,32)],'fixe',lw=0.9,dash=True)
line(ax,[(4,8),(84,8)],'autre',lw=2.0)
for dx in (-14,0,14):
    line(ax,[o,(o[0]+2*dx,56)],'sujet',lw=1.6)
    disc(ax,o[0]+dx,32,1.5,'resultat')
disc(ax,o[0],o[1],1.2,'encre')
text(ax,14,36,'écran z = 1','fixe','s')
text(ax,70,26.5,'point ordinaire','resultat','s')
text(ax,16,13,'à l’infini : z = 0','autre','s')
save(fig,'80-091')
