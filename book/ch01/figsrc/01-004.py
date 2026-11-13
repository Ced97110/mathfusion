import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
def wmm(t):
    r=fig.canvas.get_renderer(); return t.get_window_extent(r).width/fig.dpi*25.4
line(ax,[(40,6),(40,54)],'fixe')
text(ax,21,52,'En chiffres','autre','m'); text(ax,64,52,'En lettres romaines','sujet','m')
# colonnes (centres des chiffres, police à chasse égale des chiffres)
for cx in (28.99,25.96,22.93,19.90):
    ax.add_patch(Rectangle((cx-1.3,23),2.6,22,fc=FILL['fixe'],ec='none',zorder=1))
text(ax,30,42,'4 3 2 9','autre','l',ha='right')
text(ax,30,35,'+ 1 0','varie','l',ha='right')
line(ax,[(14,31),(31,31)],'fixe')
text(ax,30,26,'4 3 3 9','autre','l',ha='right',weight='bold')
text(ax,21,14,'on pose en colonnes','resultat','s')
# lettres
text(ax,84,42,'MMMMCCCXXIX','sujet','l',ha='right')
text(ax,84,35,'+ X','varie','l',ha='right')
line(ax,[(54,31),(85,31)],'fixe')
d=0.707
line(ax,[(76-d,35-d),(76+d,35+d)],'limite',lw=1.1); line(ax,[(76-d,35+d),(76+d,35-d)],'limite',lw=1.1)
t1=text(ax,84,26,'IX','sujet','l',ha='right')
x1=84-wmm(t1)
t2=text(ax,x1,26,'X','varie','l',ha='right',weight='bold')
x2=x1-wmm(t2)
text(ax,x2,26,'MMMMCCCXX','sujet','l',ha='right')
arrow(ax,(83,33.5),(x1-wmm(t2)/2,28.2),'varie',curve=0.4)
text(ax,66,14,'on réécrit les lettres','limite','s')
save(fig,'01-004')
