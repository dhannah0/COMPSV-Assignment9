class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []  

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def __repr__(self):
        return f"Person({self.name})"


class SocialNetwork:
    def __init__(self):
        self.people = {}  

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network.")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people or person2_name not in self.people:
            print(f"Friendship not created. One or both people don't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        if person1_name == person2_name:
            print(f"{person1_name} cannot be friends with themselves.")
            return

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        print("\nSocial Network:")
        for name, person in self.people.items():
            friend_names = [f.name for f in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")



if __name__ == "__main__":
    network = SocialNetwork()

    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    network.add_person("Jordan")

    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Jordan", "Johnny")  
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    network.print_network()



# """
# Design Memo

# A graph is the best structure to represent a social network because it naturally shows how people connect to one another. In a social network, every person can have many friends, and those friendships can form in any direction. A graph makes it possible to show these two way relationships with edges that connect people as nodes. It also allows the network to grow easily since new people and friendships can be added without changing the overall structure.

# A list or a tree would not work as well for this task. A list can only show one direction of data and it does not allow easy back and forth connections. A tree forces a parent and child structure which is too rigid for friendships since no one person should be above another in the network. In real life, friendships are mutual and flexible, which is what a graph represents best.

# There are some trade offs when using a graph. Adding a person or a friendship is very fast, but printing the whole network takes more time because every connection must be checked. Still, this cost is worth it because it gives a clear and realistic view of how everyone is linked. Overall, graphs make it easy to model complex social systems that grow and change over time.
# """