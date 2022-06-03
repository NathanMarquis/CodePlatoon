from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser
from users.User import User



Jeff = FreeUser('jDoggg', 'jDiggityDoggg@fmail.com')
Bethany = PremiumUser('PeacefulPenguin', 'happypengu@coldmail.com')

Jeff.create_post('New pug', 'Love it even though its face looks like it got run over!')
Jeff.create_post('Hate pug', 'Its always making gross sounds, returning the thing.')
Jeff.create_post('Another dog?', 'Considering if I should give up or not...')
Bethany.create_post('Pedi day', 'About time huh?')

print(f'pre {User.all_user_posts}')
print(f'preindividual {Jeff.user_posts}')

Jeff.delete_post()


print(f'postindividual {Jeff.user_posts}')
print(f'post {User.all_user_posts}')

# print(Jeff)
# print(Bethany)