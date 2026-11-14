import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 52, r'code BCH $(255,\,231)$', 'sujet', 'l', weight='bold')
T = 76.0; x0 = 6.0
wm = T * 231 / 255
box(ax, x0, 34, wm, 8, 'resultat', label='message : 231 bits', size='s', r=0.4)
box(ax, x0 + wm, 34, T - wm, 8, 'varie', label='24', size='s', r=0.4)
text(ax, 44, 27, r'$255 - 231 = 24$ = degré de $g$', 'varie', 's')
text(ax, 44, 19, r'même calcul pour $(15,\,7)$ : $15-7=8$', 'fixe', 's')
wm2 = T * 7 / 15
box(ax, x0, 7, wm2, 8, 'resultat', label='message : 7', size='s', r=0.4)
box(ax, x0 + wm2, 7, T - wm2, 8, 'varie', label='contrôle : 8', size='s', r=0.4)
save(fig, '68-213')
