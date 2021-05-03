class Car:
    def __init__(self, tank=0.0):
        self.tank = tank

    def refuel(self, ref=0.0):
        self.tank += ref
        print('Your tank contains', round(self.tank, 1), 'liters.')

    def ride(self, distance=0):
        if self.tank >= 0.1:
            print('We are riding...')
        for i in range(0, distance+1):
            if self.tank >= 0.1:
                self.tank -= 0.1
            else:
                print('Refuel your car.')
                break
        if i > 0:
            print('We drove', i, 'kilometers. Your tank contains', round(self.tank, 1), 'liters')


car = Car()
car.refuel(10)
car.ride(78)
