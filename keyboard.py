import random
import json # In order to read the data. 

symbols = [i for i in 'ABCDEFGHIJKLMNOPQRTSUVWXYZ,.?']
places = [i for i in range(0,29)]

tm = 1.032 # Top to middle
tb = 2.138 # Top to bottom
mb = 1.118 # Middle to bottom
ne = 1.000 # Same row next key 
tmd = 1.605 # Top to middle diagonally
tbd = 2.661 # Top to bottom diagonally 
mtd = 1.247 # Middle to top diagonally
mbd = 1.803 # Middle to bottom diagonally
btd = 2.015 # Bottom to top diagonally

distances = {( 0,  1): tm,  ( 1,  0): tm, 
			 ( 0,  2): tb,  ( 2,  0): tb, 
			 ( 1,  2): mb,  ( 2,  1): mb,
			 ( 3,  4): tm,  ( 4,  3): tm,
			 ( 3,  5): tb,  ( 5,  3): tb, 
			 ( 4,  5): mb,  ( 5,  4): mb,
			 ( 6,  7): tm,  ( 7,  6): tm, 
			 ( 6,  8): tb,  ( 8,  6): tb,
			 ( 7,  8): mb,  ( 8,  7): mb,
			 ( 9, 10): tm,  (10,  9): tm, 
			 ( 9, 11): tb,  (11,  9): tb, 
			 ( 9, 12): ne,  (12,  9): ne,
			 ( 9, 13): tmd, (13,  9): tmd,
			 ( 9, 14): tbd, (14,  9): tbd,
			 (10, 11): mb,  (11, 10): mb,
			 (10, 12): mtd, (12, 10): mtd,
			 (10, 13): ne,  (13, 10): ne, 
			 (10, 14): mbd, (14, 10): mbd,
			 (11, 12): btd, (12, 11): btd,
			 (11, 13): mb,  (13, 11): mb, 
			 (11, 14): ne,  (14, 11): ne,
			 (12, 13): tm,  (13, 12): tm, 
			 (12, 14): tb,  (14, 12): tb,
			 (13, 14): mb,  (14, 13): mb, 
			 (15, 16): tm,  (16, 15): tm,
			 (15, 17): tb,  (17, 15): tb,
			 (15, 18): ne,  (18, 15): ne,
			 (15, 19): tmd, (19, 15): tmd,
			 (15, 20): tbd, (20, 15): tbd,
			 (16, 17): mb,  (17, 16): mb,
			 (16, 18): mtd, (18, 16): mtd,
			 (16, 19): ne,  (19, 16): ne,
			 (16, 20): mbd, (20, 16): mbd,
			 (17, 18): btd, (18, 17): btd,
			 (17, 19): mb,  (19, 17): mb,
			 (17, 20): ne,  (20, 17): ne,
			 (18, 19): tm,  (19, 18): tm,
			 (18, 20): tb,  (20, 18): tb, 
			 (19, 20): mb,  (20, 19): mb,
			 (21, 22): tm,  (22, 21): tm,
			 (21, 23): tb,  (23, 21): tb,
			 (22, 23): mb,  (23, 22): mb, 
			 (24, 25): tm,  (25, 24): tm,
			 (24, 26): tb,  (26, 24): tb,
			 (25, 26): mb,  (26, 25): mb,
			 (27, 28): tm,  (28, 27): tm,
			 (27, 29): tb,  (29, 27): tb,
			 (28, 29): mb,  (29, 28): mb
			 }
# # From center to upper row distance
# cur = 1.032
# # From center to lower row
# clr = 1.118
# # Top to bottom
# ttb = 2.138
# # Index finger distances
# # FT, UH
# ft = 1.247
# # FG, RT, HJ, YU, NM
# fg = 1.0
# # FB, HM
# fb = 1.803
# # RG, YJ
# rg = 1.605 
# # RB, YM
# rb = 2.661

# # RV, TB = ttb
# # TG = cur
# # TV, UN 
# tv = 2.015
# # GB = clr
# # GV = clr
# # JH = 1.0
# # JN = clr
# # YH = cur
# # YN = ttb
# # HN = clr

