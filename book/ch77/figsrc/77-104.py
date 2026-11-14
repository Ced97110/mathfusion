import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,24,66,40,12,'fixe',label=r'$u\in L$')
arrow(ax,(38,66),(22,58),'sujet'); arrow(ax,(50,66),(66,58),'autre')
text(ax,22,55,r'$N_{L/E}(u)$','sujet'); text(ax,66,55,r'$N_{L/K}(u)$','autre')
for i in range(2):
    for j in range(2): box(ax,15+j*7,36+i*7,7,7,'sujet',r=0.3)
for i in range(4):
    for j in range(4): box(ax,55+j*5.5,28+i*5.5,5.5,5.5,'autre',r=0.3)
text(ax,22,32,r'$2\times2$','sujet'); text(ax,66,24,r'$4\times4$','autre')
arrow(ax,(22,29),(22,16),'varie'); arrow(ax,(66,21),(66,16),'varie')
box(ax,8,4,28,12,'sujet',label=r'$2\sqrt{2}\in E$'); box(ax,52,4,28,12,'autre',label=r'$-8\in K$')
save(fig,'77-104')
