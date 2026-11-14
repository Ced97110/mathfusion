import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
s = 16; h = s / 2
off = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
def r_(L): n = [0] * 4; [n.__setitem__((p + 1) % 4, L[p]) for p in range(4)]; return n
def s_(L): n = [0] * 4; [n.__setitem__(3 - p, L[p]) for p in range(4)]; return n
def sq(cx, cy, L, role):
    poly(ax, [(cx-h, cy-h), (cx+h, cy-h), (cx+h, cy+h), (cx-h, cy+h)], role)
    for p, (dx, dy) in enumerate(off):
        text(ax, cx + dx * (h - 3.3), cy + dy * (h - 3.3), str(L[p]), 'sujet', 's')
L0 = [1, 2, 3, 4]
A = s_(r_(L0)); B = r_(r_(r_(s_(L0))))
assert A == B
sq(16, 38, L0, 'fixe'); sq(70, 60, A, 'resultat'); sq(70, 17, B, 'resultat')
arrow(ax, (25, 42), (61, 57), 'varie'); arrow(ax, (25, 34), (61, 20), 'varie')
text(ax, 36, 56, 'r puis s', 'varie', 's'); text(ax, 36, 21, r'$s$ puis $r^3$', 'varie', 's')
line(ax, [(65, 41), (75, 41)], 'resultat', lw=1.3); line(ax, [(65, 36), (75, 36)], 'resultat', lw=1.3)
save(fig, '44-204')
