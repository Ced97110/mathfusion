import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
box(ax,3,8,52,34,'fixe',fill=False,dash=True)
box(ax,6,24,46,15,'autre',fill=True)
for k in range(3):
    disc(ax,14+14*k,31.5,3.5,'autre'); disc(ax,14+14*k,15,3.5,'fixe')
text(ax,29,44.5,r'$G=SL_2(F_2)$ : 6','fixe','s')
text(ax,71,32,'dérivé : 3','autre','m')
text(ax,71,18,r'$G^{\prime}\neq G$','limite','l')
text(ax,29,3.5,r'seul $d$ non nul : $d^2=1$','fixe','s')
save(fig,'73-188')
