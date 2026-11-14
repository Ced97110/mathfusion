import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def ring(ax, x, y, r, role, lw=2.2):
    th = [i * math.pi / 90 for i in range(181)]
    line(ax, [(x + r * math.cos(t), y + r * math.sin(t)) for t in th], role, lw=lw)
fig, ax = canvas(62)
cx, cy, r = 22, 31, 17
disc(ax, cx, cy, r, 'fixe'); ring(ax, cx, cy, r, 'fixe', 1.0)
arrow(ax, (cx - r, cy), (cx + r, cy), 'sujet', lw=1.8, both=True)
text(ax, cx, cy + 3.5, r'$d$', 'sujet', 'l', weight='bold')
text(ax, cx, cy - 4, 'le diamètre', 'sujet', 's')
box(ax, 50, 40, 8, 9, 'sujet', label=r'$d$', size='l')
text(ax, 60, 44.5, r'= 2 $\times$ $r$', 'encre', 'l', ha='left')
text(ax, 50, 18.5, r'$C$ = $\pi$ $\times$', 'encre', 'l', ha='left')
box(ax, 73, 14, 8, 9, 'sujet', label=r'$d$', size='l')
arrow(ax, (cx + r, cy + 3), (49.5, 44.5), 'sujet', lw=0.8, curve=0.2)
arrow(ax, (cx + r - 3, cy - 12), (72.5, 18.5), 'sujet', lw=0.8, curve=-0.25)
save(fig, '11-092')
