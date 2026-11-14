import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
def frac(x, y, n, d, role, w, size='s'):
    text(ax, x, y + 3.2, n, role, size); line(ax, [(x - w / 2, y), (x + w / 2, y)], role, lw=0.8); text(ax, x, y - 3.2, d, role, size)
frac(44, 84, r'$\sin A\cos B+\cos A\sin B$', r'$\cos A\cos B-\sin A\sin B$', 'sujet', 56)
arrow(ax, (44, 74), (44, 58), 'varie', lw=1.4)
text(ax, 50, 66, r'en haut et en bas : $\div\ \cos A\cos B$', 'varie', 's', ha='left')
frac(44, 48, r'$\tan A+\tan B$', r'$1-\tan A\tan B$', 'resultat', 34, 'm')
text(ax, 44, 30, '0,9659 ÷ 0,6124 = 1,5774', 'fixe', 's')
text(ax, 44, 22, '0,2588 ÷ 0,6124 = 0,4226', 'fixe', 's')
text(ax, 44, 12, '1,5774 = 1 + 0,5774', 'fixe', 's')
save(fig, '34-067')
