import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
for y,role,a,b,t in [(40,'autre',r'$\frac{3}{4}$',r'$\frac{6}{8}$','même nombre'),(8,'sujet',r'$x+7=11$',r'$x=4$','mêmes solutions')]:
    h=14 if y==40 else 12
    box(ax,8,y,28,h,role,label=a,size='l'); box(ax,52,y,28,h,role,label=b,size='l')
    arrow(ax,(36,y+h/2),(52,y+h/2),role,both=True)
    brace(ax,8,80,y-2,role,t)
text(ax,44,59,'écritures différentes','fixe','s')
save(fig,'16-045')
