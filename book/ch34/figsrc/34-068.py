import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
def frac(x, y, n, d, role, w, size='m'):
    text(ax, x, y + 3.5, n, role, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], role, lw=0.9); text(ax, x, y - 3.5, d, role, size)
text(ax, 18, 66, r'$\tan(A-B)=$', 'sujet', 'l')
frac(60, 66, r'$\tan A-\tan B$', r'$1+\tan A\tan B$', 'sujet', 38)
arrow(ax, (44, 52), (44, 40), 'varie')
text(ax, 50, 46, '45° et 30°', 'varie', 's', ha='left')
frac(26, 26, '1 − 0,5774', '1 + 0,5774', 'fixe', 20, 's')
text(ax, 54, 26, '= 0,2679', 'resultat', 'l')
text(ax, 44, 8, r'0,2679 est $\tan 15°$', 'resultat', 's')
save(fig, '34-068')