# distances = {(0,1): cur, (1,0): cur,
#              (0,2): ttb, (2,0): ttb,
#              (1,2): clr, (2,1): clr,
#              (3,4): cur, (4,3): cur,
#              (3,5): ttb, (5,3): ttb,
#              (4,5): clr, (5,4): clr,
#              (6,7): cur, (7,6): cur,
#              (6,8): ttb, (8,6): ttb,
#              (7,8): clr, (8,7): clr,
#              (21,22): cur, (22,21): cur,
#              (21,23): ttb, (23,21): ttb,
#              (22,23): clr, (23,22): clr,
#              (24,25): cur, (25,24): cur,
#              (24,26): ttb, (26,24): ttb,
#              (25,26): clr, (26,25): clr,
#              (27,28): cur, (28,27): cur,
#              (27,29): ttb, (29,28): ttb,
#              (28,29): clr, (29,28): clr,
#              (9,10): cur, (10,9): cur,
#              (9,11): ttb, (11,9): ttb,
#              (10,11): clr, (11,10): clr,
#              (10,12): ft,  (12,10): ft,
#              (10,13): fg,  (13,10): fg, 
#              (10,14): fb,  (14,10): fb, 
#              (9, 12): fg,  (12, 9): fg,
#              (9, 13): rg,  (13, 9): rg,
#              (9, 14): rb,  (14, 9): rb, 
#              (12,13): cur, (13,12): cur, 
#              (12,14): ttb, (14,12): ttb,
#              (11, 12): tv, (12,11): tv,
#              (13,14): clr, (14,13): clr,
#              (11,13): clr, (13,11): clr,
#              (11,14): fg, (14,11): fg, 
#              (15,16): cur, (16,15): cur,
#              (15,17): ttb, (17,15): ttb,
#              (15,18): fg, (18,15): fg,
#              (15,19): rg, (19,15): rg,
#              (15,20): rb, (20,15): rb,
#              (16,17): clr, (17,16): clr,
#              (16,18): ft, (18,16): ft,
#              (16,19): fg, (19,16): fg,
#              (16,20): fb, (20,16): fb, 
#              (17,18): tv, (18,17): tv,
#              (17,19): clr, (19,17): clr,
#              (17,20): fg,  (20,17): fg, 
#              (18,19): cur, (19,18): cur,
#              (18,20): ttb, (20,18): ttb,
#              (19,20): clr, (20,19): clr
#              }


class Population():
    """Keeps track of the different generations. Should I keep only the first generation?"""
    def __init__(self, size):
        # size: population size
        self.size = size
        self.keyboards = [Keyboard() for _ in range(0,self.size)]
        self.sorted = False

    def average_fitness(self):
        fitness = 0
        for kbd in self.keyboards:
            fitness += kbd.fitness
        return fitness / self.size

    def best_fitness(self):
        self.sort_by_fitness()
        return self.keyboards[0].fitness

    def sort_by_fitness(self): 
        if not self.sorted:
            self.keyboards.sort(key = lambda k: k.fitness)
            self.sorted = True

    def generate_new_generation(self):
        self.sort_by_fitness()
        new_gen = []

        # Keep top 10% 
        keep = self.size // 10 

        for i in range(0, keep+1): 
            new_gen.append(self.keyboards[i])

        # For the top 50% randomly mate each pairs to create new keyboards. 
        half = self.size // 2
        while len(new_gen) < self.size: 
            i = random.randint(0, half+1)
            j = random.randint(0, half+1)
            new_keyboard = Keyboard(self.keyboards[i], self.keyboards[j])
            new_gen.append(new_keyboard)

        self.sorted = False
        self.keyboards = new_gen

