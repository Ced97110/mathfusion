import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
PI = np.pi
def curve(ax, f, a, b, X, Y, role='sujet', lw=1.2, n=240):
    t = np.linspace(a, b, n); ax.plot(X(t), Y(f(t)), color=COL[role], lw=lw, zorder=3, solid_capstyle='round')
def arc(ax, cx, cy, r, a0, a1, role='varie', lw=1.4, head=True):
    t = np.linspace(a0, a1, 200); xs = cx + r * np.cos(t); ys = cy + r * np.sin(t)
    ax.plot(xs, ys, color=COL[role], lw=lw, zorder=3, solid_capstyle='round')
    if head: arrow(ax, (xs[-4], ys[-4]), (xs[-1], ys[-1]), role, lw=lw)
def circ(ax, cx, cy, r, role='fixe'):
    t = np.linspace(0, 2 * PI, 300); ax.plot(cx + r * np.cos(t), cy + r * np.sin(t), color=COL[role], lw=1.0, zorder=2)
def dot(ax, x, y, role, r=1.1):
    ax.add_patch(Circle((x, y), r, fc=COL[role], ec=COL[role], zorder=4))

fig, ax = canvas(52)
x0, x1, y = 16, 70, 24
f = numberline(ax, x0, x1, y, -2, 2, 1, labels=False, arrow_right=True)
text(ax, 44, 46, r'$x=k\pi$, $k$ entier relatif', 'sujet', 'm')
ks = [-2, -1, 0, 1, 2]
xs_lab = [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$']
for k, lab in zip(ks, xs_lab):
    dot(ax, f(k), y, 'resultat', 1.3)
    line(ax, [(f(k), y + 2), (f(k), y + 8)], 'fixe', lw=0.5, dash=True)
    text(ax, f(k), y + 11, f'{k}'.replace('-', '\u2212'), 'varie', 'm')
    text(ax, f(k), y - 5, lab, 'sujet', 's')
text(ax, 7, y + 11, '$k$', 'varie', 's')
text(ax, 7, y - 5, '$x$', 'sujet', 's')
save(fig, '30-032')
