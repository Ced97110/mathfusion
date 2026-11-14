import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(76)
f = numberline(ax, 34, 80, 28, -2, 2, step=1, labels=False, arrow_right=False)
s2 = math.sqrt(2)
disc(ax, 12, 52, 8, 'sujet')
text(ax, 12, 52, r'$r=\sqrt{2}$', 'sujet', 's')
for v, l, lab, cv in [(s2, r'$\sqrt{2}$', r'$\eta=1$', 0.25), (-s2, r'$-\sqrt{2}$', r'$\eta=\sigma$', -0.25)]:
    disc(ax, f(v), 28, 2, 'resultat')
    text(ax, f(v), 22, l, 'resultat', 's')
    arrow(ax, (19, 49 if v > 0 else 47), (f(v) - (1 if v > 0 else -1) * 0.5, 31), 'varie', curve=cv)
text(ax, 55, 62, r'$\eta(r)$ pour $\eta\in G$', 'varie', 's')
text(ax, 70, 46, r'$f=x^2-2$', 'sujet', 's')
text(ax, 70, 36, r'$\eta=1$', 'varie', 's')
text(ax, 26, 33, r'$\eta=\sigma$', 'varie', 's')
text(ax, 44, 10, "l'orbite de $r$ : 2 racines de $f$", 'resultat', 's')
text(ax, 44, 3, r'Artin : $[E:F]\leq|G|$, degré fini', 'sujet', 's')
save(fig, '63-107')
