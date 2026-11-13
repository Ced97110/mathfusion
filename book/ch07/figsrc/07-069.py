import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def stack(ax, xc, yc, top, bot, w, rb="varie", rt="sujet", rbot="sujet", d=4.6, size="m"):
    line(ax, [(xc - w / 2, yc), (xc + w / 2, yc)], rb, lw=1.6)
    text(ax, xc, yc + d, top, rt, size); text(ax, xc, yc - d, bot, rbot, size)

fig, ax = canvas(96)
stack(ax, 44, 80, r'$\frac{1}{2} + \frac{1}{2}$', r'$\frac{1}{2}$', 30, rb='sujet', rt='sujet', rbot='sujet', d=7)
box(ax, 1, 8, 42, 46, 'resultat')
box(ax, 45, 8, 42, 46, 'limite')
arrow(ax, (36, 66), (22, 55.5), 'resultat')
arrow(ax, (52, 66), (66, 55.5), 'limite')
text(ax, 22, 48, 'la barre regroupe', 'resultat', 's', weight='bold')
text(ax, 66, 48, 'la barre ne regroupe pas', 'limite', 's', weight='bold')
text(ax, 22, 36, r'$(\frac{1}{2} + \frac{1}{2}) \div \frac{1}{2}$', 'resultat', 's')
text(ax, 22, 24, r'$1 \div \frac{1}{2}$', 'resultat', 'm')
text(ax, 22, 14, r'$= 2$', 'resultat', 'l')
text(ax, 66, 36, r'$\frac{1}{2} + \frac{1}{2} \div \frac{1}{2}$', 'limite', 's')
text(ax, 66, 24, r'$\frac{1}{2} + 1$', 'limite', 'm')
text(ax, 66, 14, r'$= \frac{3}{2}$', 'limite', 'l')
save(fig, '07-069')
