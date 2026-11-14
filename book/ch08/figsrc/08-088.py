import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,23,61,'bas 8 : exact','resultat','l',weight='bold')
text(ax,65,61,'bas 3 : pas exact','limite','l',weight='bold')
u=38/3
text(ax,23,52,'3/8 = 0,375','resultat','m')
for k in range(8): box(ax,3+k*38/8,36,38/8,8,'resultat',lw=0.5,r=0.2)
text(ax,23,30,'8 × 0,375 = 3','resultat','s')
text(ax,65,52,'1/3 ≈ 0,33','limite','m')
for k in range(3): box(ax,45+k*0.33*38,36,0.33*38,8,'limite',lw=0.5,r=0.2)
box(ax,45,36,38,8,'fixe',fill=False,dash=True,r=0.2,lw=0.5)
text(ax,65,30,'3 × 0,33 = 0,99','limite','s')
text(ax,65,22,'et non 1','limite','s')
save(fig,'08-088')
