import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(86)
X = lambda x: 8 + (x - 0.5) * 15
Y = lambda y: 56 + y * 15
p = lambda x: (x - 2) * (x - 1) * (x - 3)
t1 = np.linspace(1, 2, 60); t2 = np.linspace(3, 3.5, 40)
for t in (t1, t2):
    up = [(X(a), Y(np.sqrt(max(p(a), 0)))) for a in t]; dn = [(X(a), Y(-np.sqrt(max(p(a), 0)))) for a in t]
    poly(ax, up + dn[::-1], 'sujet')
for xv, lab in ((1.5, 'x = 1,5'), (2.5, 'x = 2,5')):
    line(ax, [(X(xv), 34), (X(xv), 78)], 'fixe', dash=True)
    text(ax, X(xv), 81.5, lab, 'fixe', 's')
r = np.sqrt(p(1.5))
line(ax, [(X(1.5), Y(-r)), (X(1.5), Y(r))], 'resultat', lw=2.8)
text(ax, X(1.5), 30.5, 'un seul intervalle', 'resultat', 's')
text(ax, 70, 70, r'$y^2<p(x)$', 'sujet', 'm')
text(ax, 70, 60, r'$p=(x-2)(x-1)(x-3)$', 'sujet', 's')
f = numberline(ax, 6, 70, 14, 1, 14, step=1, labels=False)
for v in (2, 3, 5, 7, 11, 13):
    disc(ax, f(v), 14, 1.3, 'autre'); text(ax, f(v), 9.5, str(v), 'autre', 's')
text(ax, 40, 22, 'dans ℤ : les nombres premiers ont des trous', 'autre', 's')
save(fig, '70-182')
