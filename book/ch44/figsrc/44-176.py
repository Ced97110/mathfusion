import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes2(ax, cx, cy, s, xl, xr, yd, yu):
    arrow(ax, (cx - xl * s, cy), (cx + xr * s, cy), 'fixe', lw=0.7)
    arrow(ax, (cx, cy - yd * s), (cx, cy + yu * s), 'fixe', lw=0.7)
    return lambda x, y: (cx + x * s, cy + y * s)
def arc(ax, P, a0, a1, role='varie'):
    d = math.radians(a1 - a0)
    p = (math.cos(math.radians(a0)), math.sin(math.radians(a0))); q = (math.cos(math.radians(a1)), math.sin(math.radians(a1)))
    arrow(ax, P(*p), P(*q), role, curve=math.tan(d / 4))
def mat(ax, x, y, cs, vals, roles, size='m'):
    for i in range(2):
        for j in range(2):
            box(ax, x + j * cs, y + (1 - i) * cs, cs, cs, roles[i][j], label=vals[i][j], size=size)

fig, ax = canvas(50)
cw = 8; x0 = 24
for k in range(7): text(ax, x0 + cw * k + cw / 2, 45, str(k), 'fixe', 's')
for k in range(7): box(ax, x0 + cw * k, 31, cw, 9, 'fixe' if k == 0 else 'sujet', dash=(k == 0))
text(ax, 2, 35.5, r'$n = 7$', 'encre', 'm', ha='left')
text(ax, x0 + 28, 27, r'$U(7)$ : tous sauf 0', 'sujet', 'm')
for k in range(6): box(ax, x0 + cw * k, 14, cw, 9, 'sujet' if k in (1, 5) else ('fixe' if k == 0 else 'limite'), dash=(k == 0))
text(ax, 2, 18.5, r'$n = 6$', 'encre', 'm', ha='left')
text(ax, x0 + cw * 3, 10.5, r'2, 3, 4 : PGCD $\neq$ 1', 'limite', 's')
text(ax, x0 + 24, 5.5, r'$U(6)$ : seulement 1 et 5', 'sujet', 'm')
save(fig, '44-176')
