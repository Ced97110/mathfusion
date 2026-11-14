import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
L = 72; k = L / 4.32; x0 = 8
text(ax, 44, 82, 'ruban : 4,32 m', 'sujet', 'm')
box(ax, x0, 70, L, 8, 'sujet')
text(ax, 44, 62, r'$\div\,7$ : 7 parts égales', 'resultat', 'm')
for i in range(7):
    box(ax, x0 + i * L / 7, 50, L / 7, 8, 'resultat', r=0.3, lw=0.6)
text(ax, 44, 43, r'$\div\,1{,}8$ : « 1,8 part » ?', 'limite', 'm')
text(ax, 44, 33, 'combien de fois 1,8 m tient ?', 'autre', 'm') if False else text(ax, 44, 33, 'combien de fois 1,8 m ?', 'autre', 'm')
for i in range(2):
    box(ax, x0 + i * 1.8 * k, 18, 1.8 * k, 8, 'autre', label='1,8 m', size='s', r=0.3)
box(ax, x0 + 3.6 * k, 18, L - 3.6 * k, 8, 'autre', fill=False, dash=True, r=0.3)
save(fig, '08-057')
