import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(92)
cx,cy,R=30,62,26
for deg in [20,70,110,160]:
    t=math.radians(deg); line(ax,[(cx-R*math.cos(t),cy-R*math.sin(t)),(cx+R*math.cos(t),cy+R*math.sin(t))],'fixe',lw=0.7)
line(ax,[(cx-R,cy),(cx+R,cy)],'sujet',lw=1.4); t=math.radians(45); line(ax,[(cx-R*math.cos(t),cy-R*math.sin(t)),(cx+R*math.cos(t),cy+R*math.sin(t))],'varie',lw=1.4)
arrow(ax,(cx+17,cy+2),(cx+12,cy+13),'resultat',curve=0.4,both=True)
text(ax,cx-R,cy-4,'pente 0','sujet','s',ha='left'); text(ax,cx+20,cy+22,'pente 1','varie','s',ha='left')
text(ax,70,82,'plan réel','fixe','s'); text(ax,70,70,'autres droites','fixe','s'); text(ax,70,63,'inchangées','fixe','s')
t=text(ax,cx+25,cy+8,'échange','resultat','s'); t.set_bbox(dict(fc='white',ec='none',pad=0.6))
box(ax,2,20,84,10,'resultat',label='échange : isomorphisme de treillis',size='s')
box(ax,2,5,84,10,'limite',label='application semi-linéaire : non',size='s')
save(fig,'80-110')
