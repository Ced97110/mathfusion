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
cs=chain(fig,ax,50,[('{','encre','l'),(r'$2k$','sujet','l'),(r'$\mid$','varie','l'),(r'$k\in\mathbb{Z}$','fixe','l'),('}','encre','l')])
text(ax,cs[1],42,'forme','sujet','m'); text(ax,cs[3],35,'condition','fixe','m')
text(ax,cs[2],61,'tel que','varie','m'); arrow(ax,(cs[2],58),(cs[2],54),'varie')
f=numberline(ax,14,70,22,-4,4,step=2,arrow_right=False)
for v in (-4,-2,0,2,4): disc(ax,f(v),22,1.8,'resultat')
text(ax,44,9,'les nombres pairs','resultat','m')
save(fig,'46-078')
