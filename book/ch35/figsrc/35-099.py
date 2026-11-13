import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi

fig, ax = canvas(64)
xa, xb, yc, amp = 8, 80, 34, 14
xm = (xa + xb) / 2
line(ax, [(xa, yc), (xb, yc)], 'fixe', lw=0.6)
wv(ax, lambda t: math.cos(t / 2), xa, xb, yc, amp, 'fixe', 0, 4 * pi, dash=True)
wv(ax, lambda t: abs(math.cos(t / 2)), xa, xb, yc, amp, 'sujet', 0, 4 * pi, lw=1.4)
for x in (xa, xm, xb):
    disc(ax, x, yc + amp, 1.3, 'resultat'); text(ax, x, yc + amp + 4, 'max', 'resultat', 's')
line(ax, [(8, 62), (14, 62)], 'fixe', dash=True); text(ax, 16, 62, r'$\cos(x/2)$', 'fixe', 's', ha='left')
line(ax, [(48, 62), (54, 62)], 'sujet'); text(ax, 56, 62, r'$|\cos(x/2)|$', 'sujet', 's', ha='left')
brace(ax, xa, xm, 17, 'resultat', r'$2\pi$'); brace(ax, xm, xb, 17, 'resultat', r'$2\pi$')
brace(ax, xa, xb, 9, 'fixe', r'$4\pi$ : un tour de $\cos(x/2)$')
save(fig, '35-099')
