import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
c, x0 = 2.3, 3.8
text(ax, 3, 60, '221 = 13 × 17 : proches', 'sujet', 'm', ha='left')
box(ax, x0, 46, c, 6, 'resultat', r=0.3, lw=0.5)
text(ax, 12, 49, 'x = 15 : 1 essai', 'resultat', 's', ha='left')
text(ax, 3, 36, '303 = 3 × 101 : éloignés', 'varie', 'm', ha='left')
for k in range(35):
    box(ax, x0 + k * c, 22, c, 6, 'resultat' if k == 34 else 'fixe', r=0.3, lw=0.5)
text(ax, x0 + 1.5, 17.5, 'x = 18', 'fixe', 's', ha='left')
text(ax, x0 + 35 * c - 1.5, 17.5, 'x = 52', 'resultat', 's', ha='right')
text(ax, 44, 31, '35 essais', 'varie', 's')
text(ax, 44, 7, 'p et q éloignés : Fermat est lent', 'encre', 's') if False else None
text(ax, 44, 8, 'choisir p et q éloignés', 'encre', 'm')
save(fig, '53-189')
