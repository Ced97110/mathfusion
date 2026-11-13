import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
cw, ch = 10, 9
gx = [22, 34]            # colonnes communes
rx = [50, 62]            # colonnes du reste
rows = [(35, r'$6x^2$', ['3', 'x'], ['2', 'x']),
        (24, r'$9x$',   ['3', 'x'], ['3'])]
box(ax, 20.5, 22.5, 25, 23.5, 'resultat', fill=False, dash=True)
box(ax, 48.5, 22.5, 25, 23.5, 'sujet', fill=False, dash=True)
for y, lab, com, rest in rows:
    text(ax, 11, y + ch / 2, lab, 'encre', 'l')
    for x, t in zip(gx, com):
        box(ax, x, y, cw, ch, 'resultat', label=t, size='l')
    for x, t in zip(rx, rest):
        box(ax, x, y, cw, ch, 'sujet', label=t, size='l')
text(ax, 33, 49.5, 'dans les deux : 3x', 'resultat', 's', weight='bold')
text(ax, 61, 49.5, 'ce qui reste', 'sujet', 's')
text(ax, 33, 18, r'PGCD de 6 et 9 : 3', 'resultat', 's')
text(ax, 44, 8, r'$6x^2+9x=3x\,(2x+3)$', 'encre', 'l')
save(fig, '05-176')
