
# importera saker som behövs för koden
import pygame
import pgzrun
import random
import time

# storleken på fönstret
WIDTH = 1000
HEIGHT = 750

# olika variabler i spelet dom ger vad värdet är i början t.ex poäng man börjar med 0 poäng.
poäng_ = 0
speed = 10
liv = 3
tid = time.time()
tid2 = 0
xStorlek = 150
yStorlek = 150
fönster = "meny"

# hjärt ikonerna får variabler och en ny storlek
heart = Actor("heartr")
heart._surf = pygame.transform.scale(heart._surf, ((100), (100)))
heart._update_pos()

heart2 = Actor("heartr")
heart2._surf = pygame.transform.scale(heart2._surf, ((100), (100)))
heart2._update_pos()

heart3 = Actor("heartr")
heart3._surf = pygame.transform.scale(heart3._surf, ((100), (100)))
heart3._update_pos()

# måltavlan får en variabel så den sedan kan användas i koden
moltavla = Actor("bear")

# gör att det bästa resultatet sedan komer kunas sparas i ett dockument.
highscore_file = open("highscores.txt", "r")
highscore = int(highscore_file.read())
highscore_file.close()

# gör en funkstoin där jag kan skriva ut text i spelet för olika fönster.
def draw():
    screen.fill((125, 165, 232))

    # när menyn är det aktiva fönstret så kommer sakerna nedan stå på skärmen
    if fönster == "meny":
        screen.draw.text("För att spela tryck mellanslag", center=(500, 300), shadow=(1, 1), color="white", fontsize=80, gcolor="Red")
        screen.draw.text("Highscore: " + str(highscore), color="red", shadow=(1, 1), center=(500, 200), fontsize=80, gcolor="blue", angle=10, owidth=2)
        screen.draw.text("F för fullskärm", center=(500, 400), shadow=(1, 1), color="white", fontsize=80, gcolor="purple")
        screen.draw.text("W för halvskärm", center=(500, 500), shadow=(1, 1), color="white", fontsize=80, gcolor="purple")

    # när spelet är det aktiva fönstret kommer ikonerna visas och dina poäng och tiden.
    if fönster == "spel":
        moltavla.draw()
        heart.draw()
        heart2.draw()
        heart3.draw()

        # gör poängen texten utsende anorlunda och ger den en posistion
        screen.draw.text("poäng: " + str(poäng_), center=(500, 30), color="pink", shadow=(1, 1), fontsize=60,
                         gcolor="purple")
        # Visar tiden inan du förlorar ett hjärta och om den sedan blir kortare tid vsar den det
        tid1 = round(time.time() - tid)
        screen.draw.text("time:" + str(tid1) + "/" + str(sec), (800, 10), color="orange", shadow=(1, 1), fontsize=60,
                         gcolor="Yellow")
    # om du förlorr kommer du till slutet den visar poängen du fick och dit bästa resultat och att du kan spela igen
    if fönster == "slut":
        screen.draw.text("poäng: " + str(poäng_), center=(500, 300), shadow=(1, 1), fontsize=60, gcolor="Yellow")
        screen.draw.text("Till menyn tryck B", center=(500, 400), shadow=(1, 1), fontsize=60, gcolor="Red")
        screen.draw.text("Highscore: " + str(highscore), center=(500, 200), shadow=(1, 1), fontsize=60, gcolor="Yellow")


# En funkstion för att köra spelet och starta det fån menyn och slut.
def update():
    global poäng_, liv, speed, fönster, highscore, tid1, tid, tid2, sec, xStorlek, yStorlek

    # måltavlan får en storlek i spelet
    moltavla._surf = pygame.transform.scale(moltavla._surf, ((xStorlek), (yStorlek)))
    moltavla._update_pos()

    # visar var hjärtana är om du har 3 liv och om du har fler en 3 liv har du 3 liv
    if liv > 3:
        liv==3
    if liv == 3:
        heart.x = 330
        heart2.x = 430
        heart3.x = 530

    # om du trycker mellanslag när du är i menyn så kommer du till spelet
    if fönster == "meny":
        if keyboard.space:
            fönster = "spel"

            # vsar vad värden på variabler är i börja av spelet
            poäng_ = 0
            tid = time.time()
            xStorlek = 150
            yStorlek = 150
            moltavla._surf = pygame.transform.scale(moltavla._surf, ((xStorlek), (yStorlek)))
            moltavla._update_pos()  # gör om måltavlans storlek

             # gör så måltavlan rör sig höger pga att fet blir plus 10 x pär speed.

    # bestämer var måltavlorna kan spawna
    if moltavla.left > WIDTH:
        moltavla.right = 0
        moltavla.y = random.randint(75, 600)
        moltavla.x = random.randint(1, 500)

    # visar vad som händer med hjärtana när du förlorar ett liv alltså dom försviner från skärmen
    # (är utanför storleken av skärmen igentligen)
    if fönster == "spel":
        moltavla.x += speed
        if liv == 2:
            heart3.x -= 600
        if liv == 1:
            heart2.x -= 500
        if liv == 0:
            heart.x -= 400

        # timer
        tid2 = round(time.time() - tid)

        # gör så destu fler poäng du får desdu snabare behöver du trycka på måltavlorna för att inte förlora liv
        # tar om pängen är midre än 10 komer du ha 3 sec men om det går upp till 3 sek komer ett liv försvina
        if poäng_ < 10:
            sec = 3
            if tid2 > 3:
                liv -= 1
                tid = time.time()

        if poäng_ > 10:
            sec = 2
            if tid2 > 2:
                liv -= 1
                tid = time.time()

        if poäng_ > 20:
            sec = 1
            if tid2 > 1:
                liv -= 1
                tid = time.time()

# när man dör
# Gör alla variabler till deras gammla värden förutom fönster
    if liv < 1:
        fönster = "slut"
        speed = 10
        heart.x = 330
        heart2.x = 430
        heart3.x = 530


# om poängen du får ar mer en dit highscore så ändras highscore till poängen du har och sedan sparar det nya highscoret
    if poäng_ > highscore:
        highscore = poäng_
        highscore_file = open("highscores.txt", "w")
        highscore_file.write(str(poäng_))
        highscore_file.close()

# gör så du kommer till menyn från slutet om du trycker på b
    if fönster == "slut":
        if keyboard.b:
            fönster = "meny"
            tid = time.time()
            liv = 3

# om du trycker på en måltavla komer du få ett poäng och speed blir snabara på måltavlorna och måltavlan försviner
def on_mouse_down(pos):
    global poäng_, speed, liv, tid, xStorlek, yStorlek
    if fönster == "spel":
        if moltavla.collidepoint(pos):
            poäng_ += 1
            # visar var måltvalorna är för programet och spelaren ser var dom är/spawnar
            moltavla.right = 0
            moltavla.y = random.randint(75, 600)
            moltavla.x = random.randint(1, 500)
            speed += 0.1
            tid = time.time()

        # om spelarn trycker och misar en måltavla förloras 1 liv
        else:
            liv -= 1
            print(pos)


# Fullskärms läge och halvskär. En funkstion som gör att du kan gi in i fluskärm och ut från det.
def on_key_down(key):
    if key == key.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif key == key.W:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))

pgzrun.go()  #spelet körs och skärmen stanar kvar.

