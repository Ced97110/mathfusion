import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'entiers $a+b\sqrt{2}$', 'encre', 's')
def card(x, el, n, inv, role):
    box(ax, x, 12, 40, 41, role, fill=True)
    text(ax, x + 20, 46, el, role, 'm', weight='bold'); text(ax, x + 20, 36, n, 'encre', 'm')
    text(ax, x + 20, 26, 'inverse :', 'encre', 's'); text(ax, x + 20, 19, inv, role, 's')
card(2, r'$3+2\sqrt{2}$', r'$N=1$', 'entier', 'resultat')
card(46, r'$1+3\sqrt{2}$', r'$N=-17$', 'des fractions', 'limite')
save(fig, '77-147')
