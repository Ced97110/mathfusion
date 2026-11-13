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
text(ax,44,54,r'$s^{-1}\in X$','sujet','l')
box(ax,6,16,26,30,'sujet'); text(ax,19,41,r'$X=\{4\}$','sujet','m')
disc(ax,19,26,4.5,'sujet',label='4')
disc(ax,68,28,4.5,'autre',label='8'); text(ax,68,20,r'$s=8$','autre','m'); text(ax,68,38,r'$8\notin X$','limite','m')
arrow(ax,(63,28),(24.5,28),'varie'); text(ax,45,32,'inverse de 8 : 4','varie','m')
text(ax,44,7,r'$s^{-1}=4\in X$ : 8 permis','resultat','m')
save(fig,'46-070')
