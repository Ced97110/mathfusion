import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cx, cy, u = 24, 30, 16
th = math.pi / 3
arrow(ax, (cx - 19, cy), (cx + 19, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - 19), (cx, cy + 19), 'fixe', lw=0.6)
disc(ax, cx, cy, u, 'fixe', fill=False, lw=0.6)
line(ax, [(cx, cy), (cx + 1.15 * u * math.cos(th), cy + 1.15 * u * math.sin(th))], 'fixe', lw=0.9, dash=True)
px, py = cx - u * math.cos(th), cy - u * math.sin(th)
arrow(ax, (cx, cy), (px + 0.5, py + 0.8), 'varie', lw=1.2)
disc(ax, px, py, 1.2, 'sujet')
text(ax, cx + 11, cy + 18.5, r'$\theta=\pi/3$', 'fixe', 's', ha='left')
text(ax, 9, 24, r'$r=-1$', 'varie', 's')
text(ax, 24, 7.5, r'$(-0{,}5\,;\,-0{,}866)$', 'sujet', 's')
box(ax, 52, 38, 34, 14, 'resultat', label='gauche : (0,25 + 0,75)²\n= 1', size='s')
text(ax, 69, 34, '=', 'resultat', 'l')
box(ax, 52, 16, 34, 14, 'resultat', label='droite : −0,125 + 1,125\n= 1', size='s')
save(fig, '40-111')
