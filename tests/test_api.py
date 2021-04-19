from faker import Faker

from hue import Bridge, Light

fake = Faker()


def test_bridge_init():
    ip = fake.ipv4_private()
    user = fake.uuid4()
    bridge = Bridge(ip=ip, user=user)
    assert bridge


def test_light_init():
    ip = fake.ipv4_private()
    user = fake.uuid4()
    num = fake.random_int()
    light = Light(num, ip=ip, user=user)
    assert light