class Keyboard():
    def __init__(self, *parents):
        if parents: 
            self.layout = self.generate_layout_from_parents(parents)
        else: 
            self.layout = self.generate_layout_randomly()
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        """ Calculate the fitness of the keyboard. """
        total_penalty = 0
        # This will eat a list of distances between keys. 
        # It will also use a data set from ArXiv e.g. 
        # We need to constantly keep track of where the fingers are. 
        # Fingers stay on key last pressed until used again. 
        # TODO: The last assumption should be changed. 
        # Fingers should return to base position after a certain number of keys and 
        # after each space. 
        # Also give a slight bonus if certain finger combinations are used.
        # E.g. a rolling finger motion with the same hand.
        text = "the quick brown fox jumps over the lazy dog.".upper()
        # self.layout = dict(zip('QAZWSXEDCRFVTGBYHNUJMIK,OL.P?', [i for i in range(0,30)])) # For QWERTY
        finger_positions = [1, 4, 7, 10, 19, 22, 25, 28]
        with open('./arxiv-metadata-oai-snapshot.json', 'r') as file: 
            i = 0
            for jsonObj in file: 
                i += 1
                if i > 1000: # Use the 1000 first abstracts only.
                    break
                entry = json.loads(jsonObj) 
                text = str(entry['abstract']).upper()
                previous_finger = ' '
                for letter in text: 
                    if letter in symbols:
                        l = self.layout[letter]
                        # If the finger is already in position, add no penatly. 
                        if l in finger_positions: 
                            continue
                        elif l in [0,1,2]: # Left little finger.
                            total_penalty += distances[(finger_positions[0], l)]
                            if previous_finger == 'll': # Same finger twice
                                total_penalty += .5
                            elif previous_finger[0] == 'r': # If other hand 
                                total_penalty -= .5
                            finger_positions[0] = l # Move finger.
                            previous_finger = 'll' 
                        elif l in [3, 4, 5]: # Left ring finger. 
                            total_penalty += distances[(finger_positions[1], l)]
                            if previous_finger == 'lr': 
                                total_penalty += .5 
                            elif previous_finger[0] == 'r': 
                                total_penalty -= .5
                            finger_positions[1] = l 
                            previous_finger = 'lr' 
                        elif l in [6, 7, 8]: # Left middle finger.
                            total_penalty += distances[(finger_positions[2], l)]
                            if previous_finger == 'lm':
                                total_penalty += .5
                            elif previous_finger[0] == 'r': 
                                total_penalty -=.5
                            finger_positions[2] = l 
                            previous_finger = 'lm' 
                        elif l in [9, 10, 11, 12, 13, 14]: # Left index finger. 
                            total_penalty += distances[(finger_positions[3], l)]
                            if previous_finger == 'li':
                                total_penalty += .5
                            elif previous_finger[0] == 'r': 
                                total_penalty -=.5
                            finger_positions[3] = l 
                            previous_finger = 'li' 
                        elif l in [15, 16, 17, 18, 19, 20]: # Right index finger.
                            total_penalty += distances[(finger_positions[4], l)]
                            if previous_finger == 'ri':
                                total_penalty += .5
                            elif previous_finger[0] == 'l': 
                                total_penalty -=.5
                            finger_positions[4] = l 
                            previous_finger = 'ri'
                        elif l in [21, 22, 23]: # Right middle finger.
                            total_penalty += distances[(finger_positions[5], l)]
                            if previous_finger == 'rm':
                                total_penalty += .5
                            elif previous_finger[0] == 'l': 
                                total_penalty -=.5
                            finger_positions[5] = l 
                            previous_finger = 'rm'
                        elif l in [24, 25, 26]: # Right ring finger. 
                            total_penalty += distances[(finger_positions[6], l)]
                            if previous_finger == 'rr':
                                total_penalty += .5
                            elif previous_finger[0] == 'l': 
                                total_penalty -=.5
                            finger_positions[6] = l 
                            previous_finger = 'rr'
                        elif l in [27, 28, 29]: # Right little finger.
                            total_penalty += distances[(finger_positions[7], l)]
                            if previous_finger == 'rl':
                                total_penalty += .5
                            elif previous_finger[0] == 'l': 
                                total_penalty -=.5
                            finger_positions[7] = l 
                            previous_finger = 'rl'

        return total_penalty
    
    @staticmethod
    def generate_layout_from_parents(parents):
        layout = {}
        coins = [random.randint(0,1) for _ in range(0,30)]
        for i, key in enumerate(parents[0].layout.keys()):
            if key not in layout.keys():
                proposed_position = parents[coins[i]].layout[key]
                while proposed_position in layout.values(): 
                    # Move to next available position.
                    proposed_position += 1 
                    proposed_position %= 30 
                layout[key] = proposed_position
        # Choose half of the keys from one and half from the other. 
        # layout = dict(zip('QAZWSXEDCRFVTGBYHNUJMIK,OL.P?',[i for i in range(0,30)])) # For QWERTY
        return layout
    
    @staticmethod
    def generate_layout_randomly():
        random.shuffle(places)
        layout = dict(zip(symbols, places))
        return layout

    @staticmethod
    def distances(a,b): 
        return distances[(a,b)] 

    def __add__(self, other):

        """ Returns a keyboard that is a child of both keyboards. """
        return Keyboard(self, other) 
    

# Keyboards should be able to generate themselves randomly? 
# Keyboards should able to mate. kbd1 + kbd2 gives a new child. 
# A new generation should be generated at each step. 


