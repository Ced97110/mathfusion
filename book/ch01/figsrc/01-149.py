import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
r1 = [('1','fixe'),('3','fixe'),('0','autre'),('5','autre')]
r2 = [('1','fixe'),('3','fixe'),('5','sujet'),('0','sujet')]
for i in range(4):
    box(ax, 30+10*i, 52, 10, 10, r1[i][1], label=r1[i][0], size='l')
    box(ax, 30+10*i, 38, 10, 10, r2[i][1], label=r2[i][0], size='l')
text(ax, 15, 57, 'rang 2', 'autre', 's')
text(ax, 15, 43, '10 × rang 1', 'sujet', 's')
brace(ax, 30, 50, 63, 'fixe', label='1 300 en commun', down=False)
brace(ax, 50, 70, 37, 'varie', label='05 contre 50', down=True)
text(ax, 44, 24, 'écart : 50 − 5 = 45', 'resultat', 'l')
text(ax, 44, 14, '45 = 9 × 5 : divisible par 9', 'resultat', 'm')
save(fig, '01-149')
