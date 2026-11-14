import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

rows = [(r'$x^2-5x+6$', 5, 6, r'$5^2-4\times 6$'), (r'$x^2-2$', 0, -2, r'$0^2-4(-2)$'), (r'$x^2-4$', 0, -4, r'$0^2-4(-4)$')]
exp = [1, 8, 16]
fig, ax = canvas(86)
text(ax, 44, 81, r'$d=a_1^2-4a_2$', 'sujet', 'xl', weight='bold')
text(ax, 44, 73, r'$a_1$ : somme des racines, $a_2$ : produit', 'fixe', 's')
box(ax, 32, 10, 30, 56, 'sujet', dash=True, fill=False)
text(ax, 47, 62, r'$a_1^2-4a_2$', 'sujet', 's', weight='bold')
for k, ((p, a1, a2, calc), e) in enumerate(zip(rows, exp)):
    assert a1 * a1 - 4 * a2 == e
    y = 44 - k * 15
    box(ax, 2, y, 26, 10, 'fixe', label=p, size='s')
    text(ax, 47, y + 5, calc, 'varie', 's')
    arrow(ax, (28.4, y + 5), (34, y + 5), 'fixe', lw=0.8)
    arrow(ax, (62.4, y + 5), (66, y + 5), 'fixe', lw=0.8)
    box(ax, 66, y, 20, 10, 'resultat', label='d = %d' % e, size='s', weight='bold')
text(ax, 44, 4, 'la forme ne change pas', 'resultat', 's')
save(fig, '65-048')
