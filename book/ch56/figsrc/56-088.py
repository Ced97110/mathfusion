import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
labs = ['(48)', '(24)', '(12)', '(6)', '(3)', '(3)', '(3)']
w, step, x0, y = 10.5, 12.0, 3.0, 36.0
box(ax, 1, 32, 86, 27, 'varie', fill=False, lw=1.0, r=1.5)
text(ax, 44, 54, 'réunion I de tous les idéaux : I = (d)', 'varie', 's')
for i, l in enumerate(labs):
    role = 'sujet' if i < 4 else 'resultat'
    box(ax, x0 + i * step, y, w, 10, role, label=l, size='s', dash=(i >= 5))
cx = x0 + 4 * step + w / 2
text(ax, 44, 22, 'd = 3 est déjà dans (3), au rang N = 5', 'resultat', 's')
arrow(ax, (cx, 25), (cx, y - 0.5), 'resultat')
arrow(ax, (44, 19), (44, 14.5), 'fixe')
box(ax, 8, 3, 72, 11, 'resultat', label='I = (d) = (3) : la suite ne change plus', size='s')
save(fig, '56-088')
