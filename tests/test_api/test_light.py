from faker import Faker

from hue import Light


class TestLight:
    fake = Faker()
    ip = fake.ipv4_private()
    user = fake.uuid4()
    num = fake.random_int()

    def test_light_init(self):
        light = Light(self.num, ip=self.ip, user=self.user)
        assert light.id == self.num
        assert light.ip == self.ip
        assert light.user == self.user
        assert light.on is None
        assert light.info == {}
        assert light.state == {}
        assert light.saved_state == {}
        assert str(light) == f"<Light {self.num}>"
        assert repr(light) == f"<Light id={self.num} on={None} ip={self.ip}>"

    def test_light_url(self):
        light = Light(self.num, ip=self.ip, user=self.user)
        assert (
            light.url == f"http://{self.ip}/api/{self.user}/lights/{self.num}"
        )
