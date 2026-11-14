import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
c=3.0; x0=4; y0=8
for i in range(10):
    for j in range(10):
        r='fixe'; fl=False
        if i==3: r='sujet'; fl=True
        if i==3 and j==9: r='varie'
        ax.add_patch(Rectangle((x0+i*c,y0+j*c),c,c,ec=COL[r],fc=FILL[r] if fl else 'white',lw=0.4,zorder=2))
ax.add_patch(Rectangle((x0,y0),10*c,10*c,ec=COL['encre'],fc='none',lw=0.9,zorder=3))
text(ax,x0+15,y0-3.5,'carré = 1','encre','s')
text(ax,x0+15,y0+10*c+4,'10 colonnes','fixe','s')
zx=50; cz=3.6
for j in range(10):
    r='varie' if j==9 else 'sujet'
    ax.add_patch(Rectangle((zx,y0+j*cz),6,cz,ec=COL[r],fc=FILL[r],lw=0.5,zorder=2))
arrow(ax,(x0+4*c+1,y0+5*c),(zx-2,y0+5*cz),'fixe',curve=0.0)
text(ax,zx+3,y0+10*cz+4,'10 carreaux','fixe','s')
text(ax,zx+9,y0+8*cz+1.8,'carreau','varie','s',ha='left')
text(ax,zx+9,y0+8*cz-1.8,r'$1/100$','varie','s',ha='left')
text(ax,zx+9,y0+3*cz+1.8,'colonne','sujet','s',ha='left')
text(ax,zx+9,y0+3*cz-1.8,r'$1/10$','sujet','s',ha='left')
save(fig,'08-067')
