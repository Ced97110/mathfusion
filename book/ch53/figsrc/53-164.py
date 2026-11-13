import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
f = lambda v: 6 + (v - 2) / 13 * 74     # essais 2 à 15
def rangee(y, n, racine, stop, p, q):
    text(ax, 6, y + 12, rf'$n = {n}$', 'sujet', 'm', ha='left', weight='bold')
    line(ax, [(f(2), y), (f(15), y)], 'fixe', lw=0.8)
    for v in range(2, 15):
        if v < stop:
            disc(ax, f(v), y, 1.2, 'fixe')
        elif v == stop:
            disc(ax, f(v), y, 1.5, 'resultat')
        else:
            disc(ax, f(v), y, 1.2, 'fixe', fill=False)
    text(ax, f(stop), y - 5, str(stop), 'resultat', 's', weight='bold')
    line(ax, [(f(racine), y - 3), (f(racine), y + 5)], 'varie', lw=0.9, dash=True)
    text(ax, f(racine) + 1.5, y + 7.5, r'$\sqrt{n}$', 'varie', 's', ha='left')
    text(ax, 80, y + 12, rf'${n} = {p} \times {q}$', 'resultat', 's', ha='right')
rangee(48, 221, 221 ** 0.5, 13, 13, 17)
rangee(18, 55, 55 ** 0.5, 5, 5, 11)
text(ax, 44, 5, 'plein : essayé   vide : jamais essayé', 'fixe', 's')
save(fig, '53-164')
