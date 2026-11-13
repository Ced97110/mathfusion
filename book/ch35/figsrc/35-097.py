import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def wv(ax, fn, xa, xb, yc, amp, role, t0, t1, n=240, lw=1.2, dash=False):
    pts = [(xa + (xb - xa) * i / n, yc + amp * fn(t0 + (t1 - t0) * i / n)) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
pi = math.pi

fig, ax = canvas(62)
xa, xb, yc, amp = 8, 80, 34, 12
xm = (xa + xb) / 2
line(ax, [(xa, yc), (xb, yc)], 'fixe', lw=0.6)
wv(ax, lambda t: -math.cos(t), xa, xb, yc, amp, 'sujet', 0, 2 * pi)
wv(ax, lambda t: math.cos(t), xa, xb, yc, amp, 'autre', 0, 2 * pi)
line(ax, [(xm, yc - amp - 3), (xm, yc + amp + 3)], 'fixe', dash=True)
disc(ax, xm, yc + amp, 1.3, 'sujet'); disc(ax, xm, yc - amp, 1.3, 'autre'); disc(ax, xm, yc, 1.3, 'resultat')
text(ax, xm, yc + amp + 5, '+1', 'sujet', 's'); text(ax, xm, yc - amp - 5, '−1', 'autre', 's')
text(ax, xm + 4, yc + 3, '0', 'resultat', 's')
line(ax, [(10, 57), (16, 57)], 'sujet'); text(ax, 18, 57, 'onde A', 'sujet', 's', ha='left')
line(ax, [(52, 57), (58, 57)], 'autre'); text(ax, 60, 57, 'onde B', 'autre', 's', ha='left')
text(ax, xm, 12.5, r'$x=\pi$', 'fixe', 's')
text(ax, xm, 5.5, r'$+1+(-1)=0$', 'resultat', 'm')
save(fig, '35-097')
