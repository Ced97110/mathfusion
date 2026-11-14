import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(60)
for y, nom in ((44, 'virage'), (28, 'horloge'), (12, 'sinus')):
    box(ax, 2, y, 36, 11, 'fixe', label=nom + ' : 0,01745', size='s')
    arrow(ax, (38, y + 5.5), (52, 33), 'varie', lw=0.8)
box(ax, 52, 20, 34, 26, 'resultat', fill=True, dash=True, label='', size='s')
text(ax, 69, 37, 'facteur', 'resultat', 'm')
text(ax, 69, 29, r'exactement 1 ?', 'resultat', 's')
save(fig, '29-014')
