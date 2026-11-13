import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def fano(ax, cx, cy, s, pts=None, hl=None):
    pts = pts or {}
    h = s * math.sqrt(3) / 2
    P = {'001': (cx, cy + 2 * h / 3), '100': (cx - s / 2, cy - h / 3), '010': (cx + s / 2, cy - h / 3)}
    mid = lambda a, b: ((P[a][0] + P[b][0]) / 2, (P[a][1] + P[b][1]) / 2)
    P['101'] = mid('100', '001'); P['011'] = mid('010', '001'); P['110'] = mid('100', '010'); P['111'] = (cx, cy)
    for a, b in [('100', '001'), ('001', '010'), ('100', '010'), ('001', '110'), ('100', '011'), ('010', '101')]:
        line(ax, [P[a], P[b]], 'fixe', lw=0.8)
    rc = s * math.sqrt(3) / 6
    th = [i * math.pi / 90 for i in range(181)]
    circ = [(cx + rc * math.cos(t), cy + rc * math.sin(t)) for t in th]
    hl = hl or {}
    if 'circle' in hl: line(ax, circ, hl['circle'], lw=1.8)
    else: line(ax, circ, 'fixe', lw=0.8)
    if 'm001' in hl: line(ax, [P['001'], P['110']], hl['m001'], lw=1.8)
    off = {'001': (0, 3.4, 'center'), '100': (-1.0, -3.4, 'center'), '010': (1.0, -3.4, 'center'),
           '101': (-2.8, 0.6, 'right'), '011': (2.8, 0.6, 'left'), '110': (0, -3.6, 'center'), '111': (2.6, 2.0, 'left')}
    for k, (x, y) in P.items():
        role = pts.get(k, 'fixe')
        disc(ax, x, y, 1.9, role)
        text(ax, x + off[k][0], y + off[k][1], k, role, 's', ha=off[k][2])
    return P

fig,ax=canvas(66)
fano(ax,26,30,40,pts={'110':'sujet','001':'autre','111':'resultat'},hl={'m001':'resultat'})
text(ax,68,58,'110 + 001 = 111','resultat','m')
box(ax,52,38,34,9,'resultat',label='{000, 110, 001, 111}',size='s')
text(ax,69,30,'médiane qui part de 001','resultat','s')
text(ax,69,23,'une seule droite','resultat','s')
save(fig,'80-096')
