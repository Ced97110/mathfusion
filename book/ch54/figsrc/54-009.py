import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 68, r'$2-x+3x^3$', 'encre', 'l')
arrow(ax, (44, 64), (44, 58), 'varie')
vals = ['2', '−1', '0', '3']
pos = [r'$x^0$', r'$x^1$', r'$x^2$', r'$x^3$']
for i in range(4):
    x0 = 12 + 18 * i
    text(ax, x0 + 8, 52, pos[i], 'fixe', 'm')
    absent = vals[i] == '0'
    box(ax, x0, 36, 16, 12, 'fixe' if absent else 'sujet', label=vals[i], size='l', dash=absent)
brace(ax, 12, 82, 35, 'sujet', label='la liste : 2, −1, 0, 3')
text(ax, 44, 20, r'$3x^3-x+2$ : même liste', 'resultat', 's')
save(fig, '54-009')
