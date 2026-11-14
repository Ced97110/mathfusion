import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wave(ax, f, x0, w, y0, k, role, lw=1.1, dash=False, n=300, t1=2 * math.pi):
    line(ax, [(x0 + w * i / n, y0 + k * f(t1 * i / n)) for i in range(n + 1)], role, lw, dash)

fig, ax = canvas(78)
f = numberline(ax, 14, 70, 64, 440, 442, 1, arrow_right=False, size='s')
disc(ax, f(440), 64, 1.8, 'sujet'); disc(ax, f(442), 64, 1.8, 'autre')
text(ax, f(440) + 2, 70, 'diapason 440', 'sujet', 's'); text(ax, f(442) - 2, 70, 'corde 442', 'autre', 's')
brace(ax, f(440), f(442), 57, 'varie', r'$442-440=2$', True, 's')
base, k = 14, 16
wave(ax, lambda t: abs(math.sin(t)), 14, 56, base, k, 'varie', 1.3, t1=2 * math.pi)
numberline(ax, 14, 70, base, 0, 1, 0.5, arrow_right=False, size='s')
text(ax, f(440) + 14, base + k + 3, '1', 'varie', 's'); text(ax, f(440) + 42, base + k + 3, '2', 'varie', 's')
text(ax, 42, 4, 'une seconde : 2 montées du volume', 'fixe', 's')
save(fig, '35-004')
