import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
text(ax, 44, 48, r'$m_1 = 1 + x + x^4$', 'sujet', 'l', weight='bold')
labs = [r'$\omega$', r'$\omega^2$', r'$\omega^4$', r'$\omega^8$']
roles = ['sujet', 'resultat', 'resultat', 'resultat']
w, g, x0, y, h = 14, 8, 4, 24, 9
for i in range(4):
    box(ax, x0 + i * (w + g), y, w, h, roles[i], label=labs[i], size='l')
for i in range(3):
    xa = x0 + i * (w + g) + w
    arrow(ax, (xa + 0.6, y + h / 2), (xa + g - 0.6, y + h / 2), 'varie')
    text(ax, xa + g / 2, y + h / 2 + 3.4, 'carré', 'varie', 's')
brace(ax, x0, x0 + 3 * (w + g) + w, y + h + 1, 'sujet', r'quatre racines de $m_1$', down=False)
xc_last = x0 + 3 * (w + g) + w / 2
xc_first = x0 + w / 2
arrow(ax, (xc_last, y - 0.5), (xc_first, y - 0.5), 'varie', curve=-0.35)
text(ax, 44, 8, r'$\omega^{16} = \omega$ : retour au début', 'varie', 's')
save(fig, '68-210')
