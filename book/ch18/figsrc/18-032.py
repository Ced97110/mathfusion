import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
u=2.0; x0=16
for i,n in enumerate((9,18,27)):
    y=36-12*i
    text(ax,14,y,str(n),'encre','m',ha='right')
    for k in range(n//9): box(ax,x0+k*9*u,y-4,9*u,8,'sujet',label='9',size='s')
    text(ax,x0+max(n,18)*u+3,y,f'reste {n//9}','resultat','s',ha='left')
box(ax,x0,32,18*u,8,'limite',fill=False,dash=True,lw=1.0)
text(ax,x0+9*u,50,'18 ne rentre pas dans 9','limite','s')
arrow(ax,(x0+9*u,48),(x0+9*u,41),'limite')
save(fig,'18-032')
