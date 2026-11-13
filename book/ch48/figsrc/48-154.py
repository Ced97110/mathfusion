import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(96)
cx,cy,R=26,52,20
disc(ax,cx,cy,R,'fixe',fill=False)
text(ax,cx,cy,r'$\mathbb{T}$','fixe','l')
lx=72
line(ax,[(lx,10),(lx,80)],'fixe')
def Y(d): return 10+70*d/405
pairs=[('sujet',(0,360)),('varie',(45,405))]
pts={'sujet':0,'varie':45}
for role,ds in pairs:
    a=math.radians(pts[role]); px=cx+R*math.cos(a); py=cy+R*math.sin(a)
    disc(ax,px,py,2.2,role)
    for d in ds:
        disc(ax,lx,Y(d),2,role); text(ax,lx+4,Y(d),f'{d}°',role,'s',ha='left')
        arrow(ax,(lx-3,Y(d)),(px+2.4*math.cos(a)+0.5,py+2.4*math.sin(a)+0.3),role,curve=0.0)
text(ax,cx+15,cy,'1','sujet','s')
text(ax,cx+9,cy+11,'45°','varie','s')
text(ax,lx,87,'un tour de ℝ','fixe','s')
text(ax,cx,26,'même couleur : même point','fixe','s')
text(ax,cx,10,r'$\mathbb{R}/2\pi\mathbb{Z}\cong\mathbb{T}$','resultat','l')
save(fig,'48-154')
