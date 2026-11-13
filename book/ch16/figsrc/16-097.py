import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
verbs = ['est', 'vaut', 'donne', 'égale']
for i, v in enumerate(verbs):
    x = 3 + i * 21
    box(ax, x, 44, 19, 8, 'fixe', label=v)
    arrow(ax, (x + 9.5, 44), (44, 33), 'fixe', lw=0.8)
text(ax, 44, 56.5, 'quatre façons de dire', 'fixe', 's')
text(ax, 28, 26, r'$x + 3$', 'sujet', 'xl')
text(ax, 44, 26, r'$=$', 'varie', 'xl', weight='bold')
text(ax, 58, 26, r'$7$', 'sujet', 'xl')
brace(ax, 20, 36, 20, 'sujet', 'un côté')
brace(ax, 52, 64, 20, 'sujet', 'l’autre côté')
text(ax, 44, 6, 'un seul signe, un même nombre', 'resultat', 's')
save(fig, '16-097')
