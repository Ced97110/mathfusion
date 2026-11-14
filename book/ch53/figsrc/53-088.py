import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
cw, g = 3.5, 0.5


def grille(y_top, e):
    for r in range(40):
        row, col = divmod(r, 20)
        atteint = (e * 0 + r) % e == 0 if e == 4 else True
        if r == 1:
            role = 'resultat' if e == 3 else 'limite'
        else:
            role = 'resultat' if e == 3 else ('varie' if atteint else 'fixe')
        box(ax, 4.25 + col * (cw + g), y_top - row * (cw + g), cw, cw, role, r=0.2, lw=0.5)


text(ax, 44, 74, r'$e = 3$ : PGCD$(3, 40) = 1$', 'resultat', 'm')
grille(60, 3)
text(ax, 6.25 + 4.0, 66.5, '1', 'encre', 's')
text(ax, 44, 48, 'tous les restes, dont 1', 'resultat', 's')
text(ax, 44, 40, r'$e = 4$ : PGCD$(4, 40) = 4$', 'varie', 'm')
grille(30, 4)
text(ax, 6.25 + 4.0, 36.5, '1', 'limite', 's')
text(ax, 44, 18, 'multiples de 4 seulement', 'varie', 's')
text(ax, 44, 10, 'le reste 1 n’est jamais atteint', 'limite', 's')
save(fig, '53-088')
