import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(80)
text(ax, 44, 74, r'$p=x^4-10x^2+1$', 'sujet', 'm')
f = numberline(ax, 8, 80, 34, -4, 4, step=1, labels=False, arrow_right=False)
s2, s3 = math.sqrt(2), math.sqrt(3)
roots = [(s2 + s3, True, r'$\gamma=\sqrt{2}+\sqrt{3}$'), (s3 - s2, True, r'$\sqrt{3}-\sqrt{2}$'),
         (s2 - s3, False, r'$\sqrt{2}-\sqrt{3}$'), (-s2 - s3, False, r'$-\sqrt{2}-\sqrt{3}$')]
for i, (v, up, l) in enumerate(roots):
    disc(ax, f(v), 34, 2, 'varie' if i == 0 else 'resultat')
    text(ax, f(v) + (-4 if i == 1 else (4 if i == 2 else 0)), 41 if up else 27, l, 'varie' if i == 0 else 'resultat', 's')
brace(ax, 8, 80, 49, 'resultat', label=r'$E=\mathbb{Q}(\gamma)$', down=False)
text(ax, 44, 10, '4 racines distinctes, toutes dans $E$', 'resultat', 's')
save(fig, '63-120')
