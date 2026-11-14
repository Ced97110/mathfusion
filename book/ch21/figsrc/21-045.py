import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 7.0; x0, y0 = 4, 22
for i in range(7):
    for j in range(3):
        poly(ax, [(x0 + i * u, y0 + j * u), (x0 + (i + 1) * u, y0 + j * u), (x0 + (i + 1) * u, y0 + (j + 1) * u), (x0 + i * u, y0 + (j + 1) * u)], 'sujet' if i < 5 else 'varie', lw=0.5)
brace(ax, x0, x0 + 7 * u, y0 + 3 * u, down=False, label=r'largeur $a+b=7$')
text(ax, x0 + 7 * u + 3, y0 + 1.5 * u + 3, 'hauteur', 'sujet', 's', ha='left')
text(ax, x0 + 7 * u + 3, y0 + 1.5 * u - 1, r'$a-b=3$', 'sujet', 's', ha='left')
text(ax, 28, 16, 'aire = 21 cases', 'sujet', 's')
box(ax, 14, 2, 60, 9, 'resultat', label=r'$21\div3=7$ = largeur', size='s')
save(fig, '21-045')
