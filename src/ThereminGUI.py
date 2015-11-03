import sys
import os
import pygame
import LeapTheremin
sys.path.append("../lib")
import Leap


class GUI():
    width = 1024
    height = 600

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.theremin = LeapTheremin.ThereminListener()
        self.controller = Leap.Controller()
        self.controller.add_listener(self.theremin)
        self.lefthandpos = (self.width / 2 - 200, self.height / 2)
        self.righthandpos = (self.width / 2 + 200, self.height / 2)

    def getpositions(self):
        self.lefthandpos = tuple(
            (-1 * int(self.theremin.get_left_hand_pos().get("y")) + self.width / 2, self.height / 2))
        self.righthandpos = tuple(
            (self.width / 2, -1 * int(self.theremin.get_right_hand_pos().get("y")) + self.height / 2))


def main():
    gui = GUI()
    lefthand = pygame.image.load(os.path.join("../lib", "lefthand.png"))
    righthand = pygame.image.load(os.path.join("../lib", "righthand.png"))
    therepic = pygame.image.load(os.path.join("../lib", "blacktheremin.png"))
    lefthand.set_colorkey((255, 255, 255))
    righthand.set_colorkey((255, 255, 255))
    therepic.set_colorkey((255, 255, 255))
    lefthand.convert_alpha()
    righthand.convert_alpha()
    therepic.convert_alpha()
    myfont = pygame.font.SysFont("monospace", 15)
    lefthandtextbox = myfont.render("{}".format(gui.lefthandpos),1,(0,0,0))
    righthandtextbox = myfont.render("{}".format(gui.righthandpos),1,(0,0,0))

    # threading
    # self.interval = interval
    # thread = threading.Thread(target=self.run, args=())
    # thread.daemon = True                            # Daemonize thread
    # thread.start()         ?                       # Start the execution
    while True:
        gui.screen.fill((255, 255, 255))
        gui.getpositions()
        print gui.lefthandpos, gui.righthandpos
        th = pygame.draw.rect(
            gui.screen, (255, 255, 255), (gui.width / 2 - 100 / 2, gui.height / 2 + 50 / 2 - 150, 100, 50), 0)
        rh = pygame.draw.circle(gui.screen, (0, 0, 255), (gui.lefthandpos[0] + 100, gui.lefthandpos[1] + 100), 20, 0)
        lh = pygame.draw.circle(gui.screen, (255, 0, 0), (gui.righthandpos[0] + 100, gui.righthandpos[1] + 100), 20, 0)
        gui.screen.blit(therepic, (gui.width / 2 - 100 / 2 - 300, gui.height / 2 - 50 / 2 - 200, 100, 50))
        gui.screen.blit(righthand, gui.righthandpos)
        gui.screen.blit(lefthand, gui.lefthandpos)
        gui.screen.blit(lefthandtextbox, (50, 50))
        gui.screen.blit(lefthandtextbox, (gui.width - 200, 50))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gui.controller.remove_listener(gui.theremin)
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
