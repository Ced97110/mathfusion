import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lbox(ax, x, y, w, h, role, label=None, **k): return box(ax, x, y, w, h, role, label=label, **k)
fig, ax = canvas(48)
lbox(ax, 3, 30, 22, 10, 'sujet', r'$1{,}7321$'); text(ax, 14, 44, 'côté gauche', 'sujet', 's')
arrow(ax, (27, 35), (39, 35), 'varie'); text(ax, 33, 41, r'$\times\frac{\cos x}{\cos x}$', 'varie', 's')
lbox(ax, 41, 33, 16, 8, 'fixe', r'$0{,}75$'); line(ax, [(41, 30.5), (57, 30.5)], 'encre'); lbox(ax, 41, 20, 16, 8, 'fixe', r'$0{,}4330$')
text(ax, 49, 15, r'$\cos x\,\cos x$ en haut', 'fixe', 's'); text(ax, 49, 10, r'$\cos x\,(1-\sin x)$ en bas', 'fixe', 's')
arrow(ax, (60, 30), (68, 30), 'varie'); lbox(ax, 70, 25, 16, 10, 'resultat', r'$1{,}7321$'); text(ax, 78, 20, 'même valeur', 'resultat', 's')
save(fig, '31-130')
