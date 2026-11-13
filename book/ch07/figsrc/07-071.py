import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def stack(ax, xc, yc, top, bot, w, rb="varie", rt="sujet", rbot="sujet", d=4.6, size="m"):
    line(ax, [(xc - w / 2, yc), (xc + w / 2, yc)], rb, lw=1.6)
    text(ax, xc, yc + d, top, rt, size); text(ax, xc, yc - d, bot, rbot, size)

fig, ax = canvas(92)
def row(y, topB, botA):
    stack(ax, 28, y, '5', botA, 10, rb='fixe', rt='sujet', rbot='varie')
    text(ax, 42, y, r'$\times$', 'fixe', 'l')
    stack(ax, 60, y, topB, '17', 12, rb='fixe', rt='varie', rbot='sujet')
row(74, '24', '8')
stack(ax, 28, 46, '5', '8', 10, rb='fixe', rt='sujet', rbot='varie')
text(ax, 42, 46, r'$\times$', 'fixe', 'l')
line(ax, [(54, 46), (66, 46)], 'fixe', lw=1.6)
text(ax, 57, 51, '8', 'varie', 'm'); text(ax, 63, 51, r'$\times 3$', 'sujet', 'm')
text(ax, 60, 41.5, '17', 'sujet', 'm')
text(ax, 44, 62, '24 = 8 × 3', 'varie', 's')
text(ax, 44, 34, 'les deux 8 se simplifient', 'varie', 's')
arrow(ax, (44, 31), (44, 24), 'fixe')
text(ax, 44, 14, r'$\frac{5 \times 3}{17} = \frac{15}{17}$', 'resultat', 'l')
save(fig, '07-071')
