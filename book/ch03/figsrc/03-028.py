import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import re
nb=lambda s: re.sub(r'(?<=\d) (?=\d)', ' ', s)

from matplotlib.patches import Rectangle
fig,ax=canvas(80)
text(ax,44,75,nb('326 × 48 = 15 648'),'encre','m')
def band(y,cut,l1,l2,t1,t2,sumtxt,ysum):
    for a,b in [(6,cut),(cut,82)]:
        ax.add_patch(Rectangle((a,y),b-a,10,fc=FILL['sujet'],ec=COL['sujet'],lw=0.8,zorder=2))
    text(ax,(6+cut)/2,y+5,l1,'sujet','s'); text(ax,(cut+82)/2,y+5,l2,'sujet','s')
    text(ax,(6+cut)/2,y+13.5,t1,'varie','s'); text(ax,(cut+82)/2,y+13.5,t2,'varie','s')
    line(ax,[(cut,y-1),(cut,y+11)],'varie',lw=1.6,dash=True)
    text(ax,44,ysum,nb(sumtxt),'resultat','s')
u=76/48
band(52,6+40*u,'326 × 40','326 × 8','40','8','13 040 + 2 608 = 15 648',47.5)
band(25,6+30*u,'326 × 30','326 × 18','30','18','9 780 + 5 868 = 15 648',20.5)
text(ax,44,10,"la raison n'est pas montrée",'limite','s')
save(fig,'03-028')
