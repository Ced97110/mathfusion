import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
text(ax,44,45,'groupes alternés','fixe','m')
for k,(n,o) in enumerate([(3,'3'),(4,'12'),(5,'60'),(6,'360'),(7,'2 520')]):
    box(ax,2+17*k,30,16,9,'fixe',label=rf'$A_{n}$: {o}',size='s')
text(ax,44,21,r'$\neq$','limite','xl')
box(ax,24,5,40,9,'autre',label=r'$PSL_2(F_7)$ : 168',size='m')
text(ax,76,9.5,'autre famille','autre','s')
save(fig,'73-182')
