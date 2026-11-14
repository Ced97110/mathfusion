import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
W_, H_ = 18, 13

def square(x0, tl, tr, bl, br, op):
    xl, xr = x0, x0 + 24
    box(ax, xl, 36, W_, H_, 'sujet', label=tl, size='s')
    box(ax, xr, 36, W_, H_, 'sujet', label=tr, size='s')
    box(ax, xl, 8, W_, H_, 'resultat', label=bl, size='s')
    box(ax, xr, 8, W_, H_, 'resultat', label=br, size='s')
    arrow(ax, (xl + W_ + 0.5, 42.5), (xr - 0.5, 42.5), 'varie', lw=1.2)
    arrow(ax, (xl + W_ + 0.5, 14.5), (xr - 0.5, 14.5), 'varie', lw=1.2)
    arrow(ax, (xl + W_ / 2, 35.5), (xl + W_ / 2, 21.5), 'varie', lw=1.2)
    arrow(ax, (xr + W_ / 2, 35.5), (xr + W_ / 2, 21.5), 'varie', lw=1.2)
    text(ax, (xl + xr + W_) / 2, 46, op, 'varie', 's')
    text(ax, xl + W_ / 2 - 3.5, 28.5, r'$\eta$', 'varie', 's')

square(1.5, '(2 ; 1)\n(1 ; 4)', '(3 ; 5)', '0 et −7', '−7', '+')
square(45.5, '(1 ; 4)', '(3 ; 12)', '−7', '−21', r'$\times 3$')
text(ax, 22, 60, 'somme', 'encre', 'm', weight='bold')
text(ax, 66, 60, 'action', 'encre', 'm', weight='bold')
line(ax, [(44, 4), (44, 56)], 'fixe', lw=0.5, dash=True)
save(fig, '57-150')
