import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
for i in range(2):
    box(ax, 12 + i * 9, 72, 8, 9, 'fixe', r=0.5)
for i in range(5):
    box(ax, 30 + i * 8, 58, 7, 9, 'fixe', r=0.5)
text(ax, 18, 69, 'degré 2 : 2 termes', 'fixe', 's')
text(ax, 50, 54, 'degré 3 : 5 termes', 'fixe', 's')
box(ax, 54, 72, 32, 9, 'fixe', dash=True, fill=False, label='degré 4 : plus long', size='s')
arrow(ax, (44, 50), (44, 43), 'varie')
# tableau de nombres : coefficients de f = x^2 - a1 x + a2 et de f' = 2x - a1 (degré 2)
cells = [['1', r'$-a_1$', r'$a_2$'], ['2', r'$-a_1$', '0'], ['0', '2', r'$-a_1$']]
for r in range(3):
    for c in range(3):
        box(ax, 22 + c * 11, 32 - r * 10, 10, 9, 'sujet', r=0.4, label=cells[r][c], size='s')
text(ax, 38, 7, r"résultant de $f$ et $f'$", 'sujet', 's')
arrow(ax, (56, 27), (65, 27), 'varie')
box(ax, 66, 21, 20, 12, 'resultat', label=r'$d$', size='l')
save(fig, '65-151')
