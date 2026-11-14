import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
old = [r'$x^3-3x+1$', r'$3x^2-3$', r'$2x-1$', '9/4']
new = [r'$x^3-3x+1$', r'$3x^2-3$', r'$18x-9$', '729']
fac = [r'$\times1$', r'$\times1$', r'$\times9$', r'$\times324$']
text(ax, 44, 70, 'partie précédente', 'fixe', 's')
text(ax, 44, 6, r'cas $I$, $p=-3$, $q=1$', 'sujet', 's')
for i in range(4):
    x = 2 + 21 * i
    box(ax, x, 50, 19, 11, 'fixe', label=old[i], size='s')
    box(ax, x, 18, 19, 11, 'sujet', label=new[i], size='s')
    arrow(ax, (x + 9.5, 49.5), (x + 9.5, 29.5), 'varie')
    text(ax, x + 11, 39.5, fac[i], 'varie', 's', ha='left')
save(fig, '69-128')
