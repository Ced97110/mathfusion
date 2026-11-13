import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *

fig,ax=canvas(70)
# forme unique
box(ax,4,60,10,8,'sujet',label=r'$a$',size='l')
text(ax,24,64,'fois 6','fixe','m')
text(ax,34,64,'une seule forme','sujet','s',ha='left')
# flèche de remplacement
arrow(ax,(9,59.5),(9,48),'varie',lw=0.9)
text(ax,12,53,r'remplacer $a$ par un nombre','varie','s',ha='left')
# trois cas : 4, 7, 426
for y,n in ((44,'4'),(30,'7'),(16,'426')):
    box(ax,4,y-3.5,10,7,'varie',label=n,size='m')
    text(ax,24,y,'fois 6','fixe','m')

def bar(x0,yc,n_units,role,w=4.8,h=3):
    poly(ax,[(x0,yc-h/2),(x0+w,yc-h/2),(x0+w,yc+h/2),(x0,yc+h/2)],role,lw=0.6)

# chaque barre grise = un 6
for i in range(4): bar(32+6*i,44,1,'fixe')
for i in range(7): bar(32+6*i,30,1,'fixe')
for i in range(7): bar(32+6*i,16,1,'fixe')
for x in (75,77,79): ax.add_patch(Circle((x,16),0.45,fc=COL['encre'],ec=COL['encre'],lw=0.3,zorder=3))
bar(81,16,1,'fixe')
save(fig,'03-016')
