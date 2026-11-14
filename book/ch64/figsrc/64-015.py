import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
labs = [r'$S_4$ : 24', r'$A_4$ : 12', r'$V$ : 4', r'$\{e\}$ : 1']
quo = [r'$S_4/A_4$ ≅ ℤ/2  (24÷12=2)', r'$A_4/V$ ≅ ℤ/3  (12÷4=3)', r'$V/\{e\}$ = $V$  (4÷1=4)']
for i, lab in enumerate(labs):
    y = 63 - i * 19
    box(ax, 6, y, 30, 11, 'sujet', label=lab, size='m')
    if i < 3:
        arrow(ax, (21, y - 0.5), (21, y - 7.5), 'resultat')
        text(ax, 27, y - 4, quo[i], 'resultat', 's', ha='left')
save(fig, '64-015')
