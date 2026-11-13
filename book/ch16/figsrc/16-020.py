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
fig,ax=canvas(62)
box(ax,24,46,40,9,'fixe',label=r'$x+3=44$',size='l')
arrow(ax,(44,45),(44,34),'varie'); text(ax,48,39.5,'− 3 de chaque côté','varie','s',ha='left')
box(ax,22,16,16,10,'sujet',label=r'$x$',size='l'); text(ax,44,21,'=','encre','l'); box(ax,50,16,16,10,'resultat',label='41',size='l')
text(ax,30,10,'l’inconnue seule','sujet','s'); text(ax,58,10,'un nombre','resultat','s')
text(ax,44,3.5,'rien à calculer : la réponse','resultat','s')
save(fig,'16-020')
