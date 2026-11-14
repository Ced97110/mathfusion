import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def panneau(y, titre, n):
    text(ax, 44, y + 16, titre, 'fixe', 's')
    text(ax, 11, y + 8, r'$|G(E/F)|$', 'sujet', 's')
    text(ax, 11, y - 4, r'$[E:F]$', 'autre', 's')
    for k in range(n):
        box(ax, 24 + k * 8, y + 4, 8, 8, 'sujet')
        box(ax, 24 + k * 8, y - 8, 8, 8, 'autre')
    text(ax, 80, y + 2, f'{n} = {n}', 'resultat', 'm')
panneau(46, r'$x^3-2$, $F=\mathbb{Q}$', 6)
panneau(12, r'$(x^2-2)(x^2-3)$, $F=\mathbb{Q}$', 4)
save(fig, '63-088')
