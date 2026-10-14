from pico2d import *
import random

class Ballon:
    def __init__(self):
        self.x,self.y=random.randint(0,800),90
        self.frame=random.randint(0,7)
        self.image=random.randint(0,1)
        self.speed=random.randint(2,15)
        self.StopY=570
        self.stopY=600      
        if(self.image==0):
            self.image=load_image('ball21x21.png')
        else:
            self.image=load_image('ball41x41.png')
            pass

    def update(self):
        self.frame=(self.frame+1)%8

        self.y+=self.speed

        if(self.y>=self.stopY|self.y>=self.StopY):
            self.y=self.stopY
            self.y=self.StopY

    def draw(self):
        self.image.draw(self.x,self.y)

class Boy:           
    def __init__(self):
        self.x, self.y=random.randint(0,800),90
        self.frame=random.randint(0,7)
        self.image=load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x+=5
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)

    def update(self):pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
             running = False

def reset_world():
    global running

    running= True
    #세계에 존재하는 객체들을 담는 world list를 만든다
    global world
    world=[]
    #땅 객체를 생성하고 world list에 추가한다.
    global grass
    grass=Grass()
    world.append(grass)
    #소년 객체를 생성하고 world list에 추가한다.
    global team
    team=[Boy() for i in range(50)]
    world+=team

    global ballons
    ballons=[Ballon() for i in range(20)]
    world+=ballons

def update_world():
    for obj in world:
        obj.update()
    pass

def render_world():
    clear_canvas()
    for obj in world:
        obj.draw()
    update_canvas()


open_canvas()
reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
