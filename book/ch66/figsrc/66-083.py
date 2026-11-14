import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
vals = [1, 2, 2, 4 / 3, 2 / 3, 4 / 15, 4 / 45, 8 / 315]
labs = ['1', '2', '2', r'$\frac{4}{3}$', r'$\frac{2}{3}$', r'$\frac{4}{15}$', r'$\frac{4}{45}$', r'$\frac{8}{315}$']
w, p, y0, sc = 8.0, 10.2, 18.0, 14.0
text(ax, 44, 67, r'$e^u$ pour $u=2$ : les termes $\frac{2^k}{k!}$', 'sujet', 's')
for i, (v, l) in enumerate(zip(vals, labs)):
    x = 3 + i * p
    box(ax, x, y0, w, max(v * sc, 0.5), 'varie', r=0.2, lw=0.6)
    text(ax, x + w / 2, y0 - 5, l, 'encre', 's')
brace(ax, 3, 3 + 7 * p + w, 53, 'sujet', None, down=False, depth=3)
text(ax, 44, 61, r'somme $\approx 7{,}381$', 'sujet', 'm')
text(ax, 44, 5, r'on s’approche de $7{,}389\approx e^2$', 'resultat', 's')
save(fig, '66-083')
