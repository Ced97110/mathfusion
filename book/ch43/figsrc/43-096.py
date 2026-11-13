import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(105)
text(ax, 4, 100, 'égalité', 'fixe', 's', ha='left')
text(ax, 44, 93, r'$g(\nu(a))=g(\bar{a})=f(a)$', 'resultat', 's')
line(ax, [(2, 87), (86, 87)], 'fixe', lw=0.5)
text(ax, 4, 83, 'injectivité', 'fixe', 's', ha='left')
steps = [r'$g(\bar{a})=g(\bar{b})$', r'$f(a)=f(b)$', r'$a\,E_f\,b$', r'$\bar{a}=\bar{b}$']
roles = ['sujet', 'fixe', 'varie', 'resultat']; ys = [74, 62, 50, 38]
for s, r, y in zip(steps, roles, ys): box(ax, 12, y - 4, 38, 8, r, label=s, size='s')
for k, lab in enumerate([r'déf. de $g$', r'déf. de $E_f$', 'même classe']):
    arrow(ax, (31, ys[k] - 4.3), (31, ys[k + 1] + 4.3), 'fixe'); text(ax, 54, (ys[k] + ys[k + 1]) / 2, lab, 'fixe', 's', ha='left')
line(ax, [(2, 29), (86, 29)], 'fixe', lw=0.5)
text(ax, 4, 25, 'unicité', 'fixe', 's', ha='left')
text(ax, 44, 17, r'$h(\bar{a})=f(a)=g(\bar{a})$', 'resultat', 's')
text(ax, 44, 6, r'donc $h=g$', 'resultat', 's')
save(fig, '43-096')
