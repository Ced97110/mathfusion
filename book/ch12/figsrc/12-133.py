import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 8, 54, 72, 12, 'sujet', label=r'$4\times5+4\times2=28$', size='l')
text(ax, 44, 71, 'le 4 est écrit deux fois', 'sujet', 's')
box(ax, 8, 8, 72, 12, 'resultat', label=r'$4\times(5+2)=28$', size='l')
text(ax, 44, 3.5, 'le 4 est écrit une fois', 'resultat', 's')
arrow(ax, (24, 52), (24, 22), 'varie'); text(ax, 27, 37, 'factoriser', 'varie', 's', ha='left')
arrow(ax, (64, 22), (64, 52), 'fixe'); text(ax, 61, 37, 'développer', 'fixe', 's', ha='right')
save(fig, '12-133')
