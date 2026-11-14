import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
box(ax,29,38,30,16,'sujet',label=r'$\sigma$',size='xl')
text(ax,44,58,'lu « sigma »','sujet','s')
box(ax,3,6,38,17,'fixe',label=None); box(ax,47,6,38,17,'varie',label=None)
text(ax,22,18,'identité','fixe','s'); text(ax,22,11,r'$\sigma(a)=a$','fixe','s')
text(ax,66,18,'conjugaison','varie','s'); text(ax,66,11,r'$\sigma(a+bi)=a-bi$','varie','s')
arrow(ax,(36,38),(22,24),'fixe'); arrow(ax,(52,38),(66,24),'varie')
save(fig,'80-103')
