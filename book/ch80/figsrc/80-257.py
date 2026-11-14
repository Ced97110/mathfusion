import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,52,'premier contrôle : rien avant','fixe','s')
box(ax,4,30,24,12,'fixe',fill=False,dash=True,label='avant : 0',size='s')
box(ax,30,30,54,12,'sujet',label=r'$f(x)=12$')
brace(ax,4,84,29,'sujet',label=r'$g(x)=12$')
box(ax,4,6,34,10,'resultat',label=r'$\mu(x,x)=1$',size='s')
text(ax,44,11,'on ne retire rien','resultat','s',ha='left')
save(fig,'80-257')
