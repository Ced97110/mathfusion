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
fig,ax=canvas(80)
rows=[(58,r'$x+3=7$',r'$x=4$','sujet','resultat','départ'),
      (36,r'$y+3=7$',r'$y=4$','sujet','resultat','autre lettre, même solution'),
      (14,r'$x+5=7$',r'$x=2$','varie','varie','autre nombre, autre solution')]
for y,a,b,r1,r2,lab in rows:
    text(ax,4,y+14,lab,'fixe','s',ha='left')
    box(ax,4,y,34,10,r1,label=a,size='l'); arrow(ax,(40,y+5),(50,y+5),'fixe'); box(ax,52,y,28,10,r2,label=b,size='l')
save(fig,'16-025')
