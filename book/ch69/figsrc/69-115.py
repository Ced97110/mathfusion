import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
w, g = 24.5, 5.0
x0 = (88 - 3 * w - 2 * g) / 2
labs = [r'1. calculer' + '\n' + r'$f(a)$ et $f(b)$', '2. une valeur' + '\n' + 'est nulle ?', '3. décaler' + '\n' + 'la borne']
for i in range(3):
    box(ax, x0 + i * (w + g), 42, w, 12, 'sujet' if i < 2 else 'varie', label=labs[i], size='s')
    if i < 2:
        arrow(ax, (x0 + i * (w + g) + w + 0.4, 48), (x0 + (i + 1) * (w + g) - 0.4, 48), 'fixe')
f = numberline(ax, 12, 72, 20, -2, 2, 1)
disc(ax, f(-1), 20, 1.6, 'sujet')
disc(ax, f(-1.5), 20, 1.6, 'resultat', fill=False)
disc(ax, f(2), 20, 1.6, 'sujet')
arrow(ax, (f(-1) - 1, 22.5), (f(-1.5) + 1, 22.5), 'varie', curve=0.6)
text(ax, f(-1), 31, r'$a=-1$' + '\n' + r'$f(a)=0$', 'sujet', 's')
text(ax, f(2), 31, r'$b=2$' + '\n' + r'$f(b)=3$', 'sujet', 's')
text(ax, f(-1.5), 7, 'nouvelle borne' + '\n' + r'$a=-1{,}5$', 'resultat', 's')
save(fig, '69-115')
