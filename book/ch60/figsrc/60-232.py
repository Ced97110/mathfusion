import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
s = 6
text(ax, 44, 74, r'$n=540$ : exposants 2, 3, 1', 'sujet', 'm', weight='bold')
def stack(x, n, role):
    for k in range(n):
        box(ax, x, 50 + k * s, 7, s - 0.8, role, r=0.5)
stack(8, 2, 'sujet'); stack(30, 3, 'sujet'); stack(52, 1, 'sujet')
text(ax, 11.5, 45, r'$P(2)=2$', 'sujet', 's')
text(ax, 33.5, 45, r'$P(3)=3$', 'sujet', 's')
text(ax, 55.5, 45, r'$P(1)=1$', 'sujet', 's')
text(ax, 21, 53, r'$\times$', 'varie', 'l')
text(ax, 43, 53, r'$\times$', 'varie', 'l')
text(ax, 72, 53, r'$=6$', 'resultat', 'l', weight='bold')
line(ax, [(4, 36), (84, 36)], 'fixe', dash=True)
text(ax, 44, 30, r'$n=32=2^5$ : un exposant, 5', 'autre', 'm', weight='bold')
for i in range(7):
    box(ax, 8 + i * 8, 15, 7, 7, 'autre', r=0.5)
text(ax, 44, 8, r'$P(5)=7$ groupes', 'autre', 'm')
save(fig, '60-232')
