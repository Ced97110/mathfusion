import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
# f : coefficients entiers
text(ax, 15, 49, r'dans $\mathbb{Z}[x]$', 'autre', 's')
box(ax, 3, 30, 24, 15, 'autre', label=r'$f=x^2+1$')
text(ax, 15, 25, r'irréductible sur $\mathbb{Q}$', 'autre', 's')
# les trois réductions
text(ax, 64.5, 69, r'dans $\mathbb{F}_p[x]$', 'sujet')
rows = [(52, 2, r'$f_2=(x+1)^2$', 'deux facteurs égaux'),
        (30, 3, r'$f_3=x^2+1$', 'irréductible'),
        (8, 5, r'$f_5=(x+2)(x+3)$', 'deux facteurs différents')]
for y, p, form, desc in rows:
    poly(ax, [(44, y), (85, y), (85, y + 15), (44, y + 15)], 'sujet')
    text(ax, 64.5, y + 10, form, 'sujet')
    text(ax, 64.5, y + 4, desc, 'sujet', 's')
    arrow(ax, (27, 37.5), (44, y + 7.5), 'varie')
mx = 35.5
text(ax, 33, 53, 'mod 2', 'varie', 's')
text(ax, mx, 40.5, 'mod 3', 'varie', 's')
text(ax, 40, 21, 'mod 5', 'varie', 's')
save(fig, '67-155')
