class Car(object):
    def __init__ (self, model, colour, company, speed_limit):
        self.colour=colour
        self.model=model
        self.company=company
        self.speed_limit=speed_limit

    def start(self):
        print("started")
    
    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating")
        "accelerator functionality"
        
    def change_gear(self, gear_type):
        print("gear changed")
        "gear related functionality"

audi=Car("a6", "red", "audi", 80)
print(audi.start())
    