import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arcpts(cx, cy, r, a0, a1, n=60):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(46)
for ox, ro in ((0, 'sujet'), (46, 'resultat')):
    line(ax, arcpts(20 + ox, 0, 30, 62, 118, 40), ro, lw=2.4)
text(ax, 20, 36, r'$L$', 'sujet', 'xl')
text(ax, 66, 36, r'$L \approx 104{,}7$ m', 'resultat', 'm')
text(ax, 20, 6, 'longueur cherchée', 'sujet', 's')
text(ax, 66, 6, 'longueur trouvée', 'resultat', 's')
text(ax, 44, 33, 'même lettre', 'varie', 's')
arrow(ax, (34, 27), (54, 27), 'varie')
save(fig, '29-003')
