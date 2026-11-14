import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 30, 84, r'division par $x-2$', 'fixe', 's')
labs = [r'$x^3-x^2+2x-3$', r'$x^2+2x-3$', r'$4x-3$', r'$5$']
roles = ['sujet', 'fixe', 'fixe', 'resultat']
acts = [r'$-x^2(x-2)$', r'$-x(x-2)$', r'$-4(x-2)$']
w, h, x0 = 36, 9, 4
ys = [66 - 19 * i for i in range(4)]
for y, l, r in zip(ys, labs, roles):
    box(ax, x0, y, w, h, r, label=l, size='s')
for i, a in enumerate(acts):
    arrow(ax, (x0 + w / 2, ys[i]), (x0 + w / 2, ys[i + 1] + h), 'varie')
    text(ax, x0 + w / 2 + 3, (ys[i] + ys[i + 1] + h) / 2, a, 'varie', 's', ha='left')
# évaluation en 2
text(ax, 72, 84, r'$x$ remplacé par 2', 'varie', 's')
text(ax, 72, 66 + 4.5, r'$8-4+4-3$', 'varie', 's')
arrow(ax, (72, 66 - 1), (72, ys[3] + h + 3), 'varie', curve=0.0)
box(ax, 64, ys[3], 20, h, 'resultat', label=r'$f(2)=5$', size='s')
text(ax, 60, ys[3] + h / 2, '=', 'resultat', 'm')
save(fig, '54-166')
