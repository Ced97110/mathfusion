import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
for y, a, b, role in [(38, 6, 4, 'varie'), (16, 3, 6, 'varie')]:
    text(ax, 14, y, rf'$\frac{{1}}{{{a}}}$', role, 'xl'); text(ax, 28, y, '+', 'fixe', 'l')
    text(ax, 42, y, rf'$\frac{{1}}{{{b}}}$', role, 'xl'); text(ax, 56, y, '=', 'fixe', 'l')
    text(ax, 70, y, r'$\frac{1}{x}$', 'sujet', 'xl')
text(ax, 28, 50, 'dénominateurs connus : ils changent', 'varie', 's')
text(ax, 70, 27, r'$x$ : temps à deux', 'sujet', 's')
text(ax, 44, 4, 'même forme dans les deux cas', 'fixe', 's')
save(fig, '21-008')
