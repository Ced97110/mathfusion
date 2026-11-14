import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cx = lambda n: 24 + 12 * (n + 2)
cy = lambda h: 14 + 8.5 * h
text(ax, 44, 57, 'M : couples (entier, heure)', 'fixe', 'm')
for n in range(-2, 3):
    text(ax, cx(n), 47, str(n), 'fixe', 's')
    for h in range(4):
        disc(ax, cx(n), cy(h), 1.9, 'sujet' if n == 0 else 'fixe')
for h in range(4):
    text(ax, 11, cy(h), str(h), 'fixe', 's')
box(ax, cx(0) - 6, cy(0) - 5, 12, 8.5 * 3 + 10, 'sujet', fill=False, dash=True)
text(ax, 44, 4, 'tor M : 4 éléments', 'sujet', 'm')
save(fig, '60-036')
