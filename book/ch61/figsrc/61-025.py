import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
xs=[(4,22,'fixe'),(26,16,'sujet'),(48,22,'varie')]
text(ax,44,56,r'$\mathbb{Q}(\sqrt{2},\sqrt{3})$','encre','xl')
box(ax,6,34,16,12,'fixe',label=r'$\mathbb{Q}$',size='l')
box(ax,34,34,20,12,'varie',label=r'$\sqrt{2}$',size='l'); text(ax,28,40,'(','encre','xl') if False else None
text(ax,58,40,',','encre','xl'); box(ax,62,34,20,12,'autre',label=r'$\sqrt{3}$',size='l')
for x0,x1,lab,role in ((19,35,r'$+\sqrt{2}$','varie'),(53,69,r'$+\sqrt{3}$','autre')): pass
box(ax,1,4,18,12,'fixe',label=r'$\mathbb{Q}$',size='s')
box(ax,35,4,22,12,'varie',label=r'$\mathbb{Q}(\sqrt{2})$',size='s')
box(ax,70,4,17,12,'autre',label=r'$\mathbb{Q}(\sqrt{2},\sqrt{3})$',size='s') if False else None
box(ax,66,4,21,12,'autre',label=r'$\mathbb{Q}(\sqrt{2},\sqrt{3})$',size='s')
arrow(ax,(19,10),(35,10),'varie'); arrow(ax,(57,10),(66,10),'autre')
text(ax,27,19,r'$+\sqrt{2}$','varie','s'); text(ax,61.5,19,r'$+\sqrt{3}$','autre','s')
save(fig,'61-025')
