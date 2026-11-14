import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
f=lambda v: 8+v*70/12; y=24
line(ax,[(f(0),y),(f(12),y)],'fixe')
for v in range(13): ax.plot([f(v)]*2,[y-1,y+1],color=COL['fixe'],lw=0.7,zorder=1.5)
for v in (0,4,8,12):
    disc(ax,f(v),y,2.4,'resultat'); text(ax,f(v),y-6,str(v),'resultat','s')
for v in (6,10):
    disc(ax,f(v),y,2.4,'limite'); text(ax,f(v),y-6,rf'${v}\to2$','limite','s')
for a,b in ((0,4),(4,8),(8,12)): arrow(ax,(f(a),y+3),(f(b),y+3),'varie',curve=-0.5)
text(ax,f(6),y+13,r'pas de $r=4$','varie','s')
box(ax,3,1,4,3.2,'resultat',lw=0.6,r=0.4); text(ax,9,2.6,r'$k\times1$ donne 0','encre','s',ha='left')
box(ax,47,1,4,3.2,'limite',lw=0.6,r=0.4); text(ax,53,2.6,'ne donne pas 0','encre','s',ha='left')
save(fig,'45-179')
