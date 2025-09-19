from user import User

user1 = User("Nasrudeen","123abc")
user2 = User("Yaseen","123abc")
user3 = User("Vishwa","123abc")

user1.register()


u1 = User("Alice", "1234")
u2 = User("Bob", "abcd")

u1.register()   # Registering...Alice
u2.login()      # Logging...abcd

print(User.users)  # 2 (because two User objects were created)
