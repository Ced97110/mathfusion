import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
f = numberline(ax, 8, 68, 44, -3, 2, 1)
disc(ax, f(-2), 47.4, 1.4, 'sujet')
text(ax, f(-2), 51.5, 'simple', 'sujet', 's')
disc(ax, f(1), 47.4, 1.4, 'varie')
disc(ax, f(1), 50.4, 1.4, 'varie')
text(ax, f(1), 55, 'double', 'varie', 's')
text(ax, 44, 62, r'$h=(x-1)^2(x+2)$', 'encre', 'm')
text(ax, 44, 32, 'la suite de Sturm de $h$', 'encre', 'm')
w, g = 24.0, 5.0
x0 = (88 - 3 * w - 2 * g) / 2
labs = [r'$h_0=h$', r'$h_1=3x^2-3$', r'$h_2=2x-2$']
for i in range(3):
    box(ax, x0 + i * (w + g), 14, w, 12, 'sujet' if i < 2 else 'varie', label=labs[i], size='s')
    if i < 2:
        arrow(ax, (x0 + i * (w + g) + w + 0.5, 20), (x0 + (i + 1) * (w + g) - 0.5, 20), 'fixe')
brace(ax, x0 + 2 * (w + g), x0 + 2 * (w + g) + w, 14, 'varie', label=r'$s=2$')
save(fig, '69-107')
