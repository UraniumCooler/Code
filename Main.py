import time

class Elevator:
    def __init__(self, currentFloor=0, totalFloors=10, waitTime=1.5):
        self.currentFloor = currentFloor
        self.totalFloors = totalFloors
        self.requests = []
        self.waitTime = waitTime  
        self.secretFloor = 257 

    def requestFloors(self, targetFloors):
        for targetFloor in targetFloors:
            if targetFloor < 0 or (targetFloor >= self.totalFloors and targetFloor != self.secretFloor):
                print(f"Ogiltig Våning: {targetFloor}. Välj en våning mellan 0 och {self.totalFloors - 1}")
            else:
                self.requests.append(targetFloor)
                print(f"Våning {targetFloor} efterfrågad.")
        
        
        self.sortRequests()

    def sortRequests(self):
        
        if not self.requests:
            return
        
        direction = None
        if self.currentFloor < min(self.requests):
            direction = 'up'
        elif self.currentFloor > max(self.requests):
            direction = 'down'
        
        
        if direction == 'up':
            self.requests.sort(key=lambda x: (abs(x - self.currentFloor), x))
        elif direction == 'down':
            self.requests.sort(key=lambda x: (abs(x - self.currentFloor), -x))
        else:
            
            self.requests.sort(key=lambda x: abs(x - self.currentFloor))

    def moveToNextFloor(self):
        if not self.requests:
            print("Ingen våning efterfrågad.")
            return
        
        nextFloor = self.requests.pop(0)
        floorsToMove = abs(nextFloor - self.currentFloor)
        print(f"Flyttar från våning {self.currentFloor} till våning {nextFloor}...")
        
        time.sleep(floorsToMove * self.waitTime)
        
        self.currentFloor = nextFloor
        
        
        if self.currentFloor == self.secretFloor:
            print("wat. välkommen till 'The Executive Suite', hur hittade du hit och varför orkade du?")
        else:
            print(f"Våning {self.currentFloor}.")

def main():
    elevator = Elevator()
    
    while True:
        action = input("Skriv 'e' för att efterfråga en eller flera våningar, 'f' för att flytta till nästa efterfrågade våning, eller ' ' för att avsluta: ").lower()
        
        if action == 'e':
            try:
                targetFloorsInput = input(f"Skriv vilka våningar du ska till (0-{elevator.totalFloors - 1}), separerade med kommatecken: ")
                targetFloors = [int(floor.strip()) for floor in targetFloorsInput.split(',')]
                elevator.requestFloors(targetFloors)
            except ValueError:
                print("Våning existerar inte.")
        
        elif action == 'f':
            elevator.moveToNextFloor()
        
        elif action == ' ':
            print("spränger hissen")
            break
        
        else:
            print("Äru blind? 'e', 'f', eller ' '.")

if __name__ == "__main__":
    main()
