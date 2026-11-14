import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mat(ax, x, y, rows, role="sujet", rh=5.6, hw=8, size="m"):
    n = len(rows); top = y + n * rh / 2 + 0.4; bot = y - n * rh / 2 - 0.4
    for i, r in enumerate(rows):
        text(ax, x, y + n * rh / 2 - rh * (i + 0.5), r, role, size)
    for s in (-1, 1):
        xx = x + s * hw
        line(ax, [(xx - s * 1.6, top), (xx, top), (xx, bot), (xx - s * 1.6, bot)], role, lw=0.9)

fig, ax = canvas(84)
box(ax, 21, 66, 26, 10, 'fixe', label=r'$u_1=1$'); box(ax, 51, 66, 26, 10, 'fixe', label=r'$u_2=i$')
arrow(ax, (34, 66), (34, 54), 'varie'); arrow(ax, (64, 66), (64, 54), 'varie')
text(ax, 36, 60, r'$\times a$', 'varie', 's', ha='left'); text(ax, 66, 60, r'$\times a$', 'varie', 's', ha='left')
box(ax, 21, 42, 26, 12, 'varie', label=r'$au_1=2+i$', size='s'); box(ax, 51, 42, 26, 12, 'varie', label=r'$au_2=-1+2i$', size='s')
arrow(ax, (34, 42), (34, 33), 'sujet'); arrow(ax, (64, 42), (64, 33), 'sujet')
text(ax, 36, 37.5, 'coordonnées', 'sujet', 's', ha='left')
box(ax, 21, 6, 26, 26, 'varie'); box(ax, 51, 6, 26, 26, 'varie')
for xc, (a, b) in ((34, ('$2$', '$1$')), (64, ('$-1$', '$2$'))):
    text(ax, xc, 25, a, 'encre', 'l'); text(ax, xc, 13, b, 'encre', 'l')
for s, xx in ((-1, 18), (1, 80)):
    line(ax, [(xx - s * 1.6, 33.5), (xx, 33.5), (xx, 4.5), (xx - s * 1.6, 4.5)], 'sujet', lw=0.9)
text(ax, 9, 19, r'$\rho(a)=$', 'sujet', 's')
save(fig, '77-024')
