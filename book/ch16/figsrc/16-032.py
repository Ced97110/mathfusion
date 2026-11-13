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
fig,ax=canvas(68)
text(ax,44,62,'valeur connue maintenant ?','encre','m')
for y,(l,v,a,r1,r2) in zip((40,24,8),[('a','3','oui','sujet','resultat'),('b','7','oui','sujet','resultat'),('x','?','non','autre','limite')]):
    box(ax,4,y,16,10,r1,label=r'$'+l+'$',size='l'); text(ax,26,y+5,'=','encre','l'); box(ax,32,y,16,10,r1,label=v,size='l')
    arrow(ax,(50,y+5),(54,y+5),'fixe'); box(ax,56,y,24,10,r2,label=a,size='l')
save(fig,'16-032')
