import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 1, 2, 86, 72, 'fixe', fill=True)
text(ax, 8, 68, r'$A$', 'sujet', 'l')
text(ax, 44, 68, 'nombres algébriques', 'fixe', 's')
box(ax, 8, 46, 20, 12, 'sujet', label=r'$\sqrt{2}$', size='m')
box(ax, 60, 46, 20, 12, 'sujet', label=r'$\sqrt{3}$', size='m')
text(ax, 44, 52, r'$+\ \times\ \div$', 'varie', 'l')
hub = (44, 38)
line(ax, [(18, 46), hub], 'varie', lw=1.1); line(ax, [(70, 46), hub], 'varie', lw=1.1)
res = [(4, r'$\sqrt{2}+\sqrt{3}$' + '\n' + r'$\approx 3{,}146$'), (31.5, r'$\sqrt{2}\times\sqrt{3}$'), (59, r'$\sqrt{2}\div\sqrt{3}$')]
for x, lab in res:
    box(ax, x, 14, 25, 13, 'resultat', label=lab, size='s')
    arrow(ax, hub, (x + 12.5, 27.8), 'varie')
text(ax, 17, 8, r'annule $x^4-10x^2+1$', 'resultat', 's')
save(fig, '66-080')
