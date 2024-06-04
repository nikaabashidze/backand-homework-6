class Heart:
    def __init__(self):
        self.usage = ""
        self.state = ""

    def check_state(self, rate):
        if rate > 70:
            self.state = "high blood pressure"
        else:
            self.state = "feeling good"
        return self.usage, self.state

class Brain:
    def __init__(self):
        self.usage = ""
        self.state = ""

    def check_state(self, rate):
        if rate > 90:
            self.state = "tired"
        else:
            self.state = "rested"
        return self.usage, self.state

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.heart = Heart()
        self.brain = Brain()

class Leg:
    def __init__(self, person):
        self.person = person
        self.moving_speed = 0
        self.state = ""

    def check_state(self):
        if self.moving_speed > 10:
            self.state = "running"
        elif self.moving_speed > 0:
            self.state = "walking"
        else:
            self.state = "standing"
        return self.state

person = Person("nicholas", 30)
leg = Leg(person)
leg.moving_speed = 15
heart_rate = 60
brain_rate = 95

person.heart.check_state(heart_rate)
person.brain.check_state(brain_rate)
leg.check_state()

print("Person:", person.name)
print("Heart state:", person.heart.state)
print("Brain state:", person.brain.state)
print("Leg state:", leg.state)