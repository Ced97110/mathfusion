import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cs, x0, y0 = 5.5, 6, 12
for i in range(5):
    for j in range(7):
        box(ax, x0 + i * cs, y0 + j * cs, cs, cs, 'resultat' if (i < 2 and j < 3) else 'fixe', r=0.2)
brace(ax, x0, x0 + 2 * cs, y0, 'resultat', label='2 sur 5')
text(ax, x0 + 5 * cs + 2, y0 + 1.5 * cs, '3 sur 7', 'resultat', 's', ha='left')
xb, wb, hb = 50, 36, 10
box(ax, xb, 46, wb, hb, 'resultat', label=r'hauts : $2\times3=6$')
box(ax, xb, 28, wb, hb, 'sujet', label=r'bas : $5\times7=35$')
box(ax, xb, 8, wb, hb, 'encre', label=r'résultat $\frac{6}{35}$')
arrow(ax, (xb + wb / 2, 46), (xb + wb / 2, 38.5), 'varie')
arrow(ax, (xb + wb / 2, 28), (xb + wb / 2, 18.5), 'varie')
text(ax, 20, 58, r'$\frac{2}{5}\times\frac{3}{7}$', 'encre', 'l')
save(fig, '06-053')
