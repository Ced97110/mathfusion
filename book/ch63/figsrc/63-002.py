import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 67, r'le carré du nouveau nombre doit valoir $2$', 'varie', 'm')
text(ax, 13, 59, 'à la place de', 'fixe', 's')
text(ax, 50, 59, 'son carré', 'fixe', 's')
rows = [(r'$\sqrt{2}$', 'sujet', r'$(\sqrt{2})^2=2$' + '\nvrai', 'resultat'),
        (r'$-\sqrt{2}$', 'varie', r'$(-\sqrt{2})^2=2$' + '\nvrai', 'resultat'),
        (r'$5\sqrt{2}$', 'varie', r'$(5\sqrt{2})^2=50$' + '\nfaux : pas $2$', 'limite')]
for i, (a, ra, b, rb) in enumerate(rows):
    y = 40 - 19 * i
    box(ax, 2, y, 22, 14, ra, label=a)
    arrow(ax, (25, y + 7), (31, y + 7), 'fixe')
    box(ax, 32, y, 54, 14, rb, label=b, size='s')
save(fig, '63-002')
