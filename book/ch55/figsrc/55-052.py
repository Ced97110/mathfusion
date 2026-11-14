import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 65, r'$f = x_1 x_2^2 + (x_1+1)\,x_2 + 2$', 'sujet', 'm')
arrow(ax, (44, 61), (44, 49), 'varie')
text(ax, 48, 55, r'ranger selon $x_2$', 'varie', 's', ha='left')
for k, (lab, p) in enumerate([(r'$B_0 = 2$', r'devant $x_2^0$'), (r'$B_1 = x_1 + 1$', r'devant $x_2^1$'), (r'$B_2 = x_1$', r'devant $x_2^2$')]):
    x = 4 + k * 29
    box(ax, x, 35, 24, 11, 'sujet', label=lab, size='s')
    text(ax, x + 12, 30.5, p, 'fixe', 's')
brace(ax, 4, 82, 26, 'sujet', label=r'polynômes en $x_1$ : $r-1$ variables')
text(ax, 44, 7, r'$f = B_0 + B_1 x_2 + B_2 x_2^2$', 'resultat', 'm')
save(fig, '55-052')
