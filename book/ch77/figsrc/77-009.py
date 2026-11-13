import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
EM = ' '
def brk(cx, cy, hw, hh, role):
    for s in (-1, 1):
        x = cx + s * hw
        line(ax, [(x - s * 1.4, cy + hh), (x, cy + hh), (x, cy - hh), (x - s * 1.4, cy - hh)], role, lw=0.9)
box(ax, 14, 71, 60, 10, 'fixe', label=r'$u=1+\sqrt{2}+\sqrt{3}$')
arrow(ax, (34, 70), (22, 64), 'fixe'); arrow(ax, (54, 70), (66, 64), 'fixe')
text(ax, 22, 60, r'$\mathbb{Q}$ : $4\times4$', 'sujet', 's')
text(ax, 66, 60, r'$\mathbb{Q}(\sqrt{2})$ : $2\times2$', 'autre', 's')
rows = [['1','2','3','0'], ['1','1','0','3'], ['1','0','1','2'], ['0','1','1','1']]
for i, r in enumerate(rows):
    text(ax, 22, 51 - i * 6.5, (EM + EM).join(r), 'sujet', 'm')
brk(22, 41.5, 17, 12, 'sujet')
text(ax, 57, 47, r'$1+\sqrt{2}$', 'autre', 's'); text(ax, 75, 47, '3', 'autre', 'm')
text(ax, 57, 38, '1', 'autre', 'm'); text(ax, 75, 38, r'$1+\sqrt{2}$', 'autre', 's')
brk(66, 42.5, 17, 9, 'autre')
box(ax, 4, 6, 36, 14, 'sujet', label=r'$N=\det=-8$', size='m')
box(ax, 48, 6, 36, 14, 'autre', label=r'$N=\det=2\sqrt{2}$', size='m')
arrow(ax, (22, 28), (22, 21), 'sujet'); arrow(ax, (66, 31), (66, 21), 'autre')
save(fig, '77-009')
