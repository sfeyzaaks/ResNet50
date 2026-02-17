
class User:
    active_users = 0
    def __init__(self,username,name,surname,age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        User.active_users +=1
    def username(self):
        return f"{self.username}"
    def logout(self):
        User.active_users -=1
        return f"{self.username} programdan çıkış yaptı."
print(f"Aktif kullanıcı sayısı: {User.active_users}")
user1 = User("levenert","levent","ertunalılar",37)
user2 = User("feyzaaks","feyza","aksoy",18)
print(user2.logout())
print(f"Aktif kullanıcı sayısı: {User.active_users}")

