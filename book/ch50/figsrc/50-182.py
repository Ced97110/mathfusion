import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
w, g = 6.0, 0.8; x0 = (88 - (12 * w + 11 * g)) / 2; y = 34
for i in range(12):
    box(ax, x0 + i * (w + g), y, w, 9, 'sujet' if i < 8 else 'resultat', r=0.5)
xa, xb, xc = x0, x0 + 8 * w + 7 * g, x0 + 8 * (w + g)
brace(ax, xa, xb, y + 10, 'sujet', label='8 éléments d’ordre 3', down=False)
brace(ax, xc, x0 + 12 * w + 11 * g, y - 1, 'resultat', label='4 restants', down=True)
text(ax, 44, 60, r'$12 - 8 = 4$', 'encre', 'l')
arrow(ax, (62, 22), (62, 17.5), 'resultat')
box(ax, 22, 3, 62, 14, 'resultat', label='un 2-Sylow : 4 éléments\n' + r'$n_2 = 1$ : unique', size='m')
save(fig, '50-182')
