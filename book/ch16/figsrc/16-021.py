import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def eq(ax, y, toks, x0=4, gap=3, h=9, anchor=None):
    """toks: (label, role, width); role '~role' = plain sign. Returns (left, right) edges."""
    cs = []; x = x0
    for lab, role, w in toks:
        cs.append(x + w / 2); x += w + gap
    sh = 0 if anchor is None else anchor[1] - cs[anchor[0]]
    out = []
    for (lab, role, w), c in zip(toks, cs):
        c += sh
        if role.startswith('~'): text(ax, c, y + h / 2, lab, role[1:], 'l')
        else: box(ax, c - w / 2, y, w, h, role, label=lab, size='l')
        out.append((c - w / 2, c + w / 2))
    return out

def bal(ax, cx, y, left, right, w=9):
    line(ax, [(cx - 32, y), (cx + 32, y)], 'fixe', lw=1.4)
    poly(ax, [(cx - 4, y - 6), (cx + 4, y - 6), (cx, y)], 'fixe')
    for i, (lab, role) in enumerate(left): box(ax, cx - 31 + i * (w + 1), y + 0.8, w, 8, role, label=lab)
    for i, (lab, role) in enumerate(right): box(ax, cx + 31 - w - i * (w + 1), y + 0.8, w, 8, role, label=lab)
fig,ax=canvas(56)
text(ax,19,48,'expression','sujet','m'); text(ax,69,48,'équation','autre','m')
box(ax,4,28,30,12,'sujet',label=r'$x+3$',size='l'); box(ax,54,28,30,12,'autre',label=r'$x+3=7$',size='l')
arrow(ax,(35,34),(53,34),'varie'); text(ax,44,38.5,'on écrit = 7','varie','s')
text(ax,19,20,'désigne un nombre','sujet','s'); text(ax,69,20,'affirme : vrai ou faux','autre','s')
text(ax,19,13,'n’affirme rien','fixe','s')
save(fig,'16-021')
