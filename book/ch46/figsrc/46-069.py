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

fig,ax=canvas(60)
box(ax,6,28,76,26,'sujet')
text(ax,44,50,r'partie $X=\{0,4,8\}$','sujet','m')
for x,l in [(26,'0'),(44,'4'),(62,'8')]: disc(ax,x,37,4.5,'sujet',label=l)
text(ax,44,21,r'$\in$ se lit « appartient à »','encre','m')
disc(ax,14,8,4,'resultat',label='4'); text(ax,31,8,r'$4\in X$','resultat','m')
disc(ax,52,8,4,'limite',label='5'); text(ax,69,8,r'$5\notin X$','limite','m')
save(fig,'46-069')
