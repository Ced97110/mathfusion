import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
xl,wl,xr,wr,bh=2,38,48,38,9
ys=[46,28,10]
text(ax,xl+wl/2,60,'Divisions (de haut en bas)','fixe','m')
text(ax,xr+wr/2,60,'Remontée (de bas en haut)','varie','m')
left=['54 = 252 − 198','36 = 198 − 3 × 54','18 = 54 − 36']
right=['18 = 4 × 252 − 5 × 198','18 = 4 × 54 − 198','18 = 54 − 36']
rr=['resultat','varie','varie']
for y,l,r,ro in zip(ys,left,right,rr):
    box(ax,xl,y,wl,bh,'fixe',label=l)
    box(ax,xr,y,wr,bh,ro,label=r)
    arrow(ax,(xl+wl,y+bh/2),(xr,y+bh/2),'fixe')
cx=xr+wr/2
arrow(ax,(cx,ys[2]+bh),(cx,ys[1]),'varie')
arrow(ax,(cx,ys[1]+bh),(cx,ys[0]),'varie')
text(ax,cx+2,(ys[2]+bh+ys[1])/2,'on remplace 36','varie','s',ha='left')
text(ax,cx+2,(ys[1]+bh+ys[0])/2,'on remplace 54','varie','s',ha='left')
save(fig,'05-144')
