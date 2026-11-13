import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import re
nb=lambda s: re.sub(r'(?<=\d) (?=\d)', ' ', s)

from matplotlib.patches import Circle
fig,ax=canvas(64)
line(ax,[(17,58),(86,58)],'fixe',lw=0.5); line(ax,[(17,52),(86,52)],'fixe',lw=0.5,dash=True); line(ax,[(17,46),(86,46)],'fixe',lw=0.5)
text(ax,9.5,52,'mi-hauteur','fixe','s')
def d3(x): 
    for p,q in [((x,58),(x+6,58)),((x+6,58),(x+6,52)),((x,52),(x+6,52)),((x+6,52),(x+6,46)),((x,46),(x+6,46))]: line(ax,[p,q],'encre',lw=1.6)
def d5(x):
    for p,q in [((x,58),(x+6,58)),((x,58),(x,52)),((x,52),(x+6,52)),((x+6,52),(x+6,46)),((x,46),(x+6,46))]: line(ax,[p,q],'encre',lw=1.6)
d3(19); d5(34); d3(56); d5(71)
ax.add_patch(Circle((29.5,52),0.9,fc=COL['sujet'],ec=COL['sujet'],zorder=4))
ax.add_patch(Circle((66.5,46.9),0.9,fc=COL['limite'],ec=COL['limite'],zorder=4))
text(ax,29.5,40,'3 ⋅ 5 : trois fois cinq','sujet','s'); text(ax,66.5,40,'point en bas : une virgule ?','limite','s')
text(ax,44,28,'3 × 5 = 3 ⋅ 5 = 15','resultat','l')
text(ax,20,16,r'3 × $x$','limite','l'); text(ax,20,9,'× et x se ressemblent','limite','s')
text(ax,66,16,r'3 ⋅ $x$','sujet','l'); text(ax,66,9,'le point : aucune lettre','sujet','s')
save(fig,'03-024')
