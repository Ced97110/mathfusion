import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
def loop(x,y,role):
    arrow(ax,(x-2,y+2.3),(x+2,y+2.3),role,curve=-2.2,lw=0.9)
# left: bad rule
text(ax,22,56,'tout va sur le 1er point','limite','s')
disc(ax,12,30,3,'limite'); disc(ax,32,30,3,'limite')
text(ax,12,22,'1er point','fixe','s'); text(ax,32,22,'2e point','fixe','s')
arrow(ax,(28.8,32),(15.2,32),'limite',curve=0.5)
text(ax,22,42,r'$1$ le déplace','limite','s')
# right: good condition
text(ax,66,56,r'$1x=x$','resultat','m')
disc(ax,56,30,3,'resultat'); disc(ax,76,30,3,'resultat')
text(ax,56,22,'1er point','fixe','s'); text(ax,76,22,'2e point','fixe','s')
loop(56,30,'resultat'); loop(76,30,'resultat')
text(ax,66,42,r'$1$ ne bouge rien','resultat','s')
line(ax,[(44,14),(44,52)],'fixe',dash=True)
save(fig,'49-095')
