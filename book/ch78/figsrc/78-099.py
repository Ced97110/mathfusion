import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
text(ax, 20, 46, r'$x$', 'sujet', 'l'); text(ax, 52, 46, r'$\bar{x}$', 'sujet', 'l'); text(ax, 80, 46, r'$T(x)\,1$', 'resultat', 'm')
rows = [('ℂ', '(1, 2)', '(1, −2)', 20, 22), ('ℍ', '(1, 2, 3, 4)', '(1, −2, −3, −4)', 24, 29)]
for k, (n, a, b, wa, wb) in enumerate(rows):
    y = 28 - k * 17
    text(ax, 5, y + 4, n, 'sujet', 'l')
    box(ax, 11, y, wa, 8, 'sujet', label=a)
    xp = 11 + wa + 3
    line(ax, [(xp - 1.2, y + 4), (xp + 1.2, y + 4)], 'encre', lw=1.2); line(ax, [(xp, y + 2.8), (xp, y + 5.2)], 'encre', lw=1.2)
    box(ax, xp + 3, y, wb, 8, 'autre', label=b)
    xe = xp + 3 + wb + 3
    line(ax, [(xe - 1.2, y + 3.2), (xe + 1.2, y + 3.2)], 'encre', lw=1.2); line(ax, [(xe - 1.2, y + 4.8), (xe + 1.2, y + 4.8)], 'encre', lw=1.2)
    box(ax, 75, y, 11, 8, 'resultat', label=r'$2\cdot1$')
save(fig, '78-099')
