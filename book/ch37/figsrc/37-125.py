import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 52, 'côtés 10 ; 6 ; 4 : s = 10', 'fixe', 'm')
labs = ['$s$', '$s-a$', '$s-b$', '$s-c$']; vals = ['10', '0', '4', '6']
for i in range(4):
    x = 4.5 + i * 21
    role = 'varie' if vals[i] == '0' else 'sujet'
    text(ax, x + 8, 41, labs[i], role, 'm')
    box(ax, x, 28, 16, 9, role, label=vals[i], size='l')
    if i: text(ax, x - 2.5, 32.5, r'$\times$', 'fixe', 'm')
text(ax, 4.5 + 21 + 8, 22, '10 − 10 = 0', 'varie', 's')
arrow(ax, (44, 20), (44, 14), 'resultat')
box(ax, 22, 3, 44, 10, 'resultat', label='√0 = 0 : aire nulle', size='m')
save(fig, '37-125')
