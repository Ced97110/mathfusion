import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 22, 56, 'dans ℤ', 'sujet', 'l'); text(ax, 66, 56, 'dans ℤ[x]', 'autre', 'l')
for y, a in ((36, '2 et 4'), (14, '6 et 10')):
    box(ax, 4, y, 15, 10, 'sujet', label=a, size='s'); arrow(ax, (20, y + 5), (25, y + 5), 'varie')
    box(ax, 26, y, 14, 10, 'resultat', label='2 seul', size='s')
box(ax, 48, 36, 15, 10, 'autre', label=r'2 et $x$', size='s'); arrow(ax, (64, 41), (69, 41), 'varie')
box(ax, 70, 36, 14, 10, 'autre', label=r'un $g$ ?', size='s', dash=True)
text(ax, 66, 22, 'à tester : pas', 'fixe', 's'); text(ax, 66, 17, 'acquis comme dans ℤ', 'fixe', 's')
save(fig, '52-294')
