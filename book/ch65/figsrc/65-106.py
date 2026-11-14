import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
y = 30
f = numberline(ax, 6, 80, y, 1790, 1840, step=10, arrow_right=False)
for yr, role in ((1799, 'fixe'), (1824, 'sujet'), (1831, 'resultat')):
    disc(ax, f(yr), y, 1.8, role)
line(ax, [(f(1799), y + 1.8), (f(1799), 42)], 'fixe')
box(ax, 3, 42, 38, 13, 'fixe', label="1799 : Ruffini\nesquisse le résultat", size='s')
line(ax, [(f(1824), y - 1.8), (f(1824), 18)], 'sujet')
box(ax, 34, 5, 38, 13, 'sujet', label="1824 : Abel\ndémontre le résultat", size='s')
line(ax, [(f(1831), y + 1.8), (f(1831), 42)], 'resultat')
box(ax, 47, 42, 39, 13, 'resultat', label="1831 : Galois\ndonne la cause : le groupe", size='s')
save(fig, '65-106')
