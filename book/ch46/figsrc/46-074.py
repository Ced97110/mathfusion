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

fig,ax=canvas(64)
text(ax,22,56,r'$\{5\}$ engendre $\mathbb{Z}/12\mathbb{Z}$','sujet','l')
text(ax,66,56,r'$\{4\}$ non','limite','l')
r1={n:'resultat' for n in range(12)}; r1[5]='sujet'
clockd(ax,22,32,12,r1,{5})
clockd(ax,66,32,12,{4:'sujet',0:'resultat',8:'resultat'},{0,4,8})
text(ax,22,12,'12 heures : tout le groupe','resultat','m')
text(ax,66,12,'3 heures seulement','limite','m')
save(fig,'46-074')
