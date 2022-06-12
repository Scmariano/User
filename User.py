# Create a file with the User class, including the __init__ with all the attributes, parameters and default values.
class User:
    def __init__ (self, first_name, last_name, email, age):
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
        self.age = age
        self.rewards_member = False
        self.gold_card_points = 0

# display_info(self) - Have this method print all of the users' details on separate lines.
    def display_info(self):
        print()
        print(f"Name : {self.firstName} {self.lastName} \nEmail: {self.email} \nAge: {self.age}")
        print(f"Member : {self.rewards_member}\nPoints : {self.gold_card_points}")

#enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self):
    # BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.    
        rewards = self.rewards_member
        if rewards is True:
            print("User already a member")
            return False
        self.rewards_member = True
        self.gold_card_points = 200

# spend_points(self, amount) - have this method decrease the user's points by the amount specified.
# BONUS: Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("You're over-spending above you're limit")
        
    
User_Stephen = User("Stephen", "Mariano", "stephen@gmail.com", 32)
User_Chelsea = User("Chelsea", "Mariano", "chelsea@gmail.com", 30)
User_Luke = User("Luke", "Skywalker", "luke@gmail.com", 22)
User_Stephen.display_info()
# Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.
User_Stephen.enroll()
User_Stephen.display_info()
# Have the first user spend 50 points
User_Stephen.spend_points(50)
print(f"Current points : {User_Stephen.gold_card_points}")
# Have the second user enroll.
User_Chelsea.enroll()
User_Chelsea.display_info()
# Have the second user spend 80 points
User_Chelsea.spend_points(80)
print(f"Current points : {User_Chelsea.gold_card_points}")
User_Luke.enroll()
User_Luke.display_info()
User_Luke.spend_points(40)
print(f"Current points : {User_Luke.gold_card_points}")

