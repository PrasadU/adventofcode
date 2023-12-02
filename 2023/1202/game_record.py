class Game:
    gid: int
    sets: list
    
    def __init__(self, gid, sets):
        self.gid = gid
        self.sets = sets
        
    def total_for_colour(self, colour) -> int:
        total = 0
        for gs in self.sets:
            if 'red' == colour:
                total += gs.red
            if 'blue' == colour:
                total += gs.blue
            if 'green' == colour:
                total += gs.green
        return total

    def get_max(self) -> [(int, int, int)]:
        max_r = 0
        max_b = 0
        max_g = 0
        for gs in self.sets:
            if gs.red > max_r:
                max_r = gs.red
            if gs.blue > max_b:
                max_b = gs.blue
            if gs.green > max_g:
                max_g = gs.green
        return [(max_r, max_b, max_g)]
    
    def is_possible(self, maxes) -> bool:
        result = True
        g_maxes = self.get_max()
        if g_maxes[0][0] > maxes[0]:
            result = False
        if g_maxes[0][1] > maxes[1]:
            result = False
        if g_maxes[0][2] > maxes[2]:
            result = False   
        return result


class GameSet:
    
    def __init__(self, red, blue, green):
        self.red = red
        self.blue = blue
        self.green = green
