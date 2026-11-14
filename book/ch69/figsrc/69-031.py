import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(86)
text(ax, 22, 81, r'$a$', 'sujet', 'l')
text(ax, 66, 81, r'$a^2$', 'resultat', 'l')
rows = [(r'$3$', r'$9$'), (r'$-4$', r'$16$'), (r'$\frac{1}{2}$', r'$\frac{1}{4}$')]
for i, (a, b) in enumerate(rows):
    y = 62 - 16 * i
    box(ax, 10, y, 24, 11, 'sujet', label=a)
    arrow(ax, (35, y + 5.5), (54, y + 5.5), 'varie')
    box(ax, 55, y, 24, 11, 'resultat', label=b)
line(ax, [(6, 26), (82, 26)], 'fixe', lw=0.6, dash=True)
y = 10
box(ax, 10, y, 24, 11, 'sujet', label=r'$0$')
arrow(ax, (35, y + 5.5), (54, y + 5.5), 'varie')
box(ax, 55, y, 24, 11, 'limite', label=r'$0$')
text(ax, 44, 5, '0 n’est pas positif', 'limite', 's')
save(fig, '69-031')
