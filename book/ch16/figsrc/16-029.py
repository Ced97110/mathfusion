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
fig,ax=canvas(74)
e=eq(ax,52,[(r'$x$','fixe',11),('+','~fixe',5),('3','fixe',11),('=','~encre',5),('7','autre',11)],x0=16)
brace(ax,e[0][0],e[2][1],63,'fixe','membre de gauche',down=False)
brace(ax,e[4][0],e[4][1],63,'autre','membre de droite',down=False)
arrow(ax,(44,50),(44,36),'varie'); text(ax,48,43,'− 3 aux deux membres','varie','s',ha='left')
eq(ax,18,[(r'$x$','sujet',11),('=','~encre',5),('4','resultat',11)],anchor=(1,44))
save(fig,'16-029')
