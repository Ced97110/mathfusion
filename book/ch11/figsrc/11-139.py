import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
xs = [17, 26, 35, 44, 53, 62, 71]
def formula(y, n):
    toks = [(r'$\frac{1}{3}\pi$', 'fixe'), ('×', 'fixe'), (r'$r$', 'sujet'), ('×', 'fixe'), (r'$r$', 'sujet'), ('×', 'fixe'), (r'$h$', 'sujet')]
    for x, (t, role) in list(zip(xs, toks))[:n]:
        text(ax, x, y, t, role, 'l')
        if role == 'sujet': line(ax, [(x - 3, y - 6), (x + 3, y - 6)], 'sujet', lw=1.6)
formula(54, 7)
brace(ax, 31, 74, 44, 'resultat', 'trois longueurs : un volume')
formula(26, 5)
brace(ax, 31, 56, 16, 'limite', 'deux longueurs : une aire')
save(fig, '11-139')
