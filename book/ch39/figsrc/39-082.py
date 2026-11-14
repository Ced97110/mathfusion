import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
f = numberline(ax, 8, 70, 20, 0, 4, 1)
E = 2.718
for v in (2, 3):
    disc(ax, f(v), 20, 1.1, 'fixe')
disc(ax, f(E), 20, 1.8, 'sujet')
text(ax, f(E), 31.5, 'e ≈ 2,718', 'sujet', 'l', weight='bold')
arrow(ax, (f(E), 29), (f(E), 23), 'sujet', lw=1.1)
brace(ax, f(2), f(3), 14, 'fixe', label='entre 2 et 3', down=True, size='s')
box(ax, 4, 41, 54, 10, 'sujet', label='base de $e^{i\\theta}$, comme 2 dans $2^{n}$', size='s')
arrow(ax, (31, 41), (f(E) - 11, 31.5), 'sujet', lw=0.9)
save(fig, '39-082')
