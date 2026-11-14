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

fig, ax = canvas(70)
text(ax, 22, 64, '$H$ = {0, 1, 11}', 'sujet', 'm')
clock(ax, 22, 38, 15, {0: 'sujet', 1: 'sujet', 11: 'sujet', 10: 'limite'}, dr=2.6, labels=(0, 1, 11, 10))
text(ax, 62, 64, 'tous les couples', 'encre', 's')
rows = [('1 − 0 = 1', True), ('0 − 1 = 11', True), ('11 − 1 = 10', False)]
for i, (t, ok) in enumerate(rows):
    y = 50 - i * 11
    text(ax, 52, y, t, 'resultat' if ok else 'limite', 'm')
    text(ax, 78, y, '✓' if ok else '✗', 'resultat' if ok else 'limite', 'l')
text(ax, 62, 14, 'un seul échec suffit', 'limite', 's')
text(ax, 22, 8, '10 est hors de $H$', 'limite', 's')
save(fig, '46-045')
