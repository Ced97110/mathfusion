import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
text(ax,6,70,r'$2x^2$','sujet','l',ha='left'); text(ax,30,70,r'$x = 5$','fixe','m',ha='left')
for i,l in enumerate(['2',r'$\times 5$',r'$\times 5$']): box(ax,6+15*i,56,13,9,'sujet',label=l)
text(ax,6,49,r'$(2x)^2$','autre','l',ha='left')
for i,l in enumerate(['10',r'$\times 10$']): box(ax,6+15*i,35,13,9,'autre',label=l)
box(ax,6,18,0.7*50,8,'sujet',label='50')
box(ax,6,6,0.7*100,8,'autre',label='100')
save(fig,'14-020')
