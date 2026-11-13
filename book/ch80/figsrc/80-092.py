import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(64)
line(ax,[(8,12),(36,40)],'sujet',lw=1.8)
line(ax,[(8,17),(31,40)],'varie',lw=1.8)
text(ax,40,32,'x − y = 0','sujet','s',ha='left')
text(ax,17,47,'x − y = −1','varie','s')
text(ax,24,57,'parallèles : aucune solution','limite','s')
text(ax,70,57,'point à l’infini','autre','s')
box(ax,58,40,26,9,'sujet',label='1 − 1 = 0',size='s')
box(ax,58,28,26,9,'varie',label='1 − 1 + 0 = 0',size='s')
box(ax,58,12,26,10,'autre',label='(1, 1, 0)',size='m')
arrow(ax,(71,39.8),(71,37.2),'fixe'); arrow(ax,(71,27.8),(71,22.2),'fixe')
save(fig,'80-092')
