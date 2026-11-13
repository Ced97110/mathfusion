import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def stack(ax, xc, yc, top, bot, w, rb="varie", rt="sujet", rbot="sujet", d=4.6, size="m"):
    line(ax, [(xc - w / 2, yc), (xc + w / 2, yc)], rb, lw=1.6)
    text(ax, xc, yc + d, top, rt, size); text(ax, xc, yc - d, bot, rbot, size)

fig, ax = canvas(62)
# row A: simple fraction
stack(ax, 18, 48, '12', '4', 10)
arrow(ax, (30, 48), (44, 48), 'varie')
text(ax, 65, 48, r'$12 \div 4 = 3$', 'resultat', 'l')
text(ax, 18, 36, 'barre = ÷', 'varie', 's')
# row B: complex fraction
stack(ax, 20, 15, r'$\frac{1}{2}$', r'$\frac{3}{4}$', 24, rt='fixe', rbot='fixe', d=7)
arrow(ax, (36, 15), (46, 15), 'varie')
text(ax, 66, 15, r'$\frac{1}{2} \div \frac{3}{4}$', 'sujet', 'l')
text(ax, 20, 2.5, 'barre longue = ÷', 'varie', 's')
text(ax, 62, 2.5, 'barres courtes : fractions', 'fixe', 's')
save(fig, '07-065')
