import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 46, 66, r'$G=\mathbb{Z}/4\oplus\mathbb{Z}/2$', 'sujet', 'm')
for a in range(4):
    for b in range(2):
        role = 'varie' if (a, b) == (2, 0) else ('sujet' if a % 2 == 1 else 'fixe')
        box(ax, 14 + a * 16, 22 + b * 13, 15, 11.5, role, label=f'({a}, {b})')
text(ax, 16, 12, 'ordre 4 = maximal', 'sujet', 's')
text(ax, 46, 12, 'g = (2, 0) : ordre 2', 'varie', 's')
text(ax, 77, 12, 'ordre ≤ 2', 'fixe', 's')
save(fig, '60-255')
