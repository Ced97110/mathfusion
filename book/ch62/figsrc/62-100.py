import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)

def panel(x0, role, title, f, fp, vmin, vmax, roots, pg, prole, note):
    text(ax, x0 + 20, 62, title, role, 'm', weight='bold')
    text(ax, x0 + 20, 54, f, role, 'm')
    text(ax, x0 + 20, 47, fp, role, 'm')
    y = 32
    g = numberline(ax, x0 + 3, x0 + 37, y, vmin, vmax, 1, labels=False, arrow_right=False)
    for v, lab, dbl in roots:
        if dbl:
            disc(ax, g(v) - 0.8, y, 1.8, role); disc(ax, g(v) + 0.8, y, 1.8, role)
            text(ax, g(v), y + 5, '×2', role, 's')
        else:
            disc(ax, g(v), y, 1.8, role)
        text(ax, g(v), y - 5.5, lab, role, 's')
    text(ax, x0 + 20, 21, note, role, 's')
    box(ax, x0 + 2, 4, 36, 10, prole, label=pg)

panel(2, 'sujet', 'facteur commun', r'$f=(x-1)^2(x+2)$', r'$f^{\prime}=3(x-1)(x+1)$', -3, 2,
      [(-2, r'$-2$', False), (1, r'$1$', True)], r'PGCD $=x-1$', 'sujet', 'une racine double')
panel(46, 'autre', 'aucun facteur commun', r'$f=x^2-2$', r'$f^{\prime}=2x$', -2, 2,
      [(-1.414, r'$-\sqrt{2}$', False), (1.414, r'$\sqrt{2}$', False)], r'PGCD $=1$', 'resultat', 'deux racines simples')
save(fig, '62-100')
