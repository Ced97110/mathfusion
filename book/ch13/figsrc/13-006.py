import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 8, 70, 24, -3, 3, labels=False)
for v, s, r in [(-2, '−2', 'sujet'), (0, '0', 'fixe'), (2, '2', 'fixe')]:
    disc(ax, f(v), 24, 2, r); text(ax, f(v), 19, s, r, 'm')
brace(ax, f(-2), f(0), 32, 'sujet', label='à 2 pas de 0', down=False)
brace(ax, f(0), f(2), 32, 'fixe', label='à 2 pas de 0', down=False)
text(ax, f(-1.5), 12, 'autre côté de zéro', 'sujet', 's')
text(ax, f(2), 12, 'côté connu', 'fixe', 's')
save(fig, '13-006')
