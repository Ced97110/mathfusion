import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
labs = [r'$\sqrt{80x^9}/\sqrt{5x^4}$', r'$\sqrt{80x^9/(5x^4)}$', r'$\sqrt{16x^5}$', r'$4x^2\sqrt{x}$']
acts = ['une seule racine', 'on divise', 'on sort les carrés']
for i, l in enumerate(labs):
    y = 78 - i * 19
    box(ax, 4, y, 40, 9, 'resultat' if i == 3 else 'sujet', label=l, size='s')
    if i < 3:
        arrow(ax, (24, y), (24, y - 10), 'varie'); text(ax, 28, y - 5, acts[i], 'varie', 's', ha='left')
box(ax, 4, 5, 40, 9, 'resultat', label=r'$x=4$ : $4\times16\times2=128$', size='s')
arrow(ax, (24, 21), (24, 14.5), 'fixe')
save(fig, '22-156')
