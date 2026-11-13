import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(62)
ox,oy=44,30
line(ax,[(8,oy),(80,oy)],'sujet',lw=1.8)
line(ax,[(ox,5),(ox,55)],'resultat',lw=1.8)
line(ax,[(ox-14,oy-18.2),(ox+14,oy+18.2)],'resultat',lw=1.8)
disc(ax,ox,oy,1.3,'encre')
text(ax,70,oy-3.6,'axe horizontal','sujet','s')
text(ax,ox,58.5,'axe vertical','resultat','s')
text(ax,ox+15,oy+21,'droite oblique','resultat','s',ha='left')
text(ax,ox-6,oy-3.6,'origine','encre','s',ha='right')
text(ax,3,58.5,'compléments :','resultat','s',ha='left')
save(fig,'80-073')
