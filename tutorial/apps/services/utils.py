import secrets
from .models import Profile


class GetCurrentLanguage(object):
    @staticmethod
    def get_language(header=None, user=None):
        if user.is_anonymous:
            if 'Accept-Language' in header:
                lang = header['Accept-Language'][:2]
            else:
                lang = 'en'
            return lang
        else:
            try:
                lang = Profile.objects.get(user=user).language[:2]
            except Profile.DoesNotExist:
                if 'Accept-Language' in header:
                    lang = header['Accept-Language'][:2]
                else:
                    lang = 'en'
            return lang


def get_random_string():
    length = 20
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    allowed_number = '0123456789'
    """
    Return a securely generated random string.
    """
    return ''.join(secrets.choice(allowed_chars) for i in range(length))


def greeting():
    print("Assalomu aleykum!")


x = 1
while x < 6:
    greeting()
    if x == 3:
        break
    x += 1
