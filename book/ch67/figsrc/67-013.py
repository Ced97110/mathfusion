import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
def chips(n, y, role):
    for i in range(n):
        x = 6 + 17 * i
        box(ax, x, y, 9, 9, role, label='1')
        if i < n - 1: text(ax, x + 13, y + 4.5, '+', 'encre', 'm')
text(ax, 4, 72, 'Corps à 4 éléments', 'sujet', 'm', ha='left')
chips(2, 58, 'sujet')
text(ax, 44, 62.5, '= 0', 'resultat', 'l', ha='left')
text(ax, 6, 52, 'deux termes : somme 0', 'resultat', 's', ha='left')
text(ax, 4, 44, 'Entiers modulo 3', 'autre', 'm', ha='left')
chips(3, 30, 'autre')
text(ax, 6, 24, 'deux termes : 2, pas 0', 'limite', 's', ha='left')
text(ax, 6, 17, 'trois termes : somme 0', 'resultat', 's', ha='left')
text(ax, 6, 8, 'règle 1 + 1 = 0 fausse ici', 'limite', 's', ha='left')
save(fig, '67-013')
