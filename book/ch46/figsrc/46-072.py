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

fig,ax=canvas(58)
text(ax,20,52,r'$\langle\{a,b\}\rangle$','autre','l')
arrow(ax,(34,52),(52,52),'varie'); text(ax,43,56,'on enlève { }','varie','s')
text(ax,68,52,r'$\langle a,b\rangle$','sujet','l')
text(ax,44,36,r'$\langle 4,6\rangle$ : les nombres pairs','resultat','m')
roles={n:('resultat' if n%2==0 else 'fixe') for n in range(12)}; roles[4]='sujet'; roles[6]='sujet'
rowd(ax,20,roles,{0,2,4,6,8,10})
text(ax,44,8,r'$X=\{4,6\}$','sujet','m')
save(fig,'46-072')
