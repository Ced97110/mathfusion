import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def rowd(ax, y, roles, labels, x0=8.0, step=6.4, r=2.6, size='s'):
    for n in range(12):
        disc(ax, x0 + n * step, y, r, roles.get(n, 'fixe'), label=(str(n) if n in labels else None), size=size)
    return lambda n: x0 + n * step

def clockd(ax, cx, cy, R, roles, labels, r=2.8, size='s'):
    for n in range(12):
        a = math.radians(30 * n)
        disc(ax, cx + R * math.sin(a), cy + R * math.cos(a), r, roles.get(n, 'fixe'), label=(str(n) if n in labels else None), size=size)

def chain(fig, ax, y, pieces, cx=44.0, gap=0.8):
    ts = [text(ax, 0, y, s, ro, sz, ha='left') for s, ro, sz in pieces]
    fig.canvas.draw(); rd = fig.canvas.get_renderer()
    ws = [t.get_window_extent(rd).width / fig.dpi * 25.4 for t in ts]
    x = cx - (sum(ws) + gap * (len(ws) - 1)) / 2; cs = []
    for t, w in zip(ts, ws):
        t.set_x(x); cs.append(x + w / 2); x += w + gap
    return cs

fig,ax=canvas(54)
for x,l in [(6,r'$s_1$'),(26,r'$s_2$'),(62,r'$s_r$')]: box(ax,x,40,16,10,'sujet',label=l)
text(ax,52,45,r'$\cdots$','fixe','l')
brace(ax,6,78,40,'sujet',label=r'$r$ facteurs')
text(ax,44,28,'cas : 4 + 4 + 4','fixe','m')
for x in (10,34,58): box(ax,x,12,16,10,'sujet',label='4')
text(ax,30,17,'+','fixe','l'); text(ax,54,17,'+','fixe','l')
brace(ax,10,74,12,'sujet',label=r'$r=3$, tous égaux à 4')
save(fig,'46-068')
