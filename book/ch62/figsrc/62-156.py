import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
S, G = 5.5, 1.0
def row(x0, y, n, role):
    for i in range(n):
        box(ax, x0 + i * (S + G), y, S, S, role, r=0.3)
# colonne gauche : x^3 - 2 (6 et 6) ; colonne droite : x^2 + t (2 et 1)
text(ax, 22, 82, r'$x^3-2$', 'sujet', 'l')
text(ax, 66, 82, r'$x^2+t$', 'autre', 'l')
text(ax, 66, 76.5, '(1 + 1 = 0)', 'fixe', 's')
text(ax, 22, 68, 'degré [E : F]', 'sujet', 's')
text(ax, 66, 68, 'degré [E : F]', 'autre', 's')
row(3, 59, 6, 'sujet'); row(47, 59, 2, 'autre')
text(ax, 22, 50, 'isomorphismes', 'resultat', 's')
text(ax, 66, 50, 'isomorphismes', 'resultat', 's')
row(3, 41, 6, 'resultat'); row(47, 41, 1, 'resultat')
box(ax, 8, 22, 28, 11, 'resultat', label='6 = 6', size='m')
box(ax, 52, 22, 28, 11, 'varie', label='1 < 2', size='m')
text(ax, 22, 15, 'racines distinctes', 'resultat', 's')
text(ax, 66, 15, 'racine répétée', 'varie', 's')
save(fig, '62-156')
