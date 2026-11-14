import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(72)
X = lambda v: 10 + v * 11
for mid, fn, role, lab in ((56, lambda t: math.sin(t), 'fixe', r'$\sin x$'), (28, lambda t: math.sin(2 * t), 'sujet', r'$\sin(2x)$')):
    Yf = lambda v, m=mid: m + 8 * v
    line(ax, [(X(0), mid), (X(2 * math.pi), mid)], 'fixe', lw=0.5)
    curve(ax, fn, 0, 2 * math.pi, X, Yf, role)
    text(ax, 80, mid + 9, lab, role, 'm')
brace(ax, X(0), X(2 * math.pi), 46, 'fixe', r'période $2\pi$')
brace(ax, X(0), X(math.pi), 18, 'sujet', r'période $\pi = 2\pi/2$')
save(fig, '30-115')
