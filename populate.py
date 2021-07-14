import argparse

from faker import Faker
import django
django.setup()
fake = Faker()


def create_post(n, m):
    from api.models import User, Post

    for i in range(n):

        user = User.objects.create(
            username=fake.user_name(),
        )
        user.set_password('password')
        user.save()
        for i in range(m):

            post = Post.objects.create(
                user_id=user,
                post_id=fake.pyint(),
                likes=fake.pyint())


if __name__ == '__main__':
    django.setup()
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int)
    parser.add_argument('-m', type=int)
    args = parser.parse_args()
    print("populating")
    print("{} this is my arg".format(args.n))
    create_post(args.n, args.m)
    print('done')
