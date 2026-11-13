import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
u=8
a=(30,44)
poly(ax,[a,(a[0]+3*u,a[1]),(a[0],a[1]+2*u)],'sujet')
line(ax,[(a[0]+2.4,a[1]),(a[0]+2.4,a[1]+2.4),(a[0],a[1]+2.4)],'encre',lw=0.7)
text(ax,a[0]+1.5*u,a[1]-3,'3','sujet','s'); text(ax,a[0]-3,a[1]+u,'2','sujet','s')
text(ax,66,a[1]+12,'$c=\\sqrt{13}$','resultat','m')
text(ax,66,a[1]+4,'$4+9=13$','sujet','s')
f=numberline(ax,10,78,14,12.9,13.1,step=0.1,arrow_right=False)
for v,lab,role,dy in [(12.96,'$3{,}6^2=12{,}96$','varie',7),(13.03,'$3{,}61^2\\approx13{,}03$','varie',7),(13,'$c^2=13$','resultat',15)]:
    x=f(v); line(ax,[(x,14),(x,14+dy-2)],role,lw=0.8)
    disc(ax,x,14,1.0,role)
    text(ax,x,14+dy,lab,role,'s')
save(fig,'22-136')
