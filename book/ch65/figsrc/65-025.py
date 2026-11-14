import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 18, 79, r'$G$', 'autre', 'l')
text(ax, 70, 79, r'$G_f$', 'sujet', 'l')
rows = [('1', 'identité'), (r'$\sigma$', r'$(r_1\ r_2\ r_3)$'), (r'$\sigma^2$', r'$(r_1\ r_3\ r_2)$')]
for k, (a, b) in enumerate(rows):
    y = 62 - k * 13
    box(ax, 6, y - 5, 24, 10, 'autre', label=a, size='m')
    box(ax, 52, y - 5, 34, 10, 'sujet', label=b, size='m')
    arrow(ax, (30, y), (52, y), 'resultat', both=True)
text(ax, 41, 66.5, 'une seule image', 'resultat', 's')
line(ax, [(2, 26), (86, 26)], 'fixe', dash=True)
text(ax, 44, 22, 'on compose, les deux côtés suivent', 'varie', 's')
box(ax, 6, 3, 34, 14, 'autre', label=r'$\sigma$ puis $\sigma$ = $\sigma^2$', size='s')
box(ax, 48, 3, 38, 14, 'sujet', label=r'$(r_1\ r_2\ r_3)$ deux fois' + '\n' + r'= $(r_1\ r_3\ r_2)$', size='s')
arrow(ax, (40, 10), (48, 10), 'resultat', both=True)
save(fig, '65-025')
