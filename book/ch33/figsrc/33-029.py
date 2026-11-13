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
f = numberline(ax, 10, 74, 24, -0.5, 1.5, step=0.5, labels=False)
for v in (-0.5, 0, 0.5, 1, 1.5):
    text(ax, f(v), 16.5, f'{v:g}'.replace('-', '−').replace('.', ','), 'fixe', 's')
line(ax, [(f(0), 24), (f(1), 24)], 'sujet', lw=3)
lb(f(0), 24); rb(f(1), 24)
disc(ax, f(0), 24, 1.7, 'sujet'); disc(ax, f(1), 24, 1.7, 'sujet'); disc(ax, f(0.5), 24, 1.4, 'sujet')
text(ax, 44, 48, '[0, 1]', 'sujet', 'xl')
text(ax, f(0), 34, 'bout compris', 'sujet', 's')
text(ax, f(1), 34, 'bout compris', 'sujet', 's')
brace(ax, f(0), f(1), 12, 'sujet', label='tous les nombres entre')
save(fig, '33-029')
