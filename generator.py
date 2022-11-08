from faker import Faker
fake = Faker()
Faker.seed()

n = 100
with open("sample.json", "w") as outfile:
    for a in range(n):
        id = str(a)
        username = fake.simple_profile()["username"]
        email = fake.simple_profile()["mail"]
        password = fake.password(length=12)
        created_on = fake.date_this_month()
        last_login = fake.date_between(created_on)

        dictionary = f'"id": "{id}", "username": "{username}", "email": "{email}", "password": "{password}", "created_on": "{created_on}", "last_login": "{last_login}", "false": "false"'
        
        outfile.write('{"index":{}}\n')

        outfile.write("{"+dictionary+"}\n")
    outfile.close()