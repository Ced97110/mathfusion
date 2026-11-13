import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
u = 2.6
def sq(x, y, n, role):
    ax.add_patch(Rectangle((x, y), n * u, n * u, ec=COL[role], fc=FILL[role], lw=0.8, zorder=2))
    text(ax, x + n * u / 2, y + n * u / 2, str(n * n), role, 's')
# l'énoncé général
text(ax, 44, 86, r'$(a^2+b^2)(c^2+d^2)=(ac-bd)^2+(ad+bc)^2$', 'encre', 's')
text(ax, 44, 80, 'deux sommes de deux carrés : le produit en est une', 'fixe', 's')
rows = [(67, r'$2=1^2+1^2$', (1, 1), 'sujet'),
        (51, r'$13=2^2+3^2$', (2, 3), 'autre'),
        (34, r'$26=5^2+1^2$', (5, 1), 'resultat')]
for c, lab, (a, b), role in rows:
    h = max(a, b) * u
    text(ax, 3, c, lab, role, 's', ha='left')
    sq(40, c - h / 2, a, role); sq(40 + a * u + 3, c - h / 2, b, role)
text(ax, 73, 59, r'$2\times13=26$', 'fixe', 's')
arrow(ax, (73, 56), (73, 40), 'fixe', lw=0.9)
text(ax, 73, 36, 'encore deux carrés', 'resultat', 's')
box(ax, 3, 4, 38, 14, 'resultat', label='2 nombres : oui', size='s')
box(ax, 45, 4, 40, 14, 'fixe', label='avec 3, 4, 5 nombres\nau lieu de 2 : encore vrai ?', size='s', dash=True)
save(fig, '39-144')
