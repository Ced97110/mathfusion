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

fig, ax = canvas(62)
text(ax, 22.5, 56, '× inventée : tout vaut 1', 'autre', 's'); text(ax, 65.5, 56, 'vrai cadran', 'sujet', 's')
box(ax, 2, 38, 41, 9, 'autre', label=r'$3\times(1+2)=3\times3=1$', r=0.5)
box(ax, 2, 25, 41, 9, 'autre', label=r'$3\times1+3\times2=1+1=2$', r=0.5)
box(ax, 45, 38, 41, 9, 'sujet', label=r'$3\times(1+2)=3\times3=1$', r=0.5)
box(ax, 45, 25, 41, 9, 'sujet', label=r'$3\times1+3\times2=3+2=1$', r=0.5)
text(ax, 22.5, 14, r'$1\neq2$', 'limite', 'l'); text(ax, 65.5, 14, r'$1=1$', 'resultat', 'l')
save(fig, '51-023')
