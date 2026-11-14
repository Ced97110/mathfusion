import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

total = 20
cos2, sin2 = 0.2, 0.8
assert abs(total * sin2 - 16) < 1e-9 and abs(total * cos2 - 4) < 1e-9
fig, ax = canvas(50)
text(ax, 44, 46, r'$\|u\times v\|^2=\|u\|^2\|v\|^2\sin^2\theta$', 'encre', 'm')
x0, x1, y, h = 6, 82, 20, 10
k = (x1 - x0) / total
xc = x0 + 4 * k
box(ax, x0, y, xc - x0, h, 'autre', label='4', r=0.4)
box(ax, xc, y, x1 - xc, h, 'sujet', label=r'16 $=\|u\times v\|^2$', r=0.4)
brace(ax, x0, x1, y + h, 'fixe', label=r'$\|u\|^2\|v\|^2=4\times5=20$', down=False)
brace(ax, x0, xc, y, 'autre', label=r'$\cos^2\theta=0{,}2$', down=True)
brace(ax, xc, x1, y, 'sujet', label=r'$\sin^2\theta=0{,}8$', down=True)
text(ax, 44, 3.5, '20 × 0,8 = 16', 'resultat', 'm')
save(fig, '41-116')
