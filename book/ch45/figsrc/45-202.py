import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 2, 24, 22, 16, 'sujet', label='37 dans ℤ/60', size='s', weight='bold')
s = 6.5; x0 = 52.0
rows = [(4, 1, 52, 'sujet'), (3, 1, 32, 'varie'), (5, 2, 12, 'autre')]
for n, r, y, role in rows:
    for i in range(n):
        box(ax, x0 + i * s, y, s, s, role if i == r else 'fixe', r=0.5, label=str(i) if i == r else None, size='s', weight='bold')
    text(ax, x0 - 3, y + s / 2, f'ℤ/{n}', role, 's', ha='right')
    arrow(ax, (24, 32), (x0 - 12, y + s / 2), role, lw=0.8)
    text(ax, 33, y + s / 2 + (4 if y > 32 else (-2.5 if y < 32 else 3)), f'mod {n}', role, 's') if False else None
text(ax, 44, 60, '37 = trois restes', 'encre', 's') if False else None
text(ax, 13, 17, 'restes : (1, 1, 2)', 'resultat', 's')
save(fig, '45-202')
