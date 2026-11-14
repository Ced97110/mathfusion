import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def row(y, title, a, b, ra, rb):
    text(ax, 44, y + 14, title, 'sujet', 's')
    box(ax, 4, y, 18, 9, ra, label=a)
    text(ax, 27, y + 4.5, r'$\times$', 'fixe', 'l')
    box(ax, 32, y, 18, 9, rb, label=b)
    text(ax, 55, y + 4.5, '=', 'fixe', 'l')
    box(ax, 60, y, 18, 9, 'resultat', label='6')
row(40, r'$\mathbb{Z}/6\supset\{0,2,4\}\supset\{0\}$', r'$\mathbb{Z}/2$', r'$\mathbb{Z}/3$', 'sujet', 'autre')
row(20, r'$\mathbb{Z}/6\supset\{0,3\}\supset\{0\}$', r'$\mathbb{Z}/3$', r'$\mathbb{Z}/2$', 'autre', 'sujet')
text(ax, 44, 7, r'$6=2\times3$ dans les deux cas', 'resultat', 's', weight='bold')
save(fig, '64-078')
