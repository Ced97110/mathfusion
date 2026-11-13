import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
def grid(x0):
    for i in range(6):
        for j in range(4):
            ax.add_patch(Rectangle((x0+4.5*i,30+4.5*j),4.5,4.5,fc=FILL['sujet'],ec=COL['sujet'],lw=0.4,zorder=2))
grid(10); grid(52)
text(ax,23.5,52,'aire : 24 carreaux','sujet','s'); text(ax,65.5,52,'aire : 24 carreaux','sujet','s')
text(ax,6,39,'4','fixe','m')
brace(ax,52,79,28,'fixe',label='6',down=True)
ax.add_patch(Rectangle((10,43.5),27,4.5,fill=False,ec=COL['varie'],lw=1.6,zorder=3))
brace(ax,10,37,28,'varie',label='largeur ?',down=True)
ax.add_patch(Rectangle((52,30),4.5,18,fill=False,ec=COL['varie'],lw=1.6,zorder=3))
line(ax,[(81,30),(81,48)],'varie',lw=1.0); line(ax,[(80,30),(82,30)],'varie',lw=1.0); line(ax,[(80,48),(82,48)],'varie',lw=1.0)
text(ax,84.5,39,'?','varie','m')
text(ax,23.5,14,'24 ÷ 4 = 6','resultat','l'); text(ax,65.5,14,'24 ÷ 6 = 4','resultat','l')
text(ax,23.5,62,'largeur cherchée','varie','s'); text(ax,65.5,62,'hauteur cherchée','varie','s')
save(fig,'03-049')
