import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
box(ax,2,44,40,10,'sujet',label='26 × 27 = 702'); box(ax,2,14,40,10,'autre',label='2 × 27 = 54')
arrow(ax,(22,43),(22,25),'varie'); text(ax,24,34,'remplace 26 par 2','varie','s',ha='left')
box(ax,54,26,32,12,'resultat',label='même classe'); text(ax,70,21,'modulo 12','resultat','m')
arrow(ax,(43,49),(53,37),'resultat'); arrow(ax,(43,19),(53,27),'resultat')
text(ax,48,6,'702 − 54 = 648 = 54 × 12','resultat','m')
save(fig,'47-103')
