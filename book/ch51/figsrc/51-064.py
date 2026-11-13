import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, 'multiplication seule : un monoïde', 'sujet', 'm')
text(ax, 44, 67, 'regrouper 3 facteurs : oui', 'resultat', 'm')
text(ax, 44, 60, 'multiplier par 1 : rien ne change', 'resultat', 'm')
text(ax, 44, 49, 'ligne de 2 sur le cadran à 4 h', 'autre', 'm')
xs = [14 + k * 20 for k in range(4)]
for k, x in enumerate(xs):
    box(ax, x - 6, 36, 12, 8, 'varie', label=str(k), size='m')
    ok = k in (0, 2)
    box(ax, x - 6, 8, 12, 8, 'resultat' if ok else 'limite', label=str(k), size='m', dash=not ok, fill=ok)
for k, x in enumerate(xs):
    hit = (2 * k) % 4
    arrow(ax, (x, 35), (xs[hit], 17), 'fixe')
text(ax, 44, 26, '', 'fixe') if False else None
text(ax, 44, 3.2, '1 et 3 ne sont jamais atteints', 'limite', 's')
save(fig, '51-064')
