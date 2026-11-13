import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
text(ax, 21, 87, 'équation', 'encre', 's'); text(ax, 67, 87, 'avec $x=3$', 'resultat', 's')
L = [r'$2x+(5-x)=8$', r'$2x+5-x=8$', r'$x+5=8$', r'$x=3$']
R = [r'$6+2=8$', r'$6+5-3=8$', r'$3+5=8$', r'$3=3$']
for i in range(4):
    yb = 68 - i * 20
    box(ax, 2, yb, 38, 10, 'sujet', label=L[i]); box(ax, 52, yb, 34, 10, 'resultat', label=R[i])
    arrow(ax, (40, yb + 5), (52, yb + 5), 'fixe')
    if i < 3: arrow(ax, (21, yb), (21, yb - 10), 'varie')
save(fig, '24-043')
