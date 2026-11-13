import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
Q = r'$\overline{\mathbb{Q}}$'
items = [('fixe', r'$f$ à coefficients dans ' + Q), ('sujet', r'une racine $u$ dans ℂ'),
         ('varie', r'$u$ algébrique sur ' + Q + r', ' + Q + r' sur ℚ'),
         ('resultat', r'$u$ est dans ' + Q), ('resultat', Q + ' est algébriquement clos')]
labs = ['théorème fondamental', None, 'théorème C', 'vrai pour tout $f$']
h, g, x, w = 10, 7, 4, 80
ys = [2 + (4 - i) * (h + g) for i in range(5)]
for i, ((role, s), y) in enumerate(zip(items, ys)):
    box(ax, x, y, w, h, role, label=s, size='s', weight='bold' if i == 4 else 'normal')
for i in range(4):
    arrow(ax, (14, ys[i]), (14, ys[i + 1] + h), 'encre')
    if labs[i]: text(ax, 18, ys[i] - g / 2, labs[i], 'varie' if i == 2 else 'fixe', 's', ha='left')
save(fig, '61-149')
