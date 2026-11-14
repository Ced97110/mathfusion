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
fig, ax = canvas(58)
for y, closed in ((40, True), (12, False)):
    line(ax, [(6, y), (80, y)], 'fixe', lw=0.9)
    line(ax, [(8, y), (56, y)], 'sujet', lw=3)
    if closed:
        rb(56, y); disc(ax, 56, y, 1.7, 'sujet')
    else:
        orb(56, y); hole(56, y)
    text(ax, 56, y - 7, r'$\pi/2$', 'fixe', 's')
    text(ax, 40, y + 9, r'$[-\pi/2,\ \pi/2]$' if closed else r'$]-\pi/2,\ \pi/2[$', 'sujet', 'l')
    text(ax, 70, y + 5, 'contient π/2' if closed else 'sans π/2', 'resultat' if closed else 'fixe', 's')
save(fig, '33-032')
