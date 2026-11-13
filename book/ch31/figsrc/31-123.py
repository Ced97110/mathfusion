import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
import math
th = math.radians(35); u = 52; ox, oy = 10, 16
P = lambda x, y: (ox + x * u, oy + y * u)
fig, ax = canvas(74)
arc = [P(math.cos(a * math.pi / 180), math.sin(a * math.pi / 180)) for a in range(0, 91, 3)]
line(ax, arc, 'fixe')
O, A, T, H, Pp = P(0, 0), P(1, 0), P(1, math.tan(th)), P(math.cos(th), 0), P(math.cos(th), math.sin(th))
line(ax, [O, A], 'fixe'); line(ax, [A, T], 'fixe'); line(ax, [H, Pp], 'fixe', dash=True)
line(ax, [O, T], 'autre', lw=1.6); line(ax, [O, H], 'sujet', lw=1.8)
for p, s, d in [(O, 'O', (-2.5, -3)), (A, 'A', (2.5, -3)), (T, 'T', (2.5, 2)), (H, 'H', (-2, -3)), (Pp, 'P', (-2.5, 2.2))]:
    text(ax, p[0] + d[0], p[1] + d[1], s, 'encre', 's')
text(ax, 22, 22.5, r'$35^\circ$', 'varie', 's')
brace(ax, O[0], H[0], oy - 4.2, 'sujet', 'OH = 0,8192')
text(ax, 22, 37, 'OT = 1,2208', 'autre', 's')
box(ax, 50, 56, 36, 12, 'resultat', r'OH $\times$ OT = 1', 'm')
save(fig, '31-123')
