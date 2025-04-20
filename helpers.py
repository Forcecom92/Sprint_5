import random

class GeneratorData:
    def generate_logins(random_int=10):
        base_email = f'Pavel_Gubkin_20_{random_int}@yandex.com'
        username, domain = base_email.split('@')
        prefix = username[:-3]
        suffix = username[-3:]

        logins = []
        for i in range(random_int):
            new_suffix = ''.join(random.choices('0123456789', k=3))
            logins.append(f"{prefix}_{new_suffix}@{domain}")

        return logins[0]

    def generate_password():
        return ''.join(random.choices('0123456789', k=6))





