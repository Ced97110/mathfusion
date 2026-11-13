import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
def panel(ytop, eq, vmax, rem, div, lab_rem, lab_div, cap, ineq):
    text(ax, 44, ytop, eq, 'encre', 'm')
    yl = ytop - 16
    f = numberline(ax, 16, 66, yl, 0, vmax, 1, labels=False, arrow_right=False)
    disc(ax, f(rem), yl, 1.8, 'resultat'); disc(ax, f(div), yl, 1.8, 'sujet')
    text(ax, f(rem), yl + 5.5, lab_rem, 'resultat', 's')
    text(ax, f(div), yl + 5.5, lab_div, 'sujet', 's')
    text(ax, 76, yl, ineq, 'encre', 'l')
    text(ax, 40, yl - 7.5, cap, 'fixe', 's')
panel(66, r'$23=4\times5+3$', 4, 3, 4, 'reste 3', 'diviseur 4', 'mesure : valeur absolue', r'$3<4$')
line(ax, [(2, 36.5), (86, 36.5)], 'fixe', lw=0.5)
panel(30, r'$x^2+5x+7=(x+2)(x+3)+1$', 2, 0, 1, 'reste : degré 0', 'diviseur : degré 1', 'mesure : degré', r'$0<1$')
save(fig, '05-177')
