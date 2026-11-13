import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
X=(26,57); Wd=29; ys=(46,30,14); Hh=14
text(ax,X[0]+Wd/2,64,r'complexe $3+4i$','sujet','s'); text(ax,X[1]+Wd/2,64,r'quaternion $1+2i+2k$','autre','s')
for y,l in zip(ys,('conjugué','somme des\ncarrés','inverse')): text(ax,13,y+Hh/2,l,'fixe','s')
cells=[(r'$3-4i$',r'$1-2i-2k$'),(r'$9+16=25$',r'$1+4+0+4=9$'),(r'$\frac{3-4i}{25}$',r'$\frac{1-2i-2k}{9}$')]
for y,(a,b) in zip(ys,cells):
    box(ax,X[0],y,Wd,Hh,'sujet',label=a,size='m' if 'frac' in a else 's'); box(ax,X[1],y,Wd,Hh,'autre',label=b,size='m' if 'frac' in b else 's')
save(fig,'51-191')
