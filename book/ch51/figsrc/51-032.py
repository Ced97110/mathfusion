import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def plus(ax, x, y, r="fixe", s=1.3):
    line(ax, [(x - s, y), (x + s, y)], r, 1.0); line(ax, [(x, y - s), (x, y + s)], r, 1.0)

def equals(ax, x, y, r="fixe", s=1.3):
    line(ax, [(x - s, y + .6), (x + s, y + .6)], r, 1.0); line(ax, [(x - s, y - .6), (x + s, y - .6)], r, 1.0)

def cross(ax, x, y, r="fixe", s=1.0):
    line(ax, [(x - s, y - s), (x + s, y + s)], r, 1.0); line(ax, [(x - s, y + s), (x + s, y - s)], r, 1.0)

def grid(ax, x0, y0, cs, n, role="fixe"):
    for r in range(n):
        for c in range(n):
            box(ax, x0 + c * cs, y0 + (n - 1 - r) * cs, cs, cs, role, r=0.4, lw=0.6)

fig, ax = canvas(70)
text(ax, 4, 62, 'à gauche', 'varie', 's', ha='left'); text(ax, 4, 38, 'à droite', 'varie', 's', ha='left')
def res(y, l, r_):
    equals(ax, 38, y + 5)
    box(ax, 43, y, 12, 10, 'resultat', label=l, r=0.5); plus(ax, 58.5, y + 5, 'resultat')
    box(ax, 62, y, 12, 10, 'resultat', label=r_, r=0.5)
box(ax, 4, 46, 8, 10, 'sujet', label=r'$a$', r=0.5); box(ax, 13, 46, 20, 10, 'autre', label=r'$b+c$', r=0.5)
res(46, r'$ab$', r'$ac$')
box(ax, 4, 22, 20, 10, 'autre', label=r'$b+c$', r=0.5); box(ax, 25, 22, 8, 10, 'sujet', label=r'$a$', r=0.5)
res(22, r'$ba$', r'$ca$')
text(ax, 44, 8, r'$3(4+5)=3\cdot4+3\cdot5=27$', 'encre', 'm')
save(fig, '51-032')
