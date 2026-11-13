import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
O = (10, 26); u = 40
c, s = 0.5, math.sqrt(3) / 2
H_ = (O[0] + c * u, O[1]); P = (O[0] + c * u, O[1] + s * u)
poly(ax, [O, H_, P], 'fixe', fill=False, lw=0.8)
line(ax, [O, H_], 'sujet', lw=1.8); line(ax, [H_, P], 'autre', lw=1.8); line(ax, [O, P], 'resultat', lw=1.8)
line(ax, [(H_[0] - 2.5, H_[1]), (H_[0] - 2.5, H_[1] + 2.5), (H_[0], H_[1] + 2.5)], 'fixe', lw=0.6)
line(ax, [(O[0] + 8 * math.cos(a * 0.02), O[1] + 8 * math.sin(a * 0.02)) for a in range(0, 53)], 'varie', lw=0.8)
text(ax, 20, 21.5, '0,5', 'sujet', 's'); text(ax, 35, 43, '0,866', 'autre', 's')
text(ax, 15, 46, '1', 'resultat', 's'); text(ax, 23, 30.5, '60°', 'varie', 's')
text(ax, 67, 52, r'$0{,}5^2 = 0{,}25$', 'sujet', 'm'); text(ax, 67, 44, r'$0{,}866^2 = 0{,}75$', 'autre', 'm')
text(ax, 67, 36, '0,25 + 0,75 = 1', 'resultat', 'm')
box(ax, 6, 6, 19, 8, 'sujet', label='0,25', size='s'); box(ax, 25, 6, 57, 8, 'autre', label='0,75', size='s')
brace(ax, 6, 82, 14, 'resultat', label='1', down=False)
save(fig, '30-171')
