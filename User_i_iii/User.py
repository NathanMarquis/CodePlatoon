class User():
    all_user_posts = [] #To store posts from all users

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.user_posts = []

    def __str__(self):
        return f'>>Username: {self.username} /n>>Email: {self.email} /n>>Posts: {self.user_posts}.'

    def create_post(self, title, post):
        User.all_user_posts.append({'Username': self.username, 'Title': title, 'Post': post})
        self.user_posts.append({'Title': title, 'Post': post})

    def delete_post(self):
        for idx in reversed(range(len(User.all_user_posts))): #To remove post from class variable all_user_posts
            if User.all_user_posts[idx]['Username'] == self.username:
                print(f'Deleting last post...')
                # print(User.all_user_posts[idx])
                del User.all_user_posts[idx]
                break 

        del self.user_posts[-1] #To remove post from instance variable user_posts    

# Jeff = User('jDoggg', 'jDiggityDoggg@fmail.com')
# Bethany = User('PeacefulPenguin', 'happypengu@coldmail.com')

# Jeff.create_post('New pug', 'Love it even though its face looks like it got run over!')
# Jeff.create_post('Hate pug', 'Its always making gross sounds, returning the thing.')
# Bethany.create_post('Pedi day', 'About time huh?')

# print(f'pre {User.all_user_posts}')
# print(f'preindividual {Jeff.user_posts}')

# Jeff.delete_post()


# print(f'postindividual {Jeff.user_posts}')
# print(f'post {User.all_user_posts}')

# print(Jeff)
# print(Bethany)