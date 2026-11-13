import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
s=78/120; x=lambda v:4+v*s
yA,yB=42,22
text(ax,44,57,'PPCM = 8 × 15 = 120','resultat','l')
text(ax,2,48.5,'bus toutes les 8 min','sujet','m',ha='left')
line(ax,[(x(0),yA),(x(120),yA)],'fixe'); line(ax,[(x(0),yB),(x(120),yB)],'fixe')
for v in range(0,121,8): disc(ax,x(v),yA,1.1,'sujet')
for v in range(0,121,15): disc(ax,x(v),yB,1.3,'autre')
disc(ax,x(120),yA,1.8,'resultat'); disc(ax,x(120),yB,1.8,'resultat')
line(ax,[(x(120),yB+2),(x(120),yA-2)],'resultat',dash=True)
line(ax,[(x(0),yB+2),(x(0),yA-2)],'fixe',dash=True)
text(ax,x(0)+1,32,'0','encre','s',ha='left'); text(ax,x(120)-1.5,32,'120','resultat','s',ha='right')
text(ax,44,32,'premier passage commun','resultat','s')
text(ax,2,15,'bus toutes les 15 min','autre','m',ha='left')
text(ax,44,6,'PGCD(8, 15) = 1','encre','m')
save(fig,'05-159')
