import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
box(ax,4,8,80,34,'fixe')
text(ax,44,46.5,r'$S_{2}$ : 2 permutations','fixe','m')
box(ax,13,18,24,12,'sujet',label='(1)')
box(ax,49,18,30,12,'varie',label='(1 2)')
text(ax,25,11.5,r'$A_{2}$ : paire','sujet','s')
text(ax,64,11.5,'impaire : exclue','varie','s')
save(fig,'46-273')
