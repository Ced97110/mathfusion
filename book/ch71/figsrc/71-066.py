import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
rows = [(62, r'$x=(2\,;\,1)$', r'$(3\,;\,1)$'), (40, r'$y=(1\,;\,0)$', r'$(1\,;\,1)$')]
for y, a, b in rows:
    box(ax, 2, y, 24, 9, 'sujet', label=a)
    arrow(ax, (26, y + 4.5), (39, y + 4.5), 'varie')
    text(ax, 32.5, y + 8, r'$P$', 'varie', 's')
    box(ax, 39, y, 20, 9, 'fixe', label=b)
box(ax, 66, 42, 20, 28, 'fixe', label=r'$A$', size='l')
text(ax, 76, 74, 'forme', 'fixe', 's')
arrow(ax, (59, 66.5), (66, 60), 'fixe'); arrow(ax, (59, 44.5), (66, 52), 'fixe')
arrow(ax, (76, 42), (76, 22), 'varie')
box(ax, 62, 10, 24, 12, 'resultat', label=r'$7$', size='l')
text(ax, 32, 22, 'deux vecteurs en entrée', 'sujet', 's')
text(ax, 31, 14, 'un nombre en sortie :', 'resultat', 's')
text(ax, 31, 8, r'rien à reconvertir', 'resultat', 's')
save(fig, '71-066')
