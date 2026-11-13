import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
specs = [(4, 'sujet', 'G/N\nabélien'), (32, 'varie', 'image du\ncommutateur\n= neutre'), (60, 'resultat', 'commutateur\ndans $N$')]
for x, role, l in specs:
    box(ax, x, 46, 24, 14, role, label=l, size='s')
arrow(ax, (28.5, 53), (31.5, 53), 'fixe')
arrow(ax, (56.5, 53), (59.5, 53), 'fixe')
text(ax, 44, 40, 'triangle modulo les 3 rotations', 'fixe', 's')
box(ax, 4, 6, 38, 28, 'resultat')
text(ax, 23, 29, 'rotations = neutre', 'resultat', 's')
disc(ax, 12, 16, 4.5, 'varie', label=r'$r^2$')
text(ax, 30, 16, 'commutateur', 'varie', 's')
box(ax, 46, 6, 38, 28, 'fixe')
text(ax, 65, 20, 'réflexions', 'fixe', 'm')
save(fig, '50-214')
