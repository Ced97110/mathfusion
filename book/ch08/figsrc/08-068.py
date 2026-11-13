import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
xs=[4,33,62]; bw=22
for x,l in zip(xs,['unités','dixièmes','centièmes']):
    box(ax,x,48,bw,8,'sujet' if x==4 else 'varie' if x==33 else 'autre',label=l,size='s')
for a in (4,33):
    arrow(ax,(a+bw+0.5,52),(a+29-0.5+0.0,52),'fixe'); text(ax,a+bw+3.5,55.2,r'$\div 10$','fixe','s')
text(ax,44,60.5,'écrit : places du nombre','encre','s')
text(ax,44,38,'dessiné : aires','encre','s')
cx=[15,44,73]; y=12; s=20
ax.add_patch(Rectangle((cx[0]-s/2,y),s,s,ec=COL['sujet'],fc=FILL['sujet'],lw=0.8,zorder=2))
ax.add_patch(Rectangle((cx[1]-s/20,y),s/10,s,ec=COL['varie'],fc=FILL['varie'],lw=0.8,zorder=2))
ax.add_patch(Rectangle((cx[2]-s/20,y),s/10,s/10,ec=COL['autre'],fc=FILL['autre'],lw=0.8,zorder=2))
for a,b in ((cx[0]+s/2+1,cx[1]-3),(cx[1]+3,cx[2]-3)):
    arrow(ax,(a,y+s/2),(b,y+s/2),'fixe')
text(ax,29.5,y+s/2+3,r'$\div 10$','fixe','s'); text(ax,58.5,y+s/2+3,r'$\div 10$','fixe','s')
for x,l,r in zip(cx,['1',r'$1/10$',r'$1/100$'],['sujet','varie','autre']):
    text(ax,x,y-4,l,r,'s')
save(fig,'08-068')
