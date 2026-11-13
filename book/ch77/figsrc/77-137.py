import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 22, 60, 'sur ℝ', 'sujet', 'm', weight='bold'); text(ax, 66, 60, 'sur ℂ', 'autre', 'm', weight='bold')
arrow(ax, (3, 24), (41, 24), 'fixe'); 
xs = [i / 10 for i in range(-20, 21)]
line(ax, [(22 + x * 8, 30 + x * x * 3.2) for x in xs], 'sujet', lw=1.2)
text(ax, 22, 52, r'$\lambda^2+1$', 'sujet', 's')
text(ax, 22, 12, 'aucune racine', 'limite', 'm')
arrow(ax, (47, 30), (85, 30), 'fixe'); arrow(ax, (66, 12), (66, 54), 'fixe')
for y, s in ((42, 'i'), (18, '-i')):
    disc(ax, 66, y, 1.6, 'resultat'); text(ax, 73, y, f'${s}$', 'resultat', 'm')
text(ax, 66, 5, 'deux racines', 'resultat', 'm')
save(fig, '77-137')
