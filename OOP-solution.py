class Pod_Racer():
    def __init__(self, max_speed, condition, price, owner):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
        self.owner = owner

    def repair(self):
        self.condition = 'repaired'


class Anakin_Pod(Pod_Racer):
    def __init__(self, max_speed, condition, price, owner = "Anakin"):
        super().__init__(max_speed, condition, price, owner)

    def boost(self):
        print("Anakin used his boost!")
        self.max_speed *= 2

class Sebulba_Pod(Pod_Racer):
    def __init__(self, max_speed, condition, price, owner = "Sebulba"):
        super().__init__(max_speed, condition, price, owner)

    def flame_jet(self, other_pod):
        print('flaming', other_pod.owner)
        other_pod.condition = "trashed"

anakins_pod = Anakin_Pod(25, "perfect", 1000)

sebulbas_pod = Sebulba_Pod(50, "perfect", 1000000)

print("Anakin's pod is", anakins_pod.condition)
print("Sebulba's pod is", sebulbas_pod.condition)

sebulbas_pod.flame_jet(anakins_pod)

print("Anakin's pod is", anakins_pod.condition)
print("Sebulba's pod is", sebulbas_pod.condition)

anakins_pod.repair()

print("Anakin's pod is", anakins_pod.condition)
print("Sebulba's pod is", sebulbas_pod.condition)

print("Anakin's max speed is", anakins_pod.max_speed)
print("Sebulba's max speed is", sebulbas_pod.max_speed)

anakins_pod.boost()

print("Anakin's max speed is", anakins_pod.max_speed)
print("Sebulba's max speed is", sebulbas_pod.max_speed)

"""
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
Answer:
Encapsulation: key characteristics of the pod racers was bundled within the class and made it easier to reuse for multiple podracers.
Abstraction: X
Inheritance: anakins_pod and sebulbas_pod were able to inherit the general characteristics of a podracer, making it easier to store data.
Polymorphism: The repair method was used for more than just pod racer and can be used for all children under it's class.

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
Answer: I think using OOP was better in this solution since there were multiple aspects that we would have wanted to reuse. Functional
programming would have been more repetitive since the need was the same for multiple objects. 

How in particular did Object Oriented Programming assist in the solving of this problem?
It was a lot easier to apply the parent class Pod_Racer to the children class and instead of reconstruction the parameters into the class' objects,
we were able to reuse them. Less code means easier fixes down the road and easier additions as well.
"""