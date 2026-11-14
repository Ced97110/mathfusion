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
fig,ax=canvas(76)
bal(ax,44,58,[(r'$x$','sujet'),('3','fixe')],[('7','fixe')])
text(ax,2,66,'haut','fixe','s',ha='left')
arrow(ax,(44,49),(44,37),'varie'); text(ax,48,43,'− 3 de chaque côté','varie','s',ha='left')
bal(ax,44,20,[(r'$x$','sujet')],[('4','resultat')])
text(ax,2,28,'bas','fixe','s',ha='left')
arrow(ax,(85,60),(85,22),'resultat',lw=1.4)
text(ax,80.5,41,r'haut vrai $\Rightarrow$ bas vrai','resultat','m',rot=90)
save(fig,'16-017')
