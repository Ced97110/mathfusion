import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
cw, gap = 4.4, 3
def row(yb, size, n, title, ql, pl):
    wtot = n * size * cw + (n - 1) * gap
    x0 = (88 - wtot) / 2
    for g in range(n):
        gx = x0 + g * (size * cw + gap)
        for c in range(size):
            box(ax, gx + c * cw, yb, cw, 6, 'sujet', r=0.4, lw=0.6)
    brace(ax, x0, x0 + wtot, yb + 6, 'resultat', ql, down=False)
    brace(ax, x0, x0 + size * cw, yb, 'sujet', pl)
    text(ax, 44, yb + 16, title, 'encre', 'm')
row(50, 4, 3, r'$p=2$ : $12=2^2\times3$', r'$q=3$', r'$2^2=4$')
row(18, 3, 4, r'$p=3$ : $12=3^1\times4$', r'$q=4$', r'$3^1=3$')
save(fig, '50-035')
