import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(cx, cy, R, n=12):
    return [(cx + R * math.cos(math.radians(90 - 360 / n * k)), cy + R * math.sin(math.radians(90 - 360 / n * k))) for k in range(n)]

fig, ax = canvas(72)
for cx, role, name, ans, ar in [(22, 'sujet', 'horloge', 'oui', 'resultat'), (66, 'autre', r'$A_4$', 'non', 'limite')]:
    text(ax, cx, 66, name, role, 'l')
    for p in ring(cx, 44, 12): disc(ax, p[0], p[1], 2.4, role)
    text(ax, cx, 27, '12 éléments', role, 's')
    arrow(ax, (cx, 23.5), (cx, 17.5), 'varie')
    box(ax, cx - 12, 4, 24, 10, ar, label=ans, size='l')
text(ax, 44, 21, 'sous-groupe de 6 ?', 'varie', 's')
save(fig, '50-007')
