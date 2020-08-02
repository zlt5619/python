import Program.Person.head as head
import Program.Person.body as body
import Program.Person.arm as arm
import Program.Person.leg as leg

class Person():
    def __init__(self,head,body,left_arm,right_arm,left_leg,right_leg):
        self.head=head
        self.body=body
        self.left_arm=left_arm
        self.right_arm=right_arm
        self.left_leg=left_leg
        self.right_leg=right_leg

    def move(self):
        print("123")

head=head.head()
body=body.body()
left_arm=arm.left_arm()
right_arm=arm.right_arm()
left_leg=leg.left_leg()
right_leg=leg.right_leg()


person=Person(head,body,left_arm,right_arm,left_leg,right_leg)
person.move()
person.head.say()