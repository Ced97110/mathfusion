import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
u=2.6; x0=20
text(ax,44,48,'deux planches, deux noms','encre','m')
disc(ax,9,34,5,'sujet',label=r'$a$',size='l'); box(ax,x0,29,12*u,10,'sujet',label='12 cm')
disc(ax,9,14,5,'autre',label=r'$b$',size='l'); box(ax,x0,9,18*u,10,'autre',label='18 cm')
text(ax,x0+12*u+2,34,'le premier nombre','sujet','s',ha='left')
text(ax,x0+18*u+2,14,'le second','autre','s',ha='left')
save(fig,'05-078')
