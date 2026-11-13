import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
n, cw, x0 = 12, 5.2, 18
ks = [1, 2, 3, 4, 5, 6, 12]
text(ax, 44, 80, r'un sous-groupe par diviseur $k$ de 12', 'sujet', 's', weight='bold')
text(ax, x0 + n * cw / 2, 73, 'positions 0 à 11', 'fixe', 's')
for r, k in enumerate(ks):
    y = 62 - r * 8.5
    div = 12 % k == 0
    text(ax, 9, y + 3, f'k = {k}', 'sujet' if div else 'limite', 's', weight='bold' if div else 'normal')
    if not div: line(ax, [(5.8, y + 3), (12.4, y + 3)], 'limite', lw=0.9)
    for p in range(n):
        on = p % k == 0
        box(ax, x0 + p * cw, y, cw - 0.6, 6, 'sujet' if (on and div) else 'fixe', fill=(on or not div), r=0.5)
text(ax, 44, 2.5, r'$k=5$ redonne $k=1$ : pas nouveau', 'limite', 's')
save(fig, '48-131')
