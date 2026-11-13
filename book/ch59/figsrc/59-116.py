import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
cw, ch, x, y = 11, 8, 33, 70
for i, row in enumerate([['4', '6'], ['6', '4']]):
    for j, v in enumerate(row):
        box(ax, x + j * cw, y + (1 - i) * ch, cw, ch, 'fixe', r=0.4, label=v, size='m')
# colonne de gauche : mineurs
arrow(ax, (x + 3, y - 1), (22, 58), 'sujet')
text(ax, 22, 54, 'par les mineurs', 'sujet', 's', weight='bold')
text(ax, 22, 44, 'Δ₁ = pgcd(4, 6, 6, 4) = 2', 'sujet', 's')
text(ax, 22, 36, 'Δ₂ = |4·4 − 6·6| = 20', 'sujet', 's')
text(ax, 22, 28, 'd₂ = 20 ÷ 2 = 10', 'sujet', 's')
# colonne de droite : opérations
arrow(ax, (x + 19, y - 1), (66, 58), 'autre')
text(ax, 66, 54, 'par les opérations', 'autre', 's', weight='bold')
text(ax, 66, 44, 'diag(2, 10)', 'autre', 's')
text(ax, 66, 36, 'd₁ = 2', 'autre', 's')
text(ax, 66, 28, 'd₂ = 10', 'autre', 's')
arrow(ax, (22, 24), (40, 14), 'resultat')
arrow(ax, (66, 24), (48, 14), 'resultat')
text(ax, 44, 8, 'mêmes nombres : 2 et 10', 'resultat', 'm', weight='bold')
save(fig, '59-116')
