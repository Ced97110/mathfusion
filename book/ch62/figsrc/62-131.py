import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, 'trois racines de $x^3+x+1$,\ncaractéristique 2', 'encre', 'm')
labs = [r'$r_1$', r'$r_1^2$', r'$r_1^4$']
roles = ['sujet', 'varie', 'autre']
for i in range(3):
    box(ax, 3 + i * 31, 46, 22, 13, roles[i], label=labs[i], size='l')
for i in range(2):
    arrow(ax, (25.5 + i * 31, 52.5), (33.5 + i * 31, 52.5), 'varie')
    text(ax, 29.5 + i * 31, 62.5, 'au carré', 'varie', 's')
text(ax, 64, 40, r'$r_1^4=r_1^2+r_1$', 'autre', 's')
box(ax, 3, 14, 82, 17, 'varie', label=r'clé : $(a+b)^2=a^2+b^2$' + '\n' + 'le carré d’une racine est une racine', size='s')
text(ax, 44, 6, r'$r_1^3=r_1+1$, donc $r_1^4=r_1^2+r_1$', 'encre', 's')
save(fig, '62-131')
