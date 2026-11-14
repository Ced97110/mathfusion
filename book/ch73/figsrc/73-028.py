import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$GL$ : de l’anglais', 'sujet', 'l')
rows = [(44, 'G', 'general', 'général', 'sujet', 'seule condition :\ninversible'),
        (26, 'L', 'linear', 'linéaire', 'sujet', 'transformations\nlinéaires'),
        (8, 'S', 'special', 'spécial', 'autre', 'condition en plus :\ndéterminant 1')]
for y, l, en, fr, role, note in rows:
    box(ax, 3, y, 14, 12, role, label=l, size='xl', weight='bold')
    arrow(ax, (18.5, y + 6), (24, y + 6), 'fixe')
    text(ax, 26, y + 8.5, en, role, 'm', ha='left')
    text(ax, 26, y + 3, '= ' + fr, role, 'm', ha='left')
    text(ax, 56, y + 6, note, 'fixe', 's', ha='left')
save(fig, '73-028')
