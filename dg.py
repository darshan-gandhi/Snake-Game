import random
import curses
# testing git
#initialize
screen=curses.initscr()
curses.curs_set(0)
#get coordinates
sh,sw=screen.getmaxyx()

w=curses.newwin(sh,sw,0,0)
w.keypad(1)
w.timeout(100)

snake_x=sw/6
snake_y=sh/2

snake= [

    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

food=[sh/4, sw/6 ]

w.addch(food[0], food[1],"*")

key=curses.KEY_RIGHT

score=0
# screen.addstr(sh-sh/8 , sw- sw/8,"YOUR SCORE IS" )
# screen.refresh()
# w.addch(sh - sh /4, sw - sw / 4, f"darshan gandhi{score}")
while True :
    new_key=w.getch()
    key=key if new_key==-1 else new_key

    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        # screen.addstr(sh/2, sw/2,"total score")
        # screen.refresh()
        curses.endwin()
        quit()

    new_head= [snake[0][0], snake[0][1]]

    if key==curses.KEY_DOWN:
        new_head[0]+=1
    if key==curses.KEY_UP:
        new_head[0]+=-1
    if key==curses.KEY_RIGHT:
        new_head[1]+=1
    if key==curses.KEY_LEFT:
        new_head[1]+=-1

    snake.insert(0, new_head)

    if snake[0]==food :

        food=None

        while food is None :
            nf = [

                random.randint(1,sh-1),
                random.randint(1,sw-1)
            ]
            score+=1 if nf not in snake else None
            food = nf if nf not in snake else None
            # screen.addstr(sh - sh /4, sw - sw / 4, "YOUR SCORE IS")
            # screen.refresh()
            # w.addch(sh - sh /4, sw - sw / 4, int(score))
        w.addch(food[0], food[1],"*")
    else :
        tail=snake.pop()
        w.addch(int(tail[0]),int(tail[1]), ' ')


    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

