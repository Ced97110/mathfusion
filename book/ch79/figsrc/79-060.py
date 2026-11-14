import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def E(ax, p, q, r=3.4, role='fixe', lw=0.9):
    dx, dy = q[0]-p[0], q[1]-p[1]; d = math.hypot(dx, dy); ux, uy = dx/d, dy/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw)
def N(ax, x, y, s, role='sujet', r=3.4, size='m'):
    disc(ax, x, y, r, role, label=s, size=size)

fig, ax = canvas(88)
Pn = {'e': (44, 14), 'r': (24, 34), 'b': (44, 34), 'v': (64, 34), 'rb': (24, 54), 'rv': (44, 54), 'bv': (64, 54), 'rbv': (44, 74)}
lab = {'e': r'$\emptyset$'}
for a, b in (('e', 'r'), ('e', 'b'), ('e', 'v'), ('r', 'rb'), ('r', 'rv'), ('b', 'rb'), ('b', 'bv'), ('v', 'rv'), ('v', 'bv'), ('rb', 'rbv'), ('rv', 'rbv'), ('bv', 'rbv')):
    E(ax, Pn[a], Pn[b], 4.5)
for k, p in Pn.items(): N(ax, *p, lab.get(k, k), 'sujet', 4.5, 's')
text(ax, 14, 80, r'$\mathcal{P}(S)$', 'sujet', 'l')
text(ax, 18, 70, 'r, b, v : 3 stylos', 'fixe', 's')
text(ax, 70, 14, r'$2\times2\times2=8$ parties', 'resultat', 's')
text(ax, 18, 14, r'$\subseteq$ : on monte', 'varie', 's')
save(fig, '79-060')
