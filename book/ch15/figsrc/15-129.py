import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, r'Les six termes, pour $r=3$ et $s=2$', 'encre', 'm')
rows = [('r', 'sujet', [(r'$r$', '3'), (r'$3r$', '9'), (r'$-4r$', '−12')], 'termes en $r$', 36),
        ('s', 'autre', [(r'$-2s$', '−4'), (r'$7s$', '14'), (r'$-5s$', '−10')], 'termes en $s$', 13)]
for key, role, terms, cap, y in rows:
    text(ax, 44, y + 17, cap, role, 's')
    for i, (t, v) in enumerate(terms):
        x = 4 + i * 22
        box(ax, x, y, 18, 13, role)
        text(ax, x + 9, y + 6.5, t + '\n' + v, role, 's')
    arrow(ax, (4 + 2 * 22 + 18, y + 6.5), (68, y + 6.5), 'fixe')
    box(ax, 68, y, 16, 13, 'resultat', label='0', size='l')
text(ax, 44, 5, r'$0 + 0 = 0$ : la somme vaut 0', 'resultat', 'm')
save(fig, '15-129')
