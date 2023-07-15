class Spiderman:

    # spider bite
    def __init__(self):
        print("Spiderman was bitten by a spider")
    
    def spiderweb(self):
        print("Shoot webs")

    def spider_sense(self, danger):
        if danger:
            print("Activate spider-sense")
        else:
            print("No danger")

class MilesMorales(Spiderman):

    def __init__(self):
        print("Miles Morales gets bitten by a spider")
    
    def spiderweb(self):
        print("Requires accessories")
        return super().spiderweb() # Use the function of the parent class

    def electrical(self):
        print("Electric shock")

class SpiderGwen(Spiderman):

    def __init__(self):
        print("Gwen Stacy gets bitten by a spider")

    def pink_spiderweb(self):
        print("Pink spiderweb")
        return super().spiderweb()
    
class LittleSpider(MilesMorales, SpiderGwen):
    
    def __init__(self):
        print("Baby")
        
    def electrical(self):
        return super().electrical()

    def pink_spiderweb(self):
        return super().pink_spiderweb()

    def spider_sense(self, danger):
        return super().spider_sense(danger)

miles = MilesMorales()
miles.spiderweb()

gwen = SpiderGwen()
gwen.pink_spiderweb()

littlespider = LittleSpider()
littlespider.electrical()
littlespider.pink_spiderweb()
littlespider.spider_sense(True)