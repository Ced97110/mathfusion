import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ln(ax,cx,cy,m,r,role,lw=1.0,dash=False):
    if m is None: pts=[(cx,cy-r),(cx,cy+r)]
    else:
        d=r/max(1,abs(m)); pts=[(cx-d,cy-m*d),(cx+d,cy+m*d)]
    line(ax,pts,role,lw,dash)
def axes(ax,cx,cy,r):
    line(ax,[(cx-r,cy),(cx+r,cy)],'fixe',0.5); line(ax,[(cx,cy-r),(cx,cy+r)],'fixe',0.5)
def lab(ax,x,y,s,role='encre',size='s'):
    t=text(ax,x,y,s,role,size); t.set_bbox(dict(fc='white',ec='none',pad=0.6)); return t

fig,ax=canvas(66)
X=(20,46,72); R=['sujet','autre','fixe']
for i in range(3):
    disc(ax,X[i],52,6,R[i],label=r'$P_%d$'%i,size='m')
sw=[1,0,2]
for i in range(3):
    disc(ax,X[i],14,6,R[sw[i]],label=r'$P_%d$'%sw[i],size='m')
arrow(ax,(X[0]+1,45.8),(X[1]-1,20.2),'varie',1.2); arrow(ax,(X[1]-1,45.8),(X[0]+1,20.2),'varie',1.2)
arrow(ax,(X[2],45.5),(X[2],20.5),'fixe',1.0)
text(ax,1.5,60,'avant','encre','s',ha='left'); text(ax,1.5,6,'après','encre','s',ha='left')
text(ax,80,33,r'$P_2$ reste','fixe','s',ha='center')
text(ax,46,3,'paires : mêmes relations','resultat','s')
save(fig,'80-306')
