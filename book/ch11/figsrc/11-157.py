import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$P = 2\times L + 2\times l$', 'sujet', 'l')
k = 2.3
def rect(x0, y0, L, l, name):
    box(ax, x0, y0, L * k, l * k, 'varie', r=0.3)
    text(ax, x0 + L * k / 2, y0 + l * k + 3, name, 'varie', 's')
    text(ax, x0 + L * k / 2, y0 - 3.2, f'L = {L}', 'varie', 's')
    text(ax, x0 - 1, y0 + l * k / 2, f'l = {l}', 'varie', 's', ha='right')
rect(15, 26, 12, 8, 'le jardin')
rect(53, 26, 15, 5, 'un autre rectangle')
text(ax, 44, 17, r'$L$ longueur, $l$ largeur : ils changent', 'varie', 's')
line(ax, [(4, 12), (84, 12)], 'fixe', dash=True)
box(ax, 22, 0.5, 26, 8, 'fixe', label=r'$\pi$ = 3,14…', size='m', weight='bold')
text(ax, 52, 4.5, 'ne change pas', 'fixe', 'm', ha='left')
save(fig, '11-157')
