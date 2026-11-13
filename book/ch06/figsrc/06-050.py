import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
cs, x0, y0 = 6, 8, 16
for k in range(3):
    for i in range(4):
        box(ax, x0 + (k * 4 + i) * cs, y0, cs, cs, 'resultat' if k < 2 else 'fixe', r=0.2)
    xs = x0 + k * 4 * cs
    brace(ax, xs + 0.5, xs + 4 * cs - 0.5, y0, 'fixe' if k == 2 else 'resultat', label='4 €')
brace(ax, x0, x0 + 12 * cs, y0 + cs, 'sujet', label='12 €', down=False)
text(ax, x0 + 4 * cs, 44, r'$\frac{2}{3}$ de 12 € = 8 €', 'resultat', 'l')
text(ax, x0 + 4 * cs, 33, 'garder 2 parts sur 3', 'varie', 's')
save(fig, '06-050')
