import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
steps = [('Sylow III réduit chaque $n_p$\nex. $n_5 \\in \\{1, 6\\}$', 'sujet'),
         ('Supposer chaque $n_p \\neq 1$', 'varie'),
         ('Compter les éléments\n$24 + 20 = 44$', 'varie'),
         ('Comparer à $|G| = 30$\n44 > 30 : impossible', 'limite'),
         ('Donc un $n_p$ vaut 1', 'resultat')]
h, gap = 13, 6
for i, (l, r) in enumerate(steps):
    y = 96 - 4 - h - i * (h + gap)
    box(ax, 14, y, 60, h, r, label=l, size='m')
    if i: arrow(ax, (44, y + h + gap), (44, y + h + 0.8), 'fixe')
save(fig, '50-187')
