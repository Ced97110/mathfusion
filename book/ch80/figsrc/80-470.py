import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(74)
box(ax, 14, 12, 60, 54, 'fixe', r=2.0)
text(ax, 44, 70.5, 'le plan entier', 'fixe', 'm')
arrow(ax, (14, 39), (74, 39), 'sujet', lw=1.8, both=True) if False else None
line(ax, [(16, 39), (72, 39)], 'sujet', lw=2.0); line(ax, [(44, 14), (44, 64)], 'varie', lw=2.0)
disc(ax, 44, 39, 2.0, 'resultat')
text(ax, 17, 43, 'droite horizontale', 'sujet', 's', ha='left')
text(ax, 47, 59, 'complément', 'varie', 's', ha='left')
text(ax, 47, 33.5, 'origine', 'resultat', 's', ha='left')
text(ax, 44, 5, 'somme : tout le plan', 'encre', 's')
save(fig, '80-470')
