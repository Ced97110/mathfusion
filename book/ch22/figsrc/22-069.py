import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
s = 21; x0, y0 = 22, 18
for i in range(2):
    for j in range(2):
        poly(ax, [(x0+i*s, y0+j*s), (x0+(i+1)*s, y0+j*s), (x0+(i+1)*s, y0+(j+1)*s), (x0+i*s, y0+(j+1)*s)], 'varie')
        text(ax, x0+(i+.5)*s, y0+(j+.5)*s, '3', 'varie', 'l')
line(ax, [(x0+s, y0), (x0+s, y0+2*s)], 'resultat', lw=1.8)
line(ax, [(x0, y0+s), (x0+2*s, y0+s)], 'resultat', lw=1.8)
text(ax, 4, y0+s, 'aire 12', 'varie', 'm', ha='left')
text(ax, x0+2*s+3, y0+s, r'$12\div4=3$', 'encre', 's', ha='left')
brace(ax, x0, x0+s, y0+2*s, 'fixe', label=r'$\sqrt{3}$', down=False)
brace(ax, x0+s, x0+2*s, y0+2*s, 'fixe', label=r'$\sqrt{3}$', down=False)
brace(ax, x0, x0+2*s, y0, 'varie', label=r'$\sqrt{12}$')
save(fig, '22-069')
