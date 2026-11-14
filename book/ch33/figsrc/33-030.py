import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lb(x, y, h=4):  # closing "[" (open side right)
    line(ax, [(x + 2, y + h), (x, y + h), (x, y - h), (x + 2, y - h)], "sujet", lw=1.2)
def rb(x, y, h=4):  # closing "]" (open side left)
    line(ax, [(x - 2, y + h), (x, y + h), (x, y - h), (x - 2, y - h)], "sujet", lw=1.2)
def olb(x, y, h=4):  # outward "]" at a left end
    line(ax, [(x - 2, y + h), (x, y + h), (x, y - h), (x - 2, y - h)], "sujet", lw=1.2)
def orb(x, y, h=4):  # outward "[" at a right end
    line(ax, [(x + 2, y + h), (x, y + h), (x, y - h), (x + 2, y - h)], "sujet", lw=1.2)
def hole(x, y):
    ax.add_patch(Circle((x, y), 1.7, ec=COL["sujet"], fc=FILL["encre"], lw=1.0, zorder=6))
fig, ax = canvas(56)
f = numberline(ax, 8, 74, 24, -120, 120, step=30, labels=False)
line(ax, [(f(-90), 24), (f(90), 24)], 'sujet', lw=3)
olb(f(-90), 24); orb(f(90), 24)
hole(f(-90), 24); hole(f(90), 24)
for v, s in ((-90, '−90°'), (0, '0°'), (90, '90°')):
    text(ax, f(v), 17, s, 'fixe', 's')
text(ax, 44, 48, ']−90°, 90°[', 'sujet', 'xl')
text(ax, f(-90), 34, 'bout exclu', 'sujet', 's')
text(ax, f(90), 34, 'bout exclu', 'sujet', 's')
brace(ax, f(-90), f(90), 11, 'sujet', label='tous les angles entre')
save(fig, '33-030')
