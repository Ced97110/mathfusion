import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(100)
text(ax, 44, 96, r'$F(x)=x^3+px+q$', 'encre', 'l')
py = 78
arrow(ax, (8, py), (80, py), 'fixe', lw=0.8)
arrow(ax, (44, 63), (44, 90), 'fixe', lw=0.8)
text(ax, 82, py - 3, r'$p$', 'fixe', 'm')
text(ax, 47, 90, r'$q$', 'fixe', 'm')
for p in range(-4, 5):
    for q in range(-2, 3):
        if (p, q) in [(-3, 1), (1, 0)]: continue
        disc(ax, 44 + 7 * p, py + 6 * q, 0.6, 'fixe')
disc(ax, 44 - 21, py + 6, 1.8, 'varie')
disc(ax, 44 + 7, py, 1.8, 'varie')
text(ax, 44, 57, 'combien de racines, pour tous $p$, $q$ ?', 'encre', 's')
ay = 28
panels = [(22, r'$p=-3,\ q=1$', lambda t: t ** 3 - 3 * t + 1, 2.1, [-1.8794, 0.3473, 1.5321], '3 racines'),
          (66, r'$p=1,\ q=0$', lambda t: t ** 3 + t, 1.5, [0.0], '1 racine')]
for cx, title, F, lim, roots, cap in panels:
    text(ax, cx, 48, title, 'varie', 'm')
    line(ax, [(cx - 19, ay), (cx + 19, ay)], 'fixe')
    ts = np.linspace(-lim, lim, 80)
    line(ax, [(cx + 8.5 * t, ay + 3 * F(t)) for t in ts], 'sujet', lw=1.4)
    for r in roots:
        disc(ax, cx + 8.5 * r, ay, 1.4, 'resultat')
    text(ax, cx, 10, cap, 'resultat', 'm')
save(fig, '69-116')
