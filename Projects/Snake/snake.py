import random   #Zufallszahl
import curses   #wird für einen Display Terminal verwendet


s = curses.initscr()    #Fenster wird initialisiert
curses.curs_set(0)  #Cursor wird auf 0 gesetzt, damit er nicht angezeigt wird
sh, sw = s.getmaxyx()   #die Höhe und die Weite werden festgelegt
w = curses.newwin(sh, sw, 0, 0)    #neues Fenster wird geöffnet, verwendet Höhe und Weite und beginnt im linken oberen Eck
w.keypad(1)     #legt fest, dass das Fenster Tastatureingaben akzeptiert
w.timeout(100)  #Millisekunden, gibt an wie lang es dauert, bis das Zeichen (die Snake) neu geladen wird und dadurch wie schnell sie sich bewegt

snk_x = sw//4    #gibt den Ausgangspunkt der Snake an (Weite des Fensters durch 4)
snk_y = sh//2    #gibt den Ausgangspunkt der Snake an (Höhe des Fensters durch 2)

snake = [                   #hier werden die drei Startkörperteile der Snake angelegt
    [snk_y, snk_x],
    [snk_y, snk_x-1],       #1 hinter dem ersten
    [snk_y, snk_x-2]        #2 hinter dem ersten
]

food = [sh//2, sw//2]     #Ausgangspunkt für das Futter der Schlange ist in der Mitte des Bildschirms
w.addch(food[0], food[1], curses.ACS_PI)    #das Futter wird ins Fenster hinzugefügt und sieht aus wie das PI Symbol

key = curses.KEY_RIGHT      #Hier wird der Snake gesagt wo sie sich zu Anfang hin bewegen soll --> nach rechts!

while True:         #unendlicher loop für die bewegung der Snake
    next_key = w.getch()    #dadurch weiß das Programm welche die nächste Taste ist
    key = key if next_key == -1 else next_key   #gibt dem Programm entweder nichts (Snake fährt in selbe Richtung weiter) oder die nächste Taste (Richtungsänderung)

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:       #Bedingung für verlieren des Spiels, Snake ist entweder an den Rand des Fensters oder in sich selbst gefahren
        curses.endwin()     #Fenster wird geschlossen und Programm beendet
        quit()

    new_head = [snake[0][0], snake[0][1]]     #legt die neue Position des Kopfes fest bei Bewegung

    if key == curses.KEY_DOWN:              #Befehle für die Bewegung der Schlange
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)       #neuer Snakekopf wird eingefügt

    if snake[0] == food:        #Abfrage ob Snake das Futter erwischt hat
        food = None
        while food is None:
            nf = [                          #neuer zufälliger Ort für neues Futter wird festgelegt, maximal 1 Feld vom Rand entfernt
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None      #check ob das neue futter in der Schlange ist, wenn ja wird geloopt und ein neues futter erstellt
        w.addch(food[0], food[1], curses.ACS_PI)        #futter wird ins fenster hinzugefügt
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

