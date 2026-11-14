import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 69, r'$b_3 = a_1^2a_4 + a_3^2 - 4a_2a_4$', 'sujet', 'm')
s = 60.0 / 121699
x0 = 14.0
A, B, C, R = 60690, 61009, 84840, 36859
box(ax, x0, 44, A * s, 8, 'sujet', label='60 690', size='s', r=0.6)
box(ax, x0 + A * s, 44, B * s, 8, 'sujet', label='61 009', size='s', r=0.6)
brace(ax, x0, x0 + A * s - 0.5, 43, 'sujet', r'$a_1^2a_4$', down=True)
brace(ax, x0 + A * s + 0.5, x0 + (A + B) * s, 43, 'sujet', r'$a_3^2$', down=True)
brace(ax, x0, x0 + (A + B) * s, 53, 'fixe', '121 699', down=False)
box(ax, x0, 18, R * s, 8, 'resultat', label='36 859', size='s', r=0.6)
box(ax, x0 + R * s, 18, C * s, 8, 'varie', label='−84 840', size='s', r=0.6)
brace(ax, x0, x0 + R * s - 0.5, 17, 'resultat', r'$41\times31\times29$', down=True)
brace(ax, x0 + R * s + 0.5, x0 + (R + C) * s, 17, 'varie', r'$4a_2a_4$', down=True)
save(fig, '65-090')
