import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
rows = [(0, 3), (1, 5), (2, 7), (4, 11), (6, 15)]
u, x0 = 4.0, 16.0
text(ax, 22, 69, 'départ : 3 €', 'fixe', 's')
text(ax, 46, 69, '+ 2 € par km', 'varie', 's')
for i, (d, p) in enumerate(rows):
    y = 55 - i * 10
    box(ax, x0, y, 3 * u, 6, 'fixe', r=0.6)
    for k in range(d):
        box(ax, x0 + 3 * u + k * 2 * u, y, 2 * u, 6, 'varie', r=0.6)
    text(ax, 14, y + 3, f'{d} km', 'encre', 's', ha='right')
    text(ax, x0 + p * u + 1.5, y + 3, f'{p} €', 'resultat' if p == 15 else 'encre', 's', ha='left')
line(ax, [(x0 + 15 * u, 8), (x0 + 15 * u, 64)], 'resultat', dash=True)
text(ax, 72, 69, '15 € en poche', 'resultat', 's')
save(fig, '17-001')
