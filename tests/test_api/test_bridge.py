from faker import Faker

from hue import Bridge


class TestBridge:
    fake = Faker()
    ip = fake.ipv4_private()
    user = fake.uuid4()

    def test_bridge_init(self):
        bridge = Bridge(ip=self.ip, user=self.user)
        assert bridge
