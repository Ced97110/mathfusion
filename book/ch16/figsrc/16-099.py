import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
words = ['quatre fois', 'un nombre', 'est', 'seize']
signs = [r'$4\times$', r'$x$', r'$=$', r'$16$']
roles = ['varie', 'sujet', 'sujet', 'fixe']
for i in range(4):
    c = 11 + i * 22
    box(ax, c - 10, 48, 20, 8, 'fixe', label=words[i], size='s')
    arrow(ax, (c, 48), (c, 38), 'varie', lw=0.9)
    text(ax, c, 33, signs[i], 'sujet', 'xl')
brace(ax, 3, 85, 28, 'resultat', None)
text(ax, 44, 19, r'$4x = 16$', 'resultat', 'xl')
text(ax, 44, 8, 'relue : « quatre fois un nombre est seize »', 'resultat', 's')
save(fig, '16-099')
