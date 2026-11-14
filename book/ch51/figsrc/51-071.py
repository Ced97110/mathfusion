import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
cx,cy,s=30,32,9
box(ax,cx-24,cy-3.2,70,6.4,'fixe',r=1.5,lw=0.6)
arrow(ax,(cx-24,cy),(cx+44,cy),'fixe',lw=0.8); arrow(ax,(cx,cy-24),(cx,cy+26),'fixe',lw=0.8)
for m in range(-2,3):
    for n in range(-2,3):
        if (m,n)==(1,1): continue
        disc(ax,cx+m*s,cy+n*s,1.0 if n==0 else 0.9,'fixe' if n==0 else 'sujet')
line(ax,[(cx+s,cy),(cx+s,cy+s)],'varie',lw=1.0,dash=True)
disc(ax,cx+s,cy+s,1.7,'sujet')
text(ax,cx+s+3,cy+s+3.5,r'$1+1\sqrt{-1}$','sujet','s',ha='left',weight='bold')
text(ax,cx+s+2,cy+s/2,r'$n=1$','varie','s',ha='left')
text(ax,cx+s,cy-6,r'$m=1$','fixe','s')
text(ax,cx+43,cy-4,r'$m$','fixe','s'); text(ax,cx+3,cy+27,r'$n\sqrt{-1}$','varie','s',ha='left')
text(ax,cx-23,cy+6.5,r'$\mathbb{Z}$ : $n=0$','fixe','s',ha='left',weight='bold')
save(fig,'51-071')
