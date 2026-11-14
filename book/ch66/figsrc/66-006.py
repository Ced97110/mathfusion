import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
u = 14.0; cx, cy = 22, 33
disc(ax, cx, cy, u, 'sujet')
line(ax, [(cx, cy), (cx + u, cy)], 'varie', lw=1.2)
text(ax, cx + u / 2, cy - 3, 'rayon 1', 'varie', 's')
text(ax, cx, cy + 6, r'aire $\pi$', 'sujet', 'm')
text(ax, cx, cy - u - 5, 'cercle', 'sujet', 'm')
s = u * math.sqrt(math.pi); x0 = 50
box(ax, x0, cy - s / 2, s, s, 'autre')
text(ax, x0 + s / 2, cy, r'aire $\pi$', 'autre', 'm')
brace(ax, x0, x0 + s, cy - s / 2 - 1.5, 'autre', label=r'côté $\sqrt{\pi}$')
text(ax, 43, cy, '=', 'fixe', 'l')
text(ax, x0 + s / 2, cy + s / 2 + 4, 'carré de même aire', 'autre', 's')
save(fig, '66-006')
