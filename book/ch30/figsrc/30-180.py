import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
f = numberline(ax, 6, 80, 40, -6, 8, step=2, labels=False, arrow_right=False)
a, b, c = f(-5.2832), f(1), f(7.2832)
for x, s in [(a, '−5,2832'), (b, '1'), (c, '7,2832')]:
    disc(ax, x, 40, 1.4, 'sujet'); text(ax, x, 33, s, 'sujet', 's')
for p, q in [(a, b), (b, c)]:
    arrow(ax, (p, 41.5), (q, 41.5), 'varie', curve=-0.4)
    text(ax, (p + q) / 2, 52, r'$+2\pi$ (un tour)', 'varie', 's')
text(ax, 44, 21, r'même classe modulo $2\pi$', 'sujet', 'm')
text(ax, 44, 12, 'sinus ≈ 0,8415 pour les trois', 'resultat', 's')
save(fig, '30-180')
