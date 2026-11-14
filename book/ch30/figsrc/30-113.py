import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(104)
rows = [(r'1. $x-C$ : $1-2$', r'$-1$'), (r'2. $\times B$ : $\times\,\pi/4$', r'$\approx-0{,}785$'),
        (r'3. $\sin$', r'$\approx-0{,}707$'), (r'4. $\times A$ : $\times\,20$', r'$\approx-14{,}14$'),
        (r'5. $+D$ : $+\,22$', r'$\approx 7{,}86$')]
text(ax, 44, 99, r'on part de $x=1$', 'sujet', 'm')
y0 = 80
for i, (op, val) in enumerate(rows):
    y = y0 - i * 17
    last = i == 4
    box(ax, 4, y, 44, 9, 'varie', label=op)
    arrow(ax, (48, y + 4.5), (56, y + 4.5), 'fixe')
    box(ax, 56, y, 30, 9, 'resultat' if last else 'sujet', label=val)
    if i < 4:
        arrow(ax, (71, y), (71, y - 8), 'fixe')
text(ax, 44, 4, 'de l’intérieur vers l’extérieur', 'encre', 's')
save(fig, '30-113')
