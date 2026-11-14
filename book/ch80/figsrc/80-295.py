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
for k in range(3):
    x0=8+k*27
    for i in range(3):
        for j in range(3):
            box(ax,x0+i*7.6,26+j*7.6,7,7,'fixe' if (k,i,j)==(0,0,0) else 'sujet',r=0.5)
    text(ax,x0+10.7,21,r'$z=%d$'%k,'encre','s')
text(ax,35.5,58,r'$3\times3\times3=27$ vecteurs','encre','m')
text(ax,14,10,'nul : (0, 0, 0)','fixe','s'); arrow(ax,(9,13),(11.5,25.5),'fixe',0.8)
text(ax,64,10,r'$27-1=26$ non nuls','resultat','m')
save(fig,'80-295')
