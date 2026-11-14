import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
cy = 68
for c, lab in [(15, 'chapitre 11'), (44, 'chapitre 19'), (73, 'chapitre 22')]:
    text(ax, c, 84, lab, 'fixe', 's')
c = 15; line(ax, [(c - 8, cy - 6), (c + 8, cy - 6)], 'sujet', lw=1.4); line(ax, [(c - 8, cy - 6), (c - 8, cy + 10)], 'sujet', lw=1.4)
line(ax, [(c - 8, cy - 3), (c - 5, cy - 3), (c - 5, cy - 6)], 'sujet', lw=0.8)
text(ax, c, 56, 'angle droit', 'sujet', 's')
c = 44; line(ax, [(c - 8, cy - 8), (c + 5, cy + 10)], 'varie', lw=1.4)
text(ax, c, 56, r'$y=mx$', 'varie', 's')
c = 73; poly(ax, [(c - 8, cy - 6), (c + 4, cy - 6), (c + 4, cy + 10)], 'autre')
text(ax, c, 56, '9 + 16 = 25', 'autre', 's')
for c in (15, 44, 73): arrow(ax, (c, 51), (c * 0.5 + 22, 37), 'fixe')
box(ax, 14, 20, 60, 16, 'resultat', label=r'une seule règle $B$', size='l')
text(ax, 44, 13, 'tout corps, toute dimension', 'resultat', 's')
text(ax, 44, 6, r'carré d’un non nul = 0 : $1-1$', 'encre', 's')
save(fig, '72-158')
