import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(84)
U = 3.6                      # 1 unité = 3,6 mm
r = math.sqrt(55)
Y = 40
# rectangle 5 x 11 et carré de côté racine de 55 : même aire 55
box(ax, 4, Y, 11 * U, 5 * U, 'sujet', r=0.2)
text(ax, 4 + 11 * U / 2 + 3, Y + 5 * U / 2, 'aire 55', 'sujet', 's')
arrow(ax, (7.5, Y + 1.2), (7.5, Y + 5 * U - 1.2), 'sujet', both=True, lw=0.8)
text(ax, 11, Y + 5 * U / 2 - 5, r'$p = 5$', 'sujet', 's', ha='left')
brace(ax, 4, 4 + 11 * U, Y, 'autre', label=r'$q = 11$')
box(ax, 50, Y, r * U, r * U, 'fixe', dash=True, r=0.2)
text(ax, 50 + r * U / 2, Y + r * U / 2, 'aire 55', 'fixe', 's')
brace(ax, 50, 50 + r * U, Y, 'fixe', label=r'$\sqrt{55} \approx 7{,}4$')
# l'ordre sur une droite
g = numberline(ax, 6, 76, 14, 0, 12, step=1, labels=False, arrow_right=False)
for v, role, lab in ((5, 'sujet', r'$p$'), (r, 'fixe', r'$\sqrt{n}$'), (11, 'autre', r'$q$')):
    disc(ax, g(v), 14, 1.3, role)
    text(ax, g(v), 8, lab, role, 'm')
text(ax, 44, 22, r'$p \leq \sqrt{n} \leq q$', 'encre', 'l')
save(fig, '53-165')
