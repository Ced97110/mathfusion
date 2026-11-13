import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
box(ax, 10, 56, 68, 11, 'resultat', label=r'règle : $a + b = b + a$')
arrow(ax, (30, 55), (22, 43.5), 'varie'); arrow(ax, (58, 55), (66, 43.5), 'varie')
text(ax, 22, 39, 'nombres entiers', 'sujet', 'm'); text(ax, 66, 39, 'heures', 'autre', 'm')
for i, x in enumerate([9, 17, 25, 33]): disc(ax, x, 22, 3.4, 'sujet', label=str(i), size='s')
text(ax, 40.5, 22, '…', 'sujet', 'm')
cx, cy, R = 66, 22, 12
disc(ax, cx, cy, R, 'autre', fill=False)
for k in range(12):
    a = math.radians(90 - 30 * k)
    line(ax, [(cx + R * math.cos(a), cy + R * math.sin(a)), (cx + (R - 1.5) * math.cos(a), cy + (R - 1.5) * math.sin(a))], 'autre')
for k, s in [(0, '12'), (3, '3'), (6, '6'), (9, '9')]:
    a = math.radians(90 - 30 * k); text(ax, cx + 7.5 * math.cos(a), cy + 7.5 * math.sin(a), s, 'autre', 's')
text(ax, 44, 3, 'même règle, deux ensembles', 'resultat', 'm')
save(fig, '80-487')
