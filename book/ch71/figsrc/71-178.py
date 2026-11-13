import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(72)
def mat(x, y, vals, role):
    cw, ch = 9, 7
    for k, v in enumerate(vals):
        text(ax, x + (k % 2) * cw + cw / 2, y + ch - (k // 2) * ch - ch / 2 + ch * 0 + 0, v, role, 'm')
    for sx in (x - 0.5, x + 2 * cw + 0.5):
        d = 1.2 if sx < x else -1.2
        line(ax, [(sx + d, y + 2 * ch - 0.2 - ch), (sx, y + 2 * ch - 0.2 - ch), (sx, y - ch + 0.2), (sx + d, y - ch + 0.2)], role)
mat(6, 62, ['1', '2', '2', '1'], 'sujet')
text(ax, 15, 70, '$C$', 'sujet', 's')
arrow(ax, (28, 59), (48, 59), 'varie')
text(ax, 38, 64, '$P^TCP$', 'varie', 's')
mat(58, 62, ['6', '0', '0', '−2'], 'resultat')
cx, cy, k = 44, 25, 9
arrow(ax, (cx - 30, cy), (cx + 32, cy), 'fixe', lw=0.7)
arrow(ax, (cx, cy - 20), (cx, cy + 20), 'fixe', lw=0.7)
a, b = math.sqrt(4 / 6), math.sqrt(2)
for sg in (1, -1):
    pts = [(cx + sg * a * k * math.cosh(t / 10), cy + b * k * math.sinh(t / 10)) for t in range(-10, 11)]
    line(ax, pts, 'sujet', lw=1.3)
    disc(ax, cx + sg * a * k, cy, 0.9, 'resultat')
text(ax, cx + 30, cy - 4, 'axe de $u_1$', 'fixe', 's')
text(ax, 67, 45, 'diag(6, −2)', 'resultat', 's')
text(ax, cx + 22, cy + 4, '2 sommets', 'resultat', 's')
text(ax, cx - 8, 3, '$6s^2-2t^2=4$', 'sujet', 'm')
save(fig, '71-178')
