import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
xs=[2.5,25.5,48.5,71.5]; S=15
coin=[0,0,1,3]  # place index of coin 1 (0=tl,1=tr,2=br,3=bl)
def pl(x,y): return [(x+1.5,y+S-1.5),(x+S-1.5,y+S-1.5),(x+S-1.5,y+1.5),(x+1.5,y+1.5)]
def square(x,y,c,numbered=False):
    poly(ax,[(x,y),(x+S,y),(x+S,y+S),(x,y+S)],'fixe')
    pts=pl(x,y)
    for i,p in enumerate(pts):
        if numbered: disc(ax,p[0],p[1],2.1,'sujet' if i==c else 'fixe',label=str(i+1),size='s')
        elif i!=c: disc(ax,p[0],p[1],0.9,'fixe')
    if not numbered: disc(ax,pts[c][0],pts[c][1],2.1,'sujet',label='1',size='s')
    return pts
Y=36
for k,x in enumerate(xs):
    pts=square(x,Y,coin[k],numbered=(k==0))
    if k==0: line(ax,[pts[0],pts[2]],'fixe',dash=True)
for k,s in enumerate([r'$s$',r'$r$',r'$s$']):
    arrow(ax,(xs[k]+S+0.8,Y+7.5),(xs[k+1]-0.8,Y+7.5),'varie',lw=1.6); text(ax,xs[k]+S+4,Y+11.5,s,'varie','l',weight='bold')
    text(ax,xs[k]+S+4,Y+3.5,str(k+1),'fixe','s')
text(ax,16,29,'axe de $s$ : 1 et 3','fixe','s')
pts=pl(xs[3],Y)
ax.add_patch(Circle(pts[3],2.4,ec=COL['resultat'],fc='none',lw=1.0,zorder=3))
# bottom: quarter turn the other way, same result
square(xs[2],6,0,numbered=False)
b=square(xs[3],6,3,numbered=False)
ax.add_patch(Circle(b[3],2.4,ec=COL['resultat'],fc='none',lw=1.0,zorder=3))
arrow(ax,(xs[2]+S+0.8,13.5),(xs[3]-0.8,13.5),'varie',lw=1.6)
text(ax,xs[2]+S+4,18.5,r'$r^{-1}$','varie','l',weight='bold')
text(ax,2.5,13.5,'quart de tour inverse','fixe','s',ha='left')
text(ax,79,28.5,'$=$','resultat','xl',weight='bold')
text(ax,62,28.5,r'$s\,r\,s=r^{-1}$','resultat','m',ha='right')
save(fig,'49-004')
