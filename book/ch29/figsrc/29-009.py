import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(66)
rows = [('degrés', 'sujet', '12°', '× 0,01745', 'varie', 40, r'$2\pi \div 360$'),
        ('grades', 'autre', '13,33', '× 0,01571', 'varie', 12, r'$2\pi \div 400$')]
for nom, ro, ang, fac, rf, y, form in rows:
    text(ax, 3, y + 20, nom, ro, 'm', ha='left', weight='bold')
    box(ax, 2, y, 18, 12, 'fixe', label='500 m', size='s')
    box(ax, 22, y, 17, 12, 'varie', label=ang, size='s')
    box(ax, 41, y, 22, 12, 'varie', label=fac, size='s')
    box(ax, 65, y, 21, 12, 'resultat', label='104,7 m', size='s')
    text(ax, 52, y - 4, form, 'varie', 's')
    arrow(ax, (39, y + 6), (41, y + 6), 'fixe')
    arrow(ax, (63, y + 6), (65, y + 6), 'fixe')
save(fig, '29-009')
