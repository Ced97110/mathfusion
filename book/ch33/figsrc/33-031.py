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
fig, ax = canvas(54)
for y, closed in ((38, True), (12, False)):
    f = numberline(ax, 10, 74, y, -0.5, 1.5, labels=False, arrow_right=False)
    line(ax, [(f(0), y), (f(1), y)], 'sujet', lw=3)
    if closed:
        lb(f(0), y); rb(f(1), y); disc(ax, f(0), y, 1.7, 'sujet'); disc(ax, f(1), y, 1.7, 'sujet')
    else:
        olb(f(0), y); orb(f(1), y); hole(f(0), y); hole(f(1), y)
    text(ax, f(0), y - 7, '0', 'fixe', 's'); text(ax, f(1), y - 7, '1', 'fixe', 's')
    text(ax, 4, y + 9, '[0, 1]' if closed else ']0, 1[', 'sujet', 'l', ha='left')
    text(ax, 84, y + 9, '1 est dedans' if closed else '1 est dehors', 'resultat' if closed else 'fixe', 's', ha='right')
save(fig, '33-031')
