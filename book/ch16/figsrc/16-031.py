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
fig,ax=canvas(58)
text(ax,4,52,'sans condition : variable','varie','s',ha='left')
box(ax,4,38,28,10,'varie',label=r'$x+3$',size='l'); arrow(ax,(33,43),(41,43),'varie')
for i,v in enumerate(('1','2','10')): box(ax,42+i*14,39,11,8,'varie',label=v)
text(ax,4,26,'avec = 7 : inconnue','sujet','s',ha='left')
box(ax,4,12,28,10,'sujet',label=r'$x+3=7$',size='l'); arrow(ax,(33,17),(41,17),'sujet')
for i,(v,r) in enumerate((('4','resultat'),('1','limite'),('10','limite'))): box(ax,42+i*14,13,11,8,r,label=v)
text(ax,44,4,'une seule valeur convient','encre','s')
save(fig,'16-031')
