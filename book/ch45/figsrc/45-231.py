import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 22, 75, r'$S_3$', 'sujet', 'l', weight='bold')
text(ax, 68, 75, r'$\mathbb{Z}/6$', 'autre', 'l', weight='bold')
for i, (a, b) in enumerate([('échange puis décalage', 'échange 1 et 3'), ('décalage puis échange', 'échange 2 et 3')]):
    y = 54 - i * 24
    box(ax, 2, y, 40, 16, 'sujet')
    text(ax, 22, y + 11.5, a, 'sujet', 's'); text(ax, 22, y + 4.5, b, 'varie', 'm', weight='bold')
text(ax, 22, 50, r'$\neq$', 'limite', 'l', weight='bold')
text(ax, 22, 22, 'l’ordre change le résultat', 'limite', 's')
for i, s in enumerate([r'$2+3=5$', r'$3+2=5$']):
    box(ax, 48, 54 - i * 24, 38, 16, 'autre', label=s, size='l')
text(ax, 67, 50, r'$=$', 'resultat', 'l', weight='bold')
text(ax, 67, 22, 'même résultat', 'resultat', 's')
save(fig, '45-231')
