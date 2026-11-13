import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def cell(ax,x,y,w,h,role,fill=True,lw=0.6): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=lw,zorder=2))
fig,ax=canvas(70)
y=36
f=numberline(ax,8,68,y,0,3,arrow_right=False)
disc(ax,f(0.75),y,1.6,'sujet'); text(ax,f(0.75),y+5,r'$3/4$','sujet','m')
disc(ax,f(3),y,1.6,'resultat'); text(ax,f(3),y+5,'3','resultat','m')
arrow(ax,(f(0.75)+2,y+9),(f(3)-2,y+9),'varie',curve=-0.35)
text(ax,f(1.9),y+19,r'$\div\, 1/4$','varie','m')
for i in range(3): cell(ax,8+i*5,12,5,7,'sujet')
text(ax,28,15.5,r'3 briques de $1/4$','sujet','s',ha='left')
text(ax,44,4,r'$3 > 3/4$','resultat','m',weight='bold')
save(fig,'06-079')
