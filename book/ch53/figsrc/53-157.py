import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(114)
TOP = (31.5, 57.75, 75.25)       # positions des essais 5, 8, 10
ESS = (5, 8, 10)
def panel(y, titre, bas, xs_bas):
    text(ax, 44, y + 40, titre, 'encre', 'm', weight='bold')
    for x, e, b, xb in zip(TOP, ESS, bas, xs_bas):
        cible = e == 8
        r = 'resultat' if cible else 'fixe'
        text(ax, x, y + 31, str(e), r, 'm', weight='bold' if cible else 'normal')
        text(ax, xb, y + 1, b, r, 'm', weight='bold' if cible else 'normal')
        arrow(ax, (x, y + 28), (xb, y + 5), r, lw=1.3 if cible else 0.9)
# sur les réels : cubes 125, 512, 1000 sur une échelle 0..1000
panel(66, 'sur ℝ : essai → cube', ('125', '512', '1 000'),
      tuple(14 + v / 1000 * 66 for v in (125, 512, 1000)))
text(ax, 44, 60, 'même ordre : chaque essai oriente', 'resultat', 's')
# sur l'horloge : restes 15, 17, 10 sur une échelle 0..20
panel(10, 'horloge à 55 cases : essai → reste', ('15', '17', '10'),
      tuple(14 + v / 20 * 66 for v in (15, 17, 10)))
text(ax, 44, 3, 'ordre perdu : rien n’oriente', 'fixe', 's')
save(fig, '53-157')
