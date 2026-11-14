import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 2, 62, 24, 12, 'sujet', label=r'$3x^2-3$')
text(ax, 28.5, 68, '=', 'encre', 'l')
box(ax, 31, 62, 28, 12, 'varie', label=r'$3x/2+3/4$')
text(ax, 61.5, 68, '×', 'encre', 'l')
box(ax, 64, 62, 22, 12, 'autre', label=r'$2x-1$')
box(ax, 2, 40, 40, 12, 'fixe', label=r'reste $-9/4$')
arrow(ax, (42.5, 45), (53.5, 45), 'varie')
text(ax, 48, 51, 'signe\nrenversé', 'varie', 's')
box(ax, 54, 40, 32, 12, 'resultat', label=r'$f_3=9/4$')
text(ax, 44, 27, 'degré : 3, 2, 1, 0', 'fixe', 's')
for k in range(4):
    cx = 14 + 20 * k
    box(ax, cx - 7, 10, 14, 3 * (3 - k + 1), 'resultat' if k == 3 else 'sujet')
    text(ax, cx, 5.5, r'$f_%d$' % k, 'encre', 's')
save(fig, '69-085')
