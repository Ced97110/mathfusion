import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
line(ax, [(44, 6), (44, 80)], 'fixe', dash=True)
for x, f in [(22, r'$\frac{3}{4}$'), (66, r'$\frac{1}{3}$')]:
    box(ax, x - 9, 62, 18, 17, 'sujet', label=f, size='l')
    arrow(ax, (x, 61), (x, 50), 'varie')
    text(ax, x + 11, 56, 'haut ÷ bas', 'varie', 's')
text(ax, 22, 44, r'$3\div 4$', 'sujet', 'l'); text(ax, 66, 44, r'$1\div 3$', 'sujet', 'l')
text(ax, 8, 28, '0,', 'sujet', 'l')
for i, d in enumerate('75'):
    box(ax, 14 + 9 * i, 23, 8, 10, 'resultat', label=d, size='l')
text(ax, 50, 28, '0,', 'sujet', 'l')
for i in range(3):
    box(ax, 56 + 9 * i, 23, 8, 10, 'limite', label='3', size='l')
text(ax, 85, 26, '…', 'limite', 'l')
text(ax, 22, 12, 'se termine', 'resultat', 's'); text(ax, 66, 12, 'ne se termine pas', 'limite', 's')
save(fig, '08-040')
