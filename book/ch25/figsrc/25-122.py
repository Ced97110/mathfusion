import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="varie", n=24):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role)
fig, ax = canvas(62)
text(ax, 18, 57, 'angle', 'sujet', 's'); text(ax, 62, 57, 'tangente', 'resultat', 's')
rows = [('80°', '≈ 5,67'), ('89°', '≈ 57,29'), ('89,9°', '≈ 572,96'), ('89,99°', '≈ 5 729,58')]
for i, (a, v) in enumerate(rows):
    y = 43 - i * 10
    box(ax, 6, y - 4, 24, 8, 'sujet', label=a, size='s')
    arrow(ax, (31, y), (39, y), 'varie')
    box(ax, 40, y - 4, 40, 8, 'resultat', label=v, size='s')
text(ax, 43, 7.5, 'dépasse tout nombre fixé', 'varie', 's', weight='bold')
arrow(ax, (18, 51), (18, 13), 'varie') if False else None
save(fig, '25-122')
