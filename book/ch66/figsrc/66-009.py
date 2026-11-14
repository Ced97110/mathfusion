import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
y = 62
f = numberline(ax, 4, 78, y, 0, 21, step=1, every=5)
E = math.e
for v, lab in [(E, r'$e\approx2{,}718$'), (E ** 2, r'$e^2\approx7{,}389$'), (E ** 3, r'$e^3\approx20{,}09$')]:
    disc(ax, f(v), y, 1.4, 'sujet')
    text(ax, f(v), y + 6, lab, 'sujet', 's')
text(ax, 44, y - 10, 'les puissances de $e$ ne sont pas entières', 'fixe', 's')
box(ax, 6, 26, 32, 10, 'sujet', label=r'$e$ : Hermite 1873', size='s')
box(ax, 50, 26, 32, 10, 'autre', label=r'$\pi$ : Lindemann 1882', size='s')
brace(ax, 6, 82, 38, 'varie', label=r'même argument, plus simple pour $e$', down=False)
box(ax, 8, 3, 72, 12, 'resultat', label="$e$ et $\\pi$ : racines d'aucun\npolynôme à coefficients entiers", size='s')
arrow(ax, (22, 26), (34, 15.5), 'resultat'); arrow(ax, (66, 26), (54, 15.5), 'resultat')
save(fig, '66-009')
