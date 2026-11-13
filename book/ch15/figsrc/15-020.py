import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(55)
box(ax, 8, 26, 16, 11, 'sujet', label=r'$4$'); text(ax, 35, 31.5, '+', 'varie', 'l')
box(ax, 46, 26, 34, 11, 'sujet', label=r'$2 \times 3$')
line(ax, [(35, 22), (35, 28)], 'varie', dash=True); line(ax, [(35, 35), (35, 46)], 'varie', dash=True)
text(ax, 35, 50, 'le $+$ coupe', 'varie', 's')
text(ax, 16, 20, 'terme', 'sujet', 'm'); text(ax, 63, 20, 'terme', 'sujet', 'm')
brace(ax, 8, 80, 14, 'fixe', 'somme', size='s')
save(fig, '15-020')
