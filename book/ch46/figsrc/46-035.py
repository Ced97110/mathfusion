import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def clock(ax, cx, cy, r, roles=None, dr=1.8, labels=(), dashed=False):
    roles = roles or {}
    pos = {}
    for k in range(12):
        x, y = cx + r * math.sin(math.pi * k / 6), cy + r * math.cos(math.pi * k / 6)
        pos[k] = (x, y)
        if k in roles: disc(ax, x, y, dr, roles[k], label=(str(k) if k in labels else None), size='s')
        else: disc(ax, x, y, dr * 0.6, 'fixe', fill=False, lw=0.6)
    return pos

fig, ax = canvas(86)
text(ax, 63, 80, 'différent\nde $G$ ?', 'sujet', 's'); text(ax, 80, 80, 'plus que\nle neutre ?', 'autre', 's')
rows = [('{0}', {0: 'sujet'}, 'oui', 'non'), ('{0, 4, 8}', {0: 'sujet', 4: 'sujet', 8: 'sujet'}, 'oui', 'oui'), ('horloge entière', {k: 'fixe' for k in range(12)}, 'non', 'oui')]
for i, (n, ro, a, b) in enumerate(rows):
    y = 66 - i * 22
    clock(ax, 12, y, 8, ro)
    text(ax, 24, y, n, 'encre', 's', ha='left')
    text(ax, 63, y, a, 'resultat' if a == 'oui' else 'limite', 'l'); text(ax, 80, y, b, 'resultat' if b == 'oui' else 'limite', 'l')
text(ax, 44, 7, 'deux questions, deux écarts différents', 'encre', 's')
save(fig, '46-035')
