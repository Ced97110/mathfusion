import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 15, 61, 'blocs', 'fixe', 'm', weight='bold')
text(ax, 68, 61, 'mots', 'sujet', 'm', weight='bold')
for y, b, w in [(44, '0', '000'), (28, '1', '111')]:
    box(ax, 10, y, 10, 8, 'fixe', label=b)
    box(ax, 52, y, 32, 8, 'sujet', label=w, weight='bold')
    arrow(ax, (21.5, y + 4), (50.5, y + 4), 'varie')
brace(ax, 10, 20, 28, 'fixe', label=r'$k = 1$')
brace(ax, 52, 84, 28, 'sujet', label=r'$n = 3$')
text(ax, 44, 12, r'$C = \{000,\ 111\}$', 'sujet', 'l', weight='bold')
text(ax, 44, 4, '2 mots, 2 bits de contrôle', 'fixe', 'm')
save(fig, '68-036')
