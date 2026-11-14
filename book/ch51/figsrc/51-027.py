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

fig, ax = canvas(66)
text(ax, 4, 59, 'avec le point', 'sujet', 's', ha='left')
text(ax, 44, 52, r'$a\cdot(b+c)=a\cdot b+a\cdot c$', 'sujet', 'm')
arrow(ax, (44, 46), (44, 35), 'varie')
text(ax, 48, 40.5, 'on enlève le point', 'varie', 's', ha='left')
text(ax, 4, 31, 'sans signe', 'resultat', 's', ha='left')
text(ax, 44, 24, r'$a(b+c)=ab+ac$', 'resultat', 'l')
box(ax, 4, 3, 80, 11, 'limite', label='3 et 4 côte à côte : 34', size='s', r=0.5)
save(fig, '51-027')
