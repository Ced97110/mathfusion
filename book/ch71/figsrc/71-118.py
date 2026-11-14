import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
u=80/37; x0=4
xs=[x0,x0+5*u,x0+21*u,x0+37*u]
brace(ax,xs[0]+0.3,xs[3]-0.3,46,'encre',r'$Q(x+y)=37$',down=False)
for i,(role,lab) in enumerate([('sujet','5'),('autre','16'),('varie','16')]):
    box(ax,xs[i],36,xs[i+1]-xs[i],8,role,label=lab,size='m',r=0.3)
text(ax,(xs[0]+xs[1])/2,32,r'$Q(x)$','sujet','s'); text(ax,(xs[1]+xs[2])/2,32,r'$Q(y)$','autre','s'); text(ax,(xs[2]+xs[3])/2,32,'reste','varie','s')
m=(xs[2]+xs[3])/2
line(ax,[(xs[2],28),(xs[2],26)],'varie',dash=True); line(ax,[(xs[3],28),(xs[3],26)],'varie',dash=True)
box(ax,xs[2],16,m-xs[2],8,'fixe',label='8',r=0.3); box(ax,m,16,xs[3]-m,8,'resultat',label='8',r=0.3)
text(ax,m,10,r'moitié $=B(x,y)$','resultat','m')
save(fig,'71-118')
