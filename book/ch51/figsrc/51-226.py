import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(100)
box(ax,6,88,76,9,'sujet',label=r'$D$ intègre fini, $a\neq0$')
rows=[('1. reste dans $D^*$',r'$ax\neq0$','sujet'),('2. injective',r'$ax_1=ax_2\Rightarrow x_1=x_2$','sujet'),
      ('3. surjective',r'fini : $m$ départs, $m$ places','varie'),('4. 1 est atteint',r'$ad=1$','sujet')]
top=88; ys=[]
for i,(a,b,role) in enumerate(rows):
    y=72-i*16; ys.append(y)
    box(ax,6,y,76,11,role,lw=2.0 if role=='varie' else 0.8)
    text(ax,9,y+5.5,a,role,'m',ha='left'); text(ax,79,y+5.5,b,role,'s' if i==2 else 'm',ha='right')
    arrow(ax,(44,y+16),(44,y+11.6) if i else (44,88-0.0),'fixe',lw=0.9) if False else None
prev=88
for i,y in enumerate(ys):
    arrow(ax,(44,prev-0.3),(44,y+11.6),'fixe',lw=0.9); prev=y
box(ax,6,8,76,9,'resultat',label=r'arrivée : $a$ a un inverse')
arrow(ax,(44,ys[-1]-0.3),(44,17.6),'fixe',lw=0.9)
text(ax,66,ys[2]+13.5,'étape décisive','varie','s')
save(fig,'51-226')
