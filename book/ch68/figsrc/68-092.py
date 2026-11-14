import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
R = 6.5
P = {'00': (26, 24), '01': (62, 24), '10': (26, 48), '11': (62, 48)}
for a, b in [('00', '01'), ('00', '10'), ('01', '11'), ('10', '11')]:
    (x0, y0), (x1, y1) = P[a], P[b]
    dx, dy = x1 - x0, y1 - y0
    n = (dx * dx + dy * dy) ** 0.5
    line(ax, [(x0 + dx / n * R, y0 + dy / n * R), (x1 - dx / n * R, y1 - dy / n * R)], 'fixe')
for w, (x, y) in P.items():
    disc(ax, x, y, R, 'varie' if w == '01' else 'sujet', label=w)
arrow(ax, (33, 24), (55, 24), 'varie')
text(ax, 26, 12, 'envoyé', 'sujet', 's')
text(ax, 62, 12, 'reçu', 'varie', 's')
text(ax, 44, 12, 'une erreur', 'varie', 's')
text(ax, 44, 60, r'tous les mots permis : $d=1$', 'sujet', 'm')
save(fig, '68-092')
