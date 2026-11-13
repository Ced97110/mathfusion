import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(58)
o = (14, 26); s = 9
P = lambda p: (o[0] + p[0] * s, o[1] + p[1] * s)
poly(ax, [P((0, 0)), P((2, 0)), P((3, 2)), P((1, 2))], 'sujet')
poly(ax, [P((0, 0)), P((1, 0)), P((1, 2))], 'varie')
arrow(ax, P((0, 0)), P((2, 0)), 'sujet', lw=1.2)
arrow(ax, P((0, 0)), P((1, 2)), 'autre', lw=1.2)
line(ax, [P((1, 2)), P((1, 0))], 'varie', dash=True, lw=1.2)
text(ax, P((1, 0))[0] + 8, P((1, 0))[1] - 3.2, r'base $\|u\|=2$', 'sujet', 's')
text(ax, P((0.5, 1))[0] - 3, P((0.5, 1))[1] + 1, r'$\|v\|$', 'autre', 's')
text(ax, P((0, 0))[0] + 10.5, P((0, 0))[1] + 2.5, r'$\theta$', 'encre', 's')
text(ax, P((1, 1))[0] + 1.5, P((1, 1))[1] + 1, 'hauteur', 'varie', 's', ha='left')
text(ax, P((1, 1))[0] + 1.5, P((1, 1))[1] - 2.5, r'$=\|v\|\sin\theta$', 'varie', 's', ha='left')
w, g = 24, 6
x0 = (88 - 3 * w - 2 * g) / 2
specs = [('départ :\nbase × hauteur', 'sujet'), ('étape : hauteur\n$=\\|v\\|\\sin\\theta$', 'varie'), ('arrivée :\n$\\|u\\|\\|v\\|\\sin\\theta$', 'resultat')]
for i, (lab, role) in enumerate(specs):
    x = x0 + i * (w + g)
    box(ax, x, 3, w, 12, role, label=lab, size='s')
    if i < 2:
        arrow(ax, (x + w + 0.5, 9), (x + w + g - 0.5, 9), 'fixe')
save(fig, '41-109')
