import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
yS = lambda i: 62 - 10 * i
for n in range(1, 7):
    disc(ax, 14, yS(n - 1), 3.8, 'sujet', label=str(n))
    arrow(ax, (18.5, yS(n - 1)), (51.5, yS(n % 3)), 'varie')
for v in range(6):
    disc(ax, 56, yS(v), 3.8, 'resultat' if v < 3 else 'limite', label=str(v))
line(ax, [(63, yS(0) + 4), (63, yS(2) - 4)], 'resultat', lw=1.4)
line(ax, [(63, yS(3) + 4), (63, yS(5) - 4)], 'limite', lw=1.4)
text(ax, 65.5, yS(1), 'atteints :\nimage de $f$\net de $g$', 'resultat', 's', ha='left')
text(ax, 65.5, yS(4), 'jamais atteints :\n$f$ non surjective\n$g$ non bijective', 'limite', 's', ha='left')
save(fig, '43-098')
