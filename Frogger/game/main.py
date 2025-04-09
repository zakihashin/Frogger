import pygame as pg
import random as rn


pg.init()

screen = pg.display.set_mode((500, 800))
pg.display.set_caption("Frogger on Foenem")


bg = pg.image.load("assets/background.png")
bg = pg.transform.scale(bg, (500, 800))
playerimage = pg.image.load("assets/frog.png")
playerimage = pg.transform.scale(playerimage, (60, 40))
roadimg = pg.image.load("assets/road.png")
roadimg = pg.transform.scale(roadimg, (500, 200))
carimg = pg.image.load("assets/street/left/1.png")
carimg = pg.transform.scale(carimg, (60, 60))
logimg = pg.image.load("assets/river/right/middle.png")
logimg = pg.transform.scale(logimg, (150, 60))
waterimg = pg.image.load("assets/river/water.png")
waterimg = pg.transform.scale(waterimg, (500, 200))
grassimg = pg.image.load("assets/grass.png")
grassimg = pg.transform.scale(grassimg, (500, 200))


x = 250
y = 750
width = 60
height = 40
accelerate = 5


def create_cars():
    cars = []
    for i in range(3):
        x_pos = rn.randint(0, 500)
        y_pos = rn.randint(400, 600) // 100 * 100  
        speed = rn.randint(3, 5)
        cars.append([x_pos, y_pos, speed, 60, 40])
    return cars


def create_logs():
    logs = []
    for j in range(2):
        x_pos = rn.randint(0, 500)
        y_pos = rn.randint(200, 300) // 100 * 100 
        speed = rn.randint(2, 4)
        logs.append([x_pos, y_pos, speed, 120, 40])
    return logs

def move_cars(cars):
    for car in cars:
        car[0] += car[2]  
        if car[0] > 500:  
            car[0] = -60  


def move_logs(logs):
    for log in logs:
        log[0] += log[2] 
        if log[0] > 500: 
            log[0] = -120 


def check_car_collision(frog, cars):
    for car in cars:
        car_rect = pg.Rect(car[0], car[1], car[3], car[4])  
        if frog.colliderect(car_rect):  
            return True
    return False


def check_log_collision(frog, logs):
    for log in logs:
        log_rect = pg.Rect(log[0], log[1], log[3], log[4]) 
        if frog.colliderect(log_rect): 
            return log 


def events():
    global x, y
    cars = create_cars()
    logs = create_logs()

    frog = pg.Rect(x, y, width, height) 
    is_on_log = None  

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            x -= accelerate
        if keys[pg.K_RIGHT]:
            x += accelerate
        if keys[pg.K_UP]:
            y -= accelerate
        if keys[pg.K_DOWN]:
            y += accelerate


        if x < 0:
            x = 0
        if x > 500 - width:
            x = 500 - width
        if y < 0:
            y = 0
        if y > 800 - height:
            y = 800 - height


        frog.x = x
        frog.y = y

        move_cars(cars)
        move_logs(logs)


        if check_car_collision(frog, cars):
            print("Game Over! You hit a car.")
            running = False

        if y <= 0:
            print("You reached the top! You win!")
            running = False


        if y < 300:
            if not check_log_collision(frog, logs):
                print("Game Over! You fell into the water.")
                running = False
            else:
                is_on_log = check_log_collision(frog, logs)
                if is_on_log:
                    x += is_on_log[2] 


        screen.fill((0, 0, 0))  
        screen.blit(bg, (0, 0))  
        screen.blit(roadimg, (0, 400))  
        screen.blit(waterimg, (0, 100))  
        screen.blit(grassimg, (0, 600)) 

        for car in cars:
            car_rect = pg.Rect(car[0], car[1], car[3], car[4])  
            screen.blit(carimg, car_rect.topleft) 

        for log in logs:
            log_rect = pg.Rect(log[0], log[1], log[3], log[4]) 
            screen.blit(logimg, log_rect.topleft) 

        screen.blit(playerimage, (x, y))


        pg.display.update()
        pg.time.Clock().tick(60) 

    pg.quit()

events()