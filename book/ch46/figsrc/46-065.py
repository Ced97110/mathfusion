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

fig,ax=canvas(72)
cs=chain(fig,ax,60,[(r'$\langle$','varie',16),(r'$X$','sujet',16),(r'$\rangle$','varie',16)],gap=1.5)
text(ax,22,48,'engendré par','varie','m'); arrow(ax,(26,51),(cs[0]-1,56),'varie')
text(ax,66,48,'partie de départ','sujet','m'); arrow(ax,(62,51),(cs[1]+1,56),'sujet')
clockd(ax,44,22,12,{4:'sujet',0:'resultat',8:'resultat'},{0,4,8})
text(ax,12,22,r'$X=\{4\}$','sujet','m')
text(ax,73,22,r'$\langle 4\rangle=\{0,4,8\}$','resultat','m')
save(fig,'46-065')
