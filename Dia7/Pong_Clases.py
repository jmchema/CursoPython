#Vamos a meter en una clase el juego del pong de emulador.py que hicimos el dia anterior

# La importaciones

from time import sleep
from sense_emu import SenseHat


class PongController:
    def __init__(self):
        self.sense = SenseHat()
        self.sense.stick.direction_up = self.move_up
        self.sense.stick.direction_down = self.move_down
        self.y = 4
        self.ball_position = [3, 3]
        self.ball_velocity = [1, 1]

    def draw_bat(self):
        self.sense.set_pixel(0, self.y, 255, 255, 255)
        self.sense.set_pixel(0, self.y+1, 255, 255, 255)
        self.sense.set_pixel(0, self.y-1, 255, 255, 255)

    def move_up(self,event):
        #global y
        if self.y > 1 and event.action=='pressed':
            self.y -= 1
        print(event)

    def move_down(self,event):
        global y
        if self.y < 6 and event.action=='pressed':
            self.y += 1
        print(event)

    def draw_ball(self):
        self.sense.set_pixel(self.ball_position[0], self.ball_position[1], 0, 0, 255)
        self.ball_position[0] += self.ball_velocity[0]
        self.ball_position[1] += self.ball_velocity[1]
        if self.ball_position[0] == 7:
            self.ball_velocity[0] = -self.ball_velocity[0]
        if self.ball_position[1] == 0 or self.ball_position[1] == 7:
            self.ball_velocity[1] = -self.ball_velocity[1]
        if self.ball_position[0] == 0:
            self.sense.show_message("You Lose", text_colour=(255, 0, 0))
            quit()
        if self.ball_position[0] == 1 and self.y - 1 <= self.ball_position[1] <= self.y+1:
            self.ball_velocity[0] = -self.ball_velocity[0]


controller = PongController()
while True:
    controller.sense.clear(0, 0, 0)
    controller.draw_bat()
    controller.draw_ball()
    sleep(0.25)

