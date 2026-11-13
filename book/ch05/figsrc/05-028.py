import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
text(ax,44,58,'$b$ : la taille d’un tas','sujet','l')
for x,n,w in ((4,5,20),(30,7,28)):
    box(ax,x,28,w,10,'sujet')
    for j in range(n): disc(ax,x+w/2+(j-(n-1)/2)*3.6,33,1.3,'sujet')
    arrow(ax,(44,54),(x+w/2,39.5),'sujet')
    text(ax,x+w/2,24,rf'$b={n}$','sujet','m')
box(ax,64,28,16,10,'limite',dash=True)
line(ax,[(68,30),(76,36)],'limite',lw=1.2); line(ax,[(68,36),(76,30)],'limite',lw=1.2)
text(ax,72,24,r'$b=0$','limite','m')
text(ax,44,10,r'$b\neq 0$ : jamais de tas vide','limite','m')
save(fig,'05-028')
