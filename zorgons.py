from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
		
            
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print "\n-------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud....if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this."
    ]
    
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
        
class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Pascel #25 have invaded your ship and destroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship after getting into an"
        print "escape pod."
        print "\n"
        print "You're running down the central corridor to the weapons armory when"
        print "a Gothon jumpsout, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you."
        
        action = raw_input("> ")
        
        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it to the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "your aim. Your laserhits his costume but misses him entirely. This"
            print "makes him fly into rage and blast you repeatedly into the face until"
            print "you are dead. Then he eats you."
            return 'death'
            
        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as Gothon's blaster cranks a laser past your head."
            print "In the middle your artful dodge, your foot slips and you"
            print "band your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'
            
        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy."
            print "You tell Gothon one of the joke you learnt."
            print "leshvislay pokari hara chi chi yanna ,mas ree kay. puru gassa."
            print "The Gothon starts laughing and you take this advantage and shoot him in the head."
            return 'laser_weapon_armory'
            
        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'
            
class LaserWeaponArmory(Scene):

    def enter(self):
        print "You do dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in the container. There's a keypad lock on the box"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb. the code is 3 digits."
        code = "123"
        guess = raw_input("[keypad]> ")
        guesses = 0
        
        while guess != code and guesses < 10:
            print "BZZZZEDDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
            
        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bpmb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time then you hear sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'
            
class TheBridge(Scene):

    def enter(self):
        print "You burst ont;o the Bridge with the neutron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to take control of the ship."
        print "each of them has an even uglier clown costume"
        print "than the last. They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't wanna set it off."
        
        action = raw_input("> ")
        
        if action == "throw the bomb":
            print "In panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door. Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'
            
        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat"
            print "You inch backward to the door, open it, and then slowly and carefully"
            print "place the bomb on the floor never taking your eye off from the"
            print "Gothons. You than jump back to the door, punch the close button"
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off the fucking ship!"
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"
            
class EscapePod(Scene):
    def enter(self):
        print "You rush through the ship desparately trying to make it to"
        print "the escape pod before the whole ship explodes. It seems like"
        print "hardly anyGothons are on the ship, so you run clear of"
        print "interference. You get to the chamber with escape pods, and"
        print "now need to pick up one to take. Some of them could be damaged"
        print "but yoy don't have time to lok. There's 5 pod, which one"
        print "do you take?"
        
        (good_pod) = "5"
        guess = raw_input("[pod #]> ")
        
        if guess != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures cushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into the space heading to"
            print "the planet below. As it flies to the planet, you look"
            print "back and see your ship implode and explode"
            print "like a bright star, taking out Gothon ship at the same time."
            print "YOU WON!"
            
            return 'finished'
            
class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
