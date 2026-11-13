import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from figstyle import *
fig, ax = canvas(64)
# ligne du haut : 8 × 5
text(ax, 9, 56, '8 ×', 'autre', 'l')
text(ax, 16, 56, '5', 'varie', 'l')
line(ax, [(4, 53.5), (21, 53.5)], 'fixe', dash=True)
text(ax, 46, 56, '= 8 + 8 + 8 + 8 + 8', 'autre', 'm')
text(ax, 46, 49, 'addition abrégée', 'autre', 's')
text(ax, 75, 56, '= 40', 'resultat', 'l')
# ligne du bas : 8⁵
text(ax, 9, 30, '8', 'sujet', 'l')
text(ax, 11.4, 33.4, '5', 'varie', 's')  # exposant collé au 8, surélevé
line(ax, [(4, 27.5), (21, 27.5)], 'fixe', dash=True)
text(ax, 46, 30, '= 8 × 8 × 8 × 8 × 8', 'sujet', 'm')
text(ax, 46, 23, 'multiplication abrégée', 'sujet', 's')
text(ax, 75, 30, '= 32 768', 'resultat', 'l')
arrow(ax, (16, 53), (11.6, 35.6), 'varie', curve=0.3)
text(ax, 46, 41, 'seule la place du 5 change', 'varie', 's')
text(ax, 44, 10, 'mais 2² et 2 × 2 valent 4', 'limite', 's')
save(fig, '04-026')
