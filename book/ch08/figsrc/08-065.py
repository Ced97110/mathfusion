import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
c=3.0; x0=4; y0=5
for i in range(10):
    for j in range(10):
        r='fixe'; fl=False
        if i<2: r='sujet'; fl=True
        elif i==2 and j<5: r='varie'; fl=True
        ax.add_patch(Rectangle((x0+i*c,y0+j*c),c,c,ec=COL['fixe'] if not fl else COL[r],fc=FILL[r] if fl else 'white',lw=0.4,zorder=2))
ax.add_patch(Rectangle((x0,y0),10*c,10*c,ec=COL['encre'],fc='none',lw=0.9,zorder=3))
text(ax,x0+15,y0+10*c+4,'carré = 1','encre','s')
tx=42
text(ax,tx,36,'2 colonnes = 2 dixièmes','sujet','s',ha='left')
text(ax,tx,28,'5 carreaux = 5 centièmes','varie','s',ha='left')
text(ax,tx,18,'20 + 5 = 25 carreaux','encre','s',ha='left')
text(ax,tx,12,'sur 100 carreaux','encre','s',ha='left')
box(ax,tx,2.5,40,6,'resultat',label='0,25 = 25 centièmes',size='s')
save(fig,'08-065')
