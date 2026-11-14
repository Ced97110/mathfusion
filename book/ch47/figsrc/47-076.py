import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,44,64,r'$H=\{0,1,2,3,4\}$ : 5 éléments','sujet','m')
cw=12; ch=8; x0=14; 
for r in range(3):
    y=44-r*11
    n=5 if r<2 else 2
    for c in range(5):
        if c<n: box(ax,x0+c*(cw+1),y,cw,ch,'sujet' if r<2 else 'limite',r=0.5)
        else: box(ax,x0+c*(cw+1),y,cw,ch,'fixe',fill=False,dash=True,r=0.5)
text(ax,44,15,'2 lignes de 5 + 2 cases','limite','m')
text(ax,44,8,'5 ne divise pas 12','limite','m')
save(fig,'47-076')
