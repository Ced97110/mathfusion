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
fig,ax=canvas(66)
line(ax,[(14,49),(74,49)],'fixe',lw=1.4); text(ax,82,49,'plateau','fixe','s')
for c,(lab,role) in zip((24,44,64),[(r'$x$','sujet'),('3','fixe'),('2','fixe')]): box(ax,c-6,50,12,9,role,label=lab,size='l')
for c,(lab,role) in zip((24,44,64),[(r'$x$','sujet'),('3','fixe'),('2','fixe')]):
    line(ax,[(c,45),(c,30)],'fixe',dash=True); text(ax,c,25,lab,role,'l')
text(ax,34,25,'+','varie','l'); text(ax,54,25,'+','varie','l')
text(ax,44,10,'+ se lit « ajouté à »','varie','m')
save(fig,'16-024')
