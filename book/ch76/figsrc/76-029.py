import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 64, r'$(2+3s)(1+4s)$', 'sujet', 'l', weight='bold')
cw, ch, gx, gy = 18, 11, 18, 28
for c, h in enumerate(['1', r'$4s$']): text(ax, gx + c * cw + cw / 2, gy + 2 * ch + 4, h, 'sujet', 'm')
for r, h in enumerate(['2', r'$3s$']): text(ax, gx - 4, gy + (1 - r) * ch + ch / 2, h, 'sujet', 'm')
cells = [[('2', 'resultat'), (r'$8s$', 'autre')], [(r'$3s$', 'autre'), (r'$12 s^2 = 12$', 'resultat')]]
for r in range(2):
    for c in range(2):
        l, ro = cells[r][c]
        box(ax, gx + c * cw, gy + (1 - r) * ch, cw, ch, ro, label=l, size='s')
text(ax, 44, 20, r'$s^2 = 1$', 'varie', 'm')
box(ax, 14, 4, 24, 10, 'resultat', label=r'$2+12=14$', size='s')
box(ax, 50, 4, 24, 10, 'autre', label=r'$8s+3s=11s$', size='s')
save(fig, '76-029')
