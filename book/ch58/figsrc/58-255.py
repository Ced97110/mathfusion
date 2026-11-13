import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def row(y, role, k, img, name):
    box(ax, 3, y, 12, 10, 'fixe', label=r'$\mathbb{Z}$')
    arrow(ax, (16, y + 5), (43, y + 5), role, lw=1.2)
    text(ax, 29.5, y + 9.5, f'{k} $\\mapsto$ {img}', role, 's')
    box(ax, 44, y, 26, 10, role, label=name, size='s')
row(46, 'sujet', 3, '(3, 0)', r'$\mathbb{Z}$(1, 0)')
row(26, 'autre', 4, '(0, 4)', r'$\mathbb{Z}$(0, 1)')
text(ax, 57, 38, r'$\oplus$', 'resultat', 'l', weight='bold')
line(ax, [(73, 51), (75, 51), (75, 31), (73, 31)], 'resultat', lw=1.0)
text(ax, 81, 41, r'$=\mathbb{Z}^2$', 'resultat', 'm', weight='bold')
text(ax, 44, 12, 'chaque ligne ressemble à ℤ', 'fixe', 's')
save(fig, '58-255')
