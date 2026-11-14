import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def cells(x,y,n,role):
    for i in range(n): poly(ax,[(x+i*5,y),(x+i*5+4.2,y),(x+i*5+4.2,y+4.2),(x,y+4.2)][:0] or [(x+(i%2)*5,y+(i//2)*5),(x+(i%2)*5+4.2,y+(i//2)*5),(x+(i%2)*5+4.2,y+(i//2)*5+4.2),(x+(i%2)*5,y+(i//2)*5+4.2)],role)
text(ax,44,62,'avec division : trois seulement','resultat','m')
for x,l,d,n in [(4,'ℝ','dim 1',1),(32,'ℂ','dim 2',2),(60,'ℍ','dim 4',4)]:
    box(ax,x,28,24,26,'resultat'); text(ax,x+12,48,l,'resultat','l',weight='bold')
    cells(x+7 if n>1 else x+9.9,32,n,'resultat'); text(ax,x+12,24,d,'resultat','s')
box(ax,4,2,80,13,'limite',label=None)
text(ax,24,8.5,r'$M_2(\mathbb{R})$ : dim 4','limite','m')
text(ax,62,8.5,r'$e_{12}\times e_{12}=0$','limite','m')
save(fig,'76-145')
