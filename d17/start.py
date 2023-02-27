#define class
class User:
    #what happens when triggered
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

        #set default value
        self.followers = 0
        self.following = 0

    #create method, always need to have a 'self' parameter
    def follow(self, user):
        user.followers += 1
        self.following += 1

#link object to class
user_1 = User("001", "test1")
user_2 = User("002", "test2")

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)


# #manually define attributes
# user_1.id = "001"
# user_1.name = "test"

