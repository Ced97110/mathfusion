import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
for x, s, r, lab in [(16, r'$a$', 'sujet', 'le nombre'), (44, r'$\geq$', 'varie', 'plus grand ou égal'), (72, '0', 'fixe', 'zéro')]:
    text(ax, x, 54, s, r, 'xl'); text(ax, x, 46, lab, r, 's')
f = numberline(ax, 6, 80, 18, -4, 9, labels=False, arrow_right=False)
ax.add_patch(Rectangle((f(0), 15), f(9) - f(0), 6, fc=FILL['resultat'], ec='none', zorder=0.5))
for v, r, ans in [(-3, 'limite', 'faux'), (0, 'resultat', 'vrai'), (8, 'resultat', 'vrai')]:
    disc(ax, f(v), 18, 1.8, r)
    text(ax, f(v), 12.5, f'{v}'.replace('-', '−'), r); text(ax, f(v), 25, ans, r, 's')
text(ax, f(4.5), 6, 'zone où $a\geq 0$ est vrai', 'resultat', 's')
save(fig, '13-048')
