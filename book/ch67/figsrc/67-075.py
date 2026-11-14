import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
# left: char 2, (a+b)^4 by squaring twice ; right: exponent 3 fails in the field with 4 elements
text(ax, 23, 75, 'caractéristique 2', 'resultat', 's')
chain = [r'$(a+b)^4$', r'$((a+b)^2)^2$', r'$(a^2+b^2)^2$', r'$a^4+b^4$']
for k, t in enumerate(chain):
    y = 58 - k * 18
    box(ax, 3, y, 40, 11, 'resultat' if k == 3 else 'sujet', label=t, size='m')
    if k < 3: arrow(ax, (23, y - 0.5), (23, y - 6.5), 'varie')
line(ax, [(46, 6), (46, 76)], 'fixe', dash=True)
text(ax, 66, 75, 'exposant 3', 'limite', 's')
box(ax, 49, 54, 36, 12, 'sujet', label=r'$(1+\alpha)^3 = 1$', size='s')
text(ax, 67, 44, r'$\neq$', 'limite', 'l')
box(ax, 49, 24, 36, 12, 'sujet', label=r'$1^3 + \alpha^3 = 0$', size='s')
text(ax, 67, 14, '3 n\'est pas\nune puissance de 2', 'limite', 's')
save(fig, '67-075')
