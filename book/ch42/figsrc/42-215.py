import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
R=2.6
def els(ax, x, ys, labels, role, dashed=False):
    for y, l in zip(ys, labels):
        disc(ax, x, y, R, role, label=l)
def setbox(ax, x, ys, role, name=None, w=14, pad=5):
    box(ax, x - w/2, min(ys) - pad, w, max(ys) - min(ys) + 2*pad, role, fill=False)
    if name: text(ax, x, max(ys) + pad + 2.6, name, role, 'l')
def link(ax, xa, ya, xb, yb, role='varie', curve=0.0):
    arrow(ax, (xa + R + 0.4, ya), (xb - R - 0.4, yb), role, curve=curve)
fig, ax = canvas(66)
xl, xr = 20, 64
y = [48, 37, 26]
els(ax, xl, y, ['', '', ''], 'sujet')
els(ax, xr, y, [r'$1$', r'$2$', r'$3$'], 'resultat')
setbox(ax, xl, y, 'sujet', 'élèves', w=16); setbox(ax, xr, y, 'resultat', r'$\{1,\ldots,n\}$', w=16)
for v in y: link(ax, xl, v, xr, v)
text(ax, 42, 14, 'un nombre par élève', 'varie', 's')
text(ax, 42, 8, 'un élève par nombre', 'varie', 's')
text(ax, 42, 2.6, r'$n = 3$ : bijection', 'resultat', 's')
save(fig, '42-215')
