import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
divs = [1, 2, 3, 4, 5, 6, 7, 10, 12]; cw, x0 = 7.2, 19
for c, d in enumerate(divs):
    text(ax, x0 + c * cw + 3, 43, str(d), 'sujet', 's')
for r, n in enumerate([7, 10, 12]):
    y = 30 - r * 10
    text(ax, 9, y + 3.5, f'ℤ/{n}ℤ', 'autre', 's')
    for c, d in enumerate(divs):
        on = n % d == 0
        box(ax, x0 + c * cw, y, cw - 0.8, 7, 'sujet' if on else 'fixe', fill=on, r=0.5)
text(ax, 44, 4, 'cases pleines = sous-groupes', 'resultat', 'm')
text(ax, 9, 43, 'k =', 'sujet', 's')
save(fig, '48-132')
