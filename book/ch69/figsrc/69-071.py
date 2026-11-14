import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# (x, largeur, role, symbole, cas chiffré, légende)
cols = [(2, 22, 'sujet', r'$f_{j-1}$', r'$x^3-3x+1$', 'dividende'),
        (29, 13, 'varie', r'$q_j$', r'$x/3$', 'quotient'),
        (44, 18, 'autre', r'$f_j$', r'$3x^2-3$', 'diviseur'),
        (68, 18, 'resultat', r'$f_{j+1}$', r'$2x-1$', 'opposé du reste')]
for x, w, role, sym, num, cap in cols:
    box(ax, x, 44, w, 10, role, label=sym)
    box(ax, x, 16, w, 10, role, label=num)
    arrow(ax, (x + w / 2, 44), (x + w / 2, 26.5), 'fixe')
    text(ax, x + w / 2, 59, cap, role, 's')
text(ax, 26.5, 49, '=', 'encre', 'l')
text(ax, 65, 49, '−', 'encre', 'l')
save(fig, '69-071')
