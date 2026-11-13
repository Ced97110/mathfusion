import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
x0,y0=8,8; X=26; U=9
cols=[X,U,U]; rows=[U,X]   # bottom row height U, top row height X
cells=[(0,1,r'$x^2$','sujet'),(1,1,r'$x$','varie'),(2,1,r'$x$','varie'),(0,0,r'$x$','varie'),(1,0,'1','fixe'),(2,0,'1','fixe')]
xs=[x0,x0+X,x0+X+U,x0+X+2*U]; ys=[y0,y0+U,y0+U+X]
for c,r,s,role in cells:
    box(ax,xs[c],ys[r],xs[c+1]-xs[c],ys[r+1]-ys[r],role,label=s,size='l',r=0.4)
brace(ax,x0,xs[3],ys[2]+1,'fixe',label=r'$x+2$',down=False)
text(ax,x0-3.5,(ys[0]+ys[2])/2,r'$x+1$','fixe','s',rot=90)
text(ax,70,50,r'$(x+1)(x+2)$','sujet','m'); arrow(ax,(70,46),(70,36),'varie')
text(ax,70,28,r'$x^2+3x+2$','resultat','l')
text(ax,70,19,'encore un polynôme','resultat','s')
save(fig,'51-076')
