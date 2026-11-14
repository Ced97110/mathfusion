import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
sw, h, y0 = 8, 7, 8
text(ax, 44, 46, r'$x$ : les racines à atteindre', 'encre', 's')
def stairs(x0, radicals, title, broken=False):
    m = len(radicals)
    for k, r in enumerate(radicals):
        box(ax, x0 + k * sw, y0, sw, (k + 1) * h, 'sujet', label=r, size='s')
    if not broken:
        box(ax, x0 + m * sw, y0, sw, (m + 1) * h, 'resultat', label=r'$x$', size='s')
    else:
        k = m
        box(ax, x0 + k * sw, y0, sw, (k + 1) * h, 'limite', fill=False, dash=True)
        text(ax, x0 + k * sw + sw / 2, y0 + (k + 1) * h / 2, 'coupé', 'limite', 's', rot=90)
        box(ax, x0 + (k + 1) * sw, y0, sw, (k + 2) * h, 'resultat', fill=False, dash=True, label=r'$x$', size='s')
        m += 1
    text(ax, x0 + (m + 1) * sw / 2, 3.5, title, 'encre', 's')
stairs(3, ['√'], 'degré 2')
stairs(23, ['√', r'$\sqrt[3]{\ \ }$'], 'degré 3')
stairs(51, ['√', r'$\sqrt[3]{\ \ }$'], 'degré 5', broken=True)
save(fig, '65-108')
