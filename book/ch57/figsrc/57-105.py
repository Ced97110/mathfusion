import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 2, 51, '$a$ = 3 : le coefficient', 'varie', 's', ha='left')
text(ax, 52, 51, '$x$ = 5 : l’objet', 'sujet', 's', ha='left')
def row(yc, cap, first, second, r1, r2):
    text(ax, 12, yc, cap, 'encre', 's')
    box(ax, 24, yc - 6, 14, 12, r1, label=first, size='l')
    box(ax, 40, yc - 6, 14, 12, r2, label=second, size='l')
    line(ax, [(57, yc + 1), (63, yc + 1)], 'resultat', lw=1.2)
    line(ax, [(57, yc - 1), (63, yc - 1)], 'resultat', lw=1.2)
    box(ax, 66, yc - 6, 16, 12, 'resultat', label='15', size='l')
row(32, 'à gauche :\n$ax$', '3', '5', 'varie', 'sujet')
row(10, 'à droite :\n$xa$', '5', '3', 'sujet', 'varie')
save(fig, '57-105')
