import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,44,74,'9797 : on essaie les premiers','encre','m')
n=25; w=3.0; p=3.4; x0=(88-(n*p-(p-w)))/2
for i in range(n):
    r='resultat' if i==n-1 else 'limite'
    box(ax,x0+i*p,52,w,9,r,r=0.3,lw=0.6)
text(ax,x0+w/2,65.5,'2','limite','s')
text(ax,x0+(n-1)*p+w/2,65.5,'97','resultat','s')
brace(ax,x0,x0+(n-1)*p-0.4,51,'limite',label='24 essais, aucun ne divise',down=True,depth=2.4)
xg=x0+(n-1)*p+w/2
arrow(ax,(xg,36),(xg-8,28),'resultat') if False else None
arrow(ax,(xg,50.5),(xg,38),'resultat')
text(ax,xg+2,33,r'$9797 = 97 \times 101$','resultat','m',ha='right')
text(ax,xg-2,44.5,'premier qui divise','resultat','s',ha='right')
text(ax,xg-4,36,'le 25e essai divise : stop','resultat','s',ha='right') if False else None
line(ax,[(4,22),(84,22)],'fixe',dash=True)
box(ax,3,3,14,10,'limite',label='1')
arrow(ax,(18,8),(30,8),'fixe')
box(ax,31,3,26,10,'fixe',label='liste vide',dash=True)
text(ax,60,8,'rien à diviser','fixe','s',ha='left')
save(fig,'05-068')
