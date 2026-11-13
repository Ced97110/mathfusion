import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
s, g = 7.5, 1.0
text(ax, 44, 64, r'$2\cdot 3+2\cdot(-3)=2\cdot(3+(-3))$', 'encre', 's')
xb, xo = 8, 49
for r in range(2):
    y = 40 - r*(s+g+1)
    for c in range(3):
        box(ax, xb + c*(s+g), y, s, s, 'sujet', r=0.6)
        box(ax, xo + c*(s+g), y, s, s, 'autre', r=0.6)
    text(ax, 44, y + s/2, '+', 'encre', 'l')
text(ax, xb + 1.5*(s+g) - g/2, 51, r'$3$', 'sujet', 'm')
text(ax, xo + 1.5*(s+g) - g/2, 51, r'$-3$', 'autre', 'm')
text(ax, 4, 49, '2 lignes', 'varie', 's', ha='left') if False else None
text(ax, 44, 25, 'chaque ligne vaut 0 : total 0', 'varie', 's')
text(ax, 44, 18, r'$2\cdot(-3)$ est l’opposé de 6', 'varie', 's')
text(ax, 44, 8, r'$2\cdot(-3)=-6$', 'resultat', 'm')
save(fig, '51-202')
