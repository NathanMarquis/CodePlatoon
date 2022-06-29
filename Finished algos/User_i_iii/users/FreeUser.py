from users.User import User

class FreeUser(User):
    premium = False

    def __init__(self, username, email):
        super().__init__(username, email)
        self.post_count = 0

    def __str__(self):
        return f'>>Username: {self.username} /n>>Email: {self.email} /n>>Posts: {self.user_posts}.'