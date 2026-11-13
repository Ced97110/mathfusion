import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def plane(cx, title):
    cy = 28
    arrow(ax, (cx-17, cy), (cx+17, cy), 'fixe', lw=0.6); arrow(ax, (cx, cy-17), (cx, cy+17), 'fixe', lw=0.6)
    text(ax, cx, 57, title, 'fixe', 's')
    return cy
cy = plane(22, 'plan habituel')
disc(ax, 22, cy, 1.6, 'sujet')
text(ax, 22, 8, r'$\nu=0$', 'sujet', 'l')
cy = plane(66, 'seconde mesure')
line(ax, [(66-13, cy-13), (66+13, cy+13)], 'sujet', lw=1.8)
disc(ax, 66, cy, 1.2, 'sujet')
text(ax, 66, 8, r'$\nu=1$', 'sujet', 'l')
text(ax, 22, 46, 'seul le vecteur nul', 'fixe', 's')
text(ax, 80, 47, 'droite de (1 ; 1)', 'sujet', 's', ha='right')
save(fig, '72-091')
