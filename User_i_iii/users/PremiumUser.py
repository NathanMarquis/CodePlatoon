from users.User import User

class PremiumUser(User):
    premium = True

    def __init__(self, username, email):
        super().__init__(username, email)

    def __str__(self):
        return f'>>Username: {self.username} /n>>Email: {self.email} /n>>Posts: {self.user_posts}.'