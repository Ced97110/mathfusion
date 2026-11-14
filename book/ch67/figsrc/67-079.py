import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
# field with 5 elements, z = 2 : z, z^2, z^3, z^4 = 2, 4, 3, 1
text(ax, 44, 65, r'$z = 2$ ; $q = 5$, $q - 1 = 4$', 'sujet', 'm')
P = [r'$z$', r'$z^2$', r'$z^3$', r'$z^4$']
V = ['2', '4', '3', '1']
for k in range(4):
    x = 4 + k * 21
    box(ax, x, 44, 19, 11, 'sujet', label=P[k])
    arrow(ax, (x + 9.5, 43), (x + 9.5, 34), 'varie')
    box(ax, x, 22, 19, 11, 'resultat', label=V[k])
brace(ax, 4, 85, 20, 'resultat', label='tous les non nuls, une fois', size='s')
save(fig, '67-079')
