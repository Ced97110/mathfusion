import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
cx,cy,R=44,38,22
prim={1,5,7,11}
for k in range(12):
    a=2*math.pi*k/12; x,y=cx+R*math.cos(a),cy+R*math.sin(a)
    r='sujet' if k in prim else 'fixe'
    disc(ax,x,y,2.6,r)
    text(ax,cx+(R+6.5)*math.cos(a),cy+(R+6.5)*math.sin(a),str(k),r,'s')
text(ax,cx,cy,r'$\omega^{k}$','encre','l')
text(ax,44,3.5,r'4 primitives : $\varphi(12)=4$','sujet','s')
save(fig,'46-285')
