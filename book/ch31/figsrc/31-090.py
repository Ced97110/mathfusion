import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
L = 54; x0 = 30
text(ax, 44, 69, 'à 45°', 'encre', 'l', weight='bold')
def row(y, role, lab, v, val):
    text(ax, x0 - 2, y + 4, lab, role, 's', ha='right')
    box(ax, x0, y, L * v, 8, role)
    text(ax, x0 + L * v + 2, y + 4, val, role, 's', ha='left')
line(ax, [(x0, 6), (x0, 62)], 'fixe', lw=0.6, dash=True)
text(ax, 44, 60, 'avec l’exposant 2', 'sujet', 'm', weight='bold') if False else None
row(46, 'sujet', r'$\cos^2 x$', 0.5, '0,5')
row(35, 'autre', r'$1-\sin^2 x$', 0.5, '0,5')
text(ax, 44, 58, 'exposant 2 : égaux', 'resultat', 'm')
row(20, 'sujet', r'$\cos^2 x$', 0.5, '0,5')
row(9, 'autre', r'$1-\sin x$', 0.2929, '0,2929')
text(ax, 44, 31.5, 'sans exposant : différents', 'limite', 'm')
save(fig, '31-090')
