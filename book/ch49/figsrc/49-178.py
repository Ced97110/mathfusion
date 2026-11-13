import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
sizes = [1, 4, 4, 2, 4, 1]; d = 3.4; gap = 2.2; pad = 1.1
total = sum(sizes) * d + len(sizes) * 2 * pad + (len(sizes) - 1) * gap
x = (W - total) / 2; y = 30
for k, n in enumerate(sizes, 1):
    w = n * d + 2 * pad
    box(ax, x, y - 4, w, 8, 'fixe')
    for i in range(n): disc(ax, x + pad + d / 2 + i * d, y, 1.4, 'fixe' if i else 'varie')
    cx = x + pad + d / 2
    arrow(ax, (cx, y - 11), (cx, y - 3), 'varie')
    text(ax, cx, y - 14, rf'$x_{k}$', 'varie', 'm', weight='bold')
    text(ax, x + w / 2, y + 7, f'{k}', 'fixe', 's')
    x += w + gap
text(ax, W / 2, y + 12, 'orbite numéro i', 'fixe', 's')
text(ax, W / 2, 7, r'$x_i$ : le point choisi dans l’orbite $i$', 'varie', 'm')
save(fig, '49-178')
