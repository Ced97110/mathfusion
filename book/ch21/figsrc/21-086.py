import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
def frac(cx, num, den, role):
    text(ax, cx, 60, num, role, 'xl')
    line(ax, [(cx - 14, 54.5), (cx + 14, 54.5)], role, lw=1.2)
    box(ax, cx - 12, 41, 24, 11, 'varie', True, den, size='l')
frac(21, '4', r'$x-1$', 'sujet'); frac(67, '2', r'$x+6$', 'autre')
text(ax, 44, 54.5, r'$=$', 'encre', 'xl')
text(ax, 44, 34, 'x est au bas des deux', 'varie', 's')
text(ax, 44, 18, r'essai $x=3$ : $2\ \neq\ \frac{2}{9}$', 'fixe', 's')
save(fig, '21-086')
