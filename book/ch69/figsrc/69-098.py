import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
ay = 34
# (centre, titre, signe de la pente, signes gauche/droite, comptes)
panels = [(22, r'$f$ décroît', -1, (r'$+,-$', r'$-,-$'), ('un changement', 'aucun')),
          (66, r'$f$ croît', 1, (r'$-,+$', r'$+,+$'), ('un changement', 'aucun'))]
for cx, title, s, signs, counts in panels:
    text(ax, cx, 66, title, 'sujet', 'm', weight='bold')
    line(ax, [(cx - 19, ay), (cx + 19, ay)], 'fixe')
    line(ax, [(cx, ay - 17), (cx, ay + 17)], 'fixe', dash=True, lw=0.6)
    line(ax, [(cx - 14, ay - s * 8), (cx + 14, ay + s * 8)], 'sujet', lw=1.3)
    line(ax, [(cx - 14, ay + s * 14), (cx + 14, ay + s * 14)], 'varie', lw=1.3)
    text(ax, cx - 9, 56, signs[0], 'encre', 'm')
    text(ax, cx + 9, 56, signs[1], 'encre', 'm')
    text(ax, cx - 9, 13, counts[0], 'varie', 's')
    text(ax, cx + 9, 13, counts[1], 'fixe', 's')
text(ax, 31, 40.5, r'$f_0$', 'sujet', 's')
text(ax, 31, 18.5, r'$f_1$', 'varie', 's')
text(ax, 18.5, 30.5, r'$c$', 'fixe', 's')
save(fig, '69-098')
