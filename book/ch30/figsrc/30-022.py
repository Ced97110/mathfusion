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

fig, ax = canvas(62)
X0, Y0, SX, SY = 3, 22, 5.8, 13
X = lambda t: X0 + t * SX
Y = lambda v: Y0 + v * SY
arrow(ax, (X0, Y0), (86, Y0), 'fixe', lw=0.8)
curve(ax, np.sin, 0, 14.1, X, Y, 'sujet', 1.1, 400)
v = np.sin(1.0)
line(ax, [(X(1), Y(v)), (X(1 + 4 * PI), Y(v))], 'fixe', lw=0.6, dash=True)
labs = [r'$x=1$', r'$x+2\pi$', r'$x+4\pi$']
for k in range(3):
    tx = 1 + 2 * PI * k
    line(ax, [(X(tx), Y0), (X(tx), Y(v))], 'fixe', lw=0.6, dash=True)
    dot(ax, X(tx), Y(v), 'resultat', 1.3)
    text(ax, X(tx), Y0 - 4, labs[k], 'encre', 's')
text(ax, 27, Y(v) + 2.5, '0,8415', 'resultat', 's')
yb = Y0 + SY + 3
brace(ax, X(1), X(1 + 2 * PI), yb, 'varie', r'$p=2\pi$ : le plus petit pas', down=False)
brace(ax, X(1), X(1 + 4 * PI), yb + 9, 'fixe', r'$4\pi$ marche aussi, mais plus grand', down=False)
save(fig, '30-022')
