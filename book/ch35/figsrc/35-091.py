import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
c=(44,36)
line(ax,[(4,c[1]),(84,c[1])],'fixe',lw=0.6); line(ax,[(c[0],14),(c[0],58)],'fixe',lw=0.6)
for k in range(12):
    a=math.radians(15+30*k)
    line(ax,[(c[0]+10*math.cos(a),c[1]+10*math.sin(a)),(c[0]+20*math.cos(a),c[1]+20*math.sin(a))],'fixe',dash=True,lw=0.8)
disc(ax,c[0],c[1],1.6,'sujet')
text(ax,c[0],c[1]-5,'$O(0\\ ;\\ 0)$','sujet','s')
text(ax,44,61,'$a=0$ et $b=0$','encre','m')
text(ax,44,10,'quelle direction ?','limite','m')
text(ax,44,4.5,r'$R=0$ : $\alpha$ sans valeur','limite','s')
save(fig,'35-091')
