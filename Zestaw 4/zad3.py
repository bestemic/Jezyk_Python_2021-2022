import pygame
from random import randint

from pygame import image

pygame.init()

# kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)


class Rakietka(pygame.sprite.Sprite):
    # klasa Rakietka dziedziczy z klasy "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy najpierw konstruktor klasy bazowej (Sprite)
        # dzięki metodzie super() dziedziczymy wszystkie elementy klasy bazowej
        super().__init__()

        # przekazanie koloru Rakietka oraz szerokości i wysokości, kolor tła i ustawienie go na przezroczyste
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysuję Rakietka jako prostokąt
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x > 700-self.image.get_width():
            self.rect.x = 700-self.image.get_width()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x < 0:
            self.rect.x = 0


class Pilka(pygame.sprite.Sprite):
    # klasa Pilka dziedziczy ze "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy konstruktor klasy bazowej
        super().__init__()

        # przekazujemy rozmiary, kolor, przezroczystość
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysowanie piłki (jako prostokącika)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # losowanie prędkości
        self.velocity = [randint(2, 6), randint(2, 6)]
        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[1] = -self.velocity[1]
        self.velocity[0] = randint(-6, 6)


topscore = 0

# definiujemy rozmiary i otwieramy nowe okno
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

rakietkaA = Rakietka(BIALY, 100, 10)
pileczka = Pilka(BIALY, 10, 10)

# lista wszystkich widzalnych obiektów potomnych z klasy Sprite
all_sprites_list = pygame.sprite.Group()

# dodanie obu rakietek i piłeczki do listy
all_sprites_list.add(rakietkaA)
all_sprites_list.add(pileczka)

# zaczynamy właściwy blok programu
kontynuuj = True
graj = True

# służy do kontroli liczby klatek na sekudnę (fps)
clock = pygame.time.Clock()


# -------- GLÓWNA PĘTLA PROGRAMU -----------
while kontynuuj:

    rakietkaA.rect.x = size[0]/2-50
    rakietkaA.rect.y = size[1]-50
    pileczka.rect.x = randint(190, 610)
    pileczka.rect.y = 100

    if(graj):
        # Początkowe wyniki graczy
        scoreA = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # zamknięcie okienka
            kontynuuj = False

    while graj:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:  # zamknięcie okienka
                graj = False
        # ruchy obiektów Rakietkas klawisze strzałka góra dół lub klawisz w s
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            rakietkaA.moveRight(5)
        if keys[pygame.K_LEFT]:
            rakietkaA.moveLeft(5)

        # aktualizacja listy duszków
        all_sprites_list.update()

        # sprawdzenie czy piłeczka nie uderza w którąś ścianę
        # i odpowiednie naliczenie punktu jeśli minie rakietkę A lub B i uderzy w ścianę za nią
        if pileczka.rect.x >= 690:
            pileczka.velocity[0] = -pileczka.velocity[0]
        if pileczka.rect.x <= 0:
            pileczka.velocity[0] = -pileczka.velocity[0]
        if pileczka.rect.y > 490:
            graj = False
        if pileczka.rect.y < 0:
            pileczka.velocity[1] = -pileczka.velocity[1]

        # sprawdzenie kolizji piłeczki z obiektem rakietkaA lub rakietkaB
        if pygame.sprite.collide_mask(pileczka, rakietkaA):
            scoreA += 1
            pileczka.bounce()

        # RYSOWANIE
        # czarny ekran
        screen.fill(CZARNY)

        # narysowanie obiektów
        all_sprites_list.draw(screen)

        # wyświetlanie wyników
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, BIALY)
        screen.blit(text, (325, 10))

        # odświeżenie / przerysowanie całego ekranu
        pygame.display.flip()

        # 60 klatek na sekundę
        clock.tick(60)

    if scoreA > topscore:
        topscore = scoreA

    font = pygame.font.Font(None, 60)
    screen.fill(CZARNY)
    text = font.render("Twój wynik: " + str(scoreA), 1, BIALY)
    text_rect = text.get_rect(center=(size[0]/2, 100))
    screen.blit(text, text_rect)
    text = font.render("Najlepszy wynik: " + str(topscore), 1, BIALY)
    text_rect = text.get_rect(center=(size[0]/2, 150))
    screen.blit(text, text_rect)
    font = pygame.font.Font(None, 35)
    text = font.render("Wciśnij G aby zagrać jeszcze raz", 1, BIALY)
    text_rect = text.get_rect(center=(size[0]/2, 300))
    screen.blit(text, text_rect)
    text = font.render("Wciśnij ESC aby wyjść z gry", 1, BIALY)
    text_rect = text.get_rect(center=(size[0]/2, 350))
    screen.blit(text, text_rect)

    pygame.display.flip()

    caps = pygame.key.get_pressed()
    if caps[pygame.K_ESCAPE]:
        kontynuuj = False
    if caps[pygame.K_g]:
        graj = True


pygame.quit()
