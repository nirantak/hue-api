from faker import Faker

from hue import Light


class TestLight:
    fake = Faker()
    ip = fake.ipv4_private()
    user = fake.uuid4()
    num = fake.random_int()

    def test_light_init(self):
        light = Light(self.num, ip=self.ip, user=self.user)
        assert light
