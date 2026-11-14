import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
box(ax, 2, 66, 38, 10, 'fixe', True, label=r'$x^2+4x=30$')
box(ax, 46, 66, 40, 10, 'fixe', True, label=r'$4x+5=35-x^2$')
arrow(ax, (21, 65), (34, 47), 'varie'); text(ax, 15, 56, r'$-30$', 'varie', 's')
arrow(ax, (66, 65), (54, 47), 'varie'); text(ax, 75, 56, r'$+x^2,\ -35$', 'varie', 's')
box(ax, 22, 36, 44, 10, 'resultat', True, label=r'$x^2+4x-30=0$')
for x, s in [(6, r'$a=1$'), (33, r'$b=4$'), (60, r'$c=-30$')]:
    box(ax, x, 12, 22, 10, 'sujet', True, label=s)
    line(ax, [(x + 11, 35.5), (x + 11, 22.5)], 'fixe', lw=0.5, dash=True)
save(fig, '23-015')
