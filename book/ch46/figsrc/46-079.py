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

fig,ax=canvas(66)
text(ax,44,60,r'$k\in\mathbb{Z}$, ici $a=5$','sujet','l')
f=numberline(ax,14,70,40,-3,3)
brace(ax,f(-3),f(-0.5),47,'varie',label='négatifs',down=False)
brace(ax,f(0.5),f(3),47,'sujet',label='positifs',down=False)
for k,v in [(-1,'7'),(0,'0'),(1,'5')]:
    arrow(ax,(f(k),34),(f(k),21),'fixe'); box(ax,f(k)-3.2,12,6.4,9,'resultat',label=v)
text(ax,14,16.5,r'$a^k$','fixe','m')
save(fig,'46-079')
