import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,44,48,'recommencer avec le reste','encre','m')
xs=[22,40,58]; ys=[34,20,6]
for r in range(3):
    text(ax,11,ys[r]+5,'reste : %d'%(3-r),'encre','s')
    for c in range(3):
        if c<r: box(ax,xs[c],ys[r],16,10,'fixe',label=(r'$u_%d$'%(c+1) if r==1 and c==0 else None))
        elif c==r and r<2: box(ax,xs[c],ys[r],16,10,'sujet',label=r'$u_%d$'%(c+1))
        elif r==2 and c==2: box(ax,xs[c],ys[r],16,10,'autre',label='radical',size='s')
        else: box(ax,xs[c],ys[r],16,10,'fixe',fill=False,dash=True)
save(fig,'71-158')
