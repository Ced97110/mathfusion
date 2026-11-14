import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
R = 3.0
y = 32
xl_ = [7, 18, 29, 40]
xr_ = [51, 62, 73, 84]

def edge(p, q, r):
    dx, dy = q[0] - p[0], q[1] - p[1]; d = math.hypot(dx, dy)
    return (p[0] + dx / d * r, p[1] + dy / d * r)

def swap(xs, i, j, role):
    p, q = (xs[i], y), (xs[j], y)
    arrow(ax, edge(p, q, R), edge(q, p, R), role, both=True)

text(ax, 23, 56, r'$(123)(234)=(12)(34)$', 'sujet', 's')
text(ax, 67, 56, r'$(234)(123)=(13)(24)$', 'autre', 's')
for i in range(4):
    disc(ax, xl_[i], y, R, 'sujet', label=str(i + 1))
    disc(ax, xr_[i], y, R, 'autre', label=str(i + 1))
swap(xl_, 0, 1, 'sujet')
swap(xl_, 2, 3, 'sujet')
arrow(ax, (xr_[0], y + R), (xr_[2], y + R), 'autre', curve=-0.45, both=True)
arrow(ax, (xr_[1], y - R), (xr_[3], y - R), 'autre', curve=0.45, both=True)
text(ax, 45.5, y, r'$\neq$', 'encre', 'xl')
text(ax, 23, 17, r"d'abord $(234)$, puis $(123)$", 'sujet', 's')
text(ax, 67, 17, r"d'abord $(123)$, puis $(234)$", 'autre', 's')
text(ax, 44, 5, r"$A_4$ n'est pas abélien", 'encre', 'm')
save(fig, '64-140')
