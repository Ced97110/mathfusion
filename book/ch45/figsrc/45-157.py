import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
box(ax, 2, 8, 84, 36, 'sujet', fill=False, dash=True)
text(ax, 44, 39, r'calcul dans $G$ (interrupteur)', 'sujet', 's')
bw = 14
for x, h, v in ((8, r'$g_1$', '1'), (34, r'$g_2$', '1')):
    text(ax, x + bw / 2, 30, h, 'sujet', 'm'); box(ax, x, 15, bw, 11, 'sujet', label=v, size='l')
text(ax, 29, 20.5, '+', 'varie', 'l'); text(ax, 55, 20.5, '=', 'varie', 'l')
text(ax, 69, 30, r'$g_1g_2$', 'resultat', 'm'); box(ax, 62, 15, bw, 11, 'resultat', label='0', size='l')
text(ax, 44, 11, '1+1=2, reste 0', 'fixe', 's')
save(fig, '45-157')
