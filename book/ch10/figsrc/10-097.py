import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 2.4
box(ax, 14, 22, 20 * 2.9, 7 * u, 'sujet', label=r'$7\times20=140$', size='m', r=0.3)
box(ax, 14 + 58, 22, 3 * 2.9, 7 * u, 'varie', label='21', size='s', r=0.3)
brace(ax, 14, 72, 20, 'sujet', r'$20$', down=True) if False else None
brace(ax, 14, 72, 41, 'fixe', r'$20+3=23$', down=False)
brace(ax, 14, 14, 22, 'fixe') if False else None
line(ax, [(11, 22), (11, 22 + 7 * u)], 'resultat', lw=1.4); text(ax, 7, 22 + 7 * u / 2, '7', 'resultat', 'l')
text(ax, 14 + 29, 17, '20', 'sujet', 's'); text(ax, 14 + 58 + 4.35, 17, '3', 'varie', 's')
text(ax, 44, 7, r'$7\times20+7\times3=7\times(20+3)$', 'resultat', 'm')
save(fig, '10-097')
