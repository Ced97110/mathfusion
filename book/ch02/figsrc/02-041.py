import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,22,70,'9 − 4 : d = 5','resultat','m'); text(ax,64,70,'52 − 27 : d = 25','resultat','m')
numberline(ax,8,76,50,0,10,1,labels=False,role='fixe')
f=lambda v:8+6.8*v
disc(ax,f(4),50,1.2,'autre'); text(ax,f(4),46.5,'s = 4','autre','s')
disc(ax,f(9),50,1.2,'fixe'); text(ax,f(9),46.5,'m = 9','fixe','s')
line(ax,[(f(4),54),(f(9),54)],'resultat',lw=2.5)
text(ax,(f(4)+f(9))/2,58,'d = 5 : de s à m','resultat','s')
line(ax,[(f(4),30),(f(4),44)],'fixe',dash=True); line(ax,[(f(9),30),(f(9),44)],'fixe',dash=True)
box(ax,8,24,f(4)-8,6,'autre',label='s = 4',size='s')
box(ax,f(4),24,f(9)-f(4),6,'resultat',label='d = 5',size='s')
brace(ax,8,f(9),22,'resultat',label='s + d = m : 4 + 5 = 9')
save(fig,'02-041')
