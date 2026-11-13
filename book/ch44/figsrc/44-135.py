import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def reg(n, cx, cy, r, role):
    poly(ax, [(cx + r * math.sin(2 * math.pi * i / n), cy + r * math.cos(2 * math.pi * i / n)) for i in range(n)], role)
rows = [(3, 60), (4, 40), (6, 20)]
for n, y in rows:
    reg(n, 10, y, 6.2 if n != 4 else 6.4, 'fixe')
    text(ax, 24, y, f'n = {n}', 'fixe', 's')
    for i in range(2 * n):
        disc(ax, 33 + (i % 6) * 5.6 if False else 33 + i * 3.6 if n == 6 else 33 + i * 4.6, y, 1.5 if n == 6 else 1.8, 'sujet' if i < n else 'autre')
    text(ax, 80, y, f'{2*n}', 'resultat', 'l')
text(ax, 45, 5, '2n = n rotations + n réflexions', 'resultat', 's')
disc(ax, 22, 70, 1.6, 'sujet'); text(ax, 25, 70, 'rotations', 'sujet', 's', ha='left')
disc(ax, 50, 70, 1.6, 'autre'); text(ax, 53, 70, 'réflexions', 'autre', 's', ha='left')
save(fig, '44-135')
