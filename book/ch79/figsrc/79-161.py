import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def redge(ax, c1, s1, c2, s2, role="fixe", lw=1.0, dash=False):
    dx, dy = c2[0]-c1[0], c2[1]-c1[1]
    def t(s):
        return min(s[0]/abs(dx) if dx else 1e9, s[1]/abs(dy) if dy else 1e9)
    t1, t2 = t(s1), t(s2)
    line(ax, [(c1[0]+dx*t1, c1[1]+dy*t1), (c2[0]-dx*t2, c2[1]-dy*t2)], role, lw, dash)

def nbox(ax, c, hw, hh, role, label, size="m"):
    box(ax, c[0]-hw, c[1]-hh, 2*hw, 2*hh, role, label=label, size=size)

def cedge(ax, p, q, r, role="fixe", lw=1.0, dash=False):
    d = math.hypot(q[0]-p[0], q[1]-p[1]); ux, uy = (q[0]-p[0])/d, (q[1]-p[1])/d
    line(ax, [(p[0]+ux*r, p[1]+uy*r), (q[0]-ux*r, q[1]-uy*r)], role, lw, dash)

fig, ax = canvas(66)
hw, hh = 7, 4
C = {'e': (26, 8), 'B': (14, 24), 'K': (14, 40), 'C': (40, 26), 'D': (26, 56)}
roles = {'e': 'fixe', 'B': 'sujet', 'K': 'sujet', 'C': 'autre', 'D': 'fixe'}
labs = {'e': r'$\{e\}$', 'B': r'$B$', 'K': r'$K$', 'C': r'$C$', 'D': r'$D_4$'}
for a, b in [('e', 'B'), ('B', 'K'), ('K', 'D'), ('e', 'C'), ('C', 'D')]:
    redge(ax, C[a], (hw, hh), C[b], (hw, hh), 'fixe', 1.0)
for k, c in C.items():
    nbox(ax, c, hw, hh, roles[k], labs[k])
text(ax, 67, 54, r'$K\cap(B\vee C)=K$', 'encre', 's')
text(ax, 67, 43, r'$K\cap C=\{e\}$', 'encre', 's')
text(ax, 67, 33, r'$B\vee(K\cap C)=B$', 'encre', 's')
text(ax, 67, 21, r'$K\neq B$', 'limite', 'l')
text(ax, 67, 10, 'la loi $M$ échoue', 'limite', 's')
save(fig, '79-161')
