import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
u = 3.2; x0 = 10; y0 = 30
for i in range(7):
    for j in range(20):
        box(ax, x0 + j * u, y0 + i * u, u, u, 'sujet' if j < 19 else 'varie', lw=0.3, r=0.1)
brace(ax, x0, x0 + 20 * u, y0 + 7 * u, 'fixe', label='20', down=False)
brace(ax, x0, x0 + 19 * u, y0, 'sujet', label='19')
arrow(ax, (6, y0), (6, y0 + 7 * u), 'fixe', both=True); text(ax, 3, y0 + 3.5 * u, '7', 'encre', 'm')
cx = x0 + 19.5 * u
text(ax, 77, 22, r'$7 \times 1 = 7$ retiré', 'varie', 's')
arrow(ax, (cx + 4, 25), (cx, y0 - 0.5), 'varie')
text(ax, 44, 11, r'$7 \times 20 - 7 \times 1 = 140 - 7 = 133$', 'resultat', 'm')
save(fig, '10-053')
