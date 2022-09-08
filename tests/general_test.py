import os
import hello_world


class TestEnvs:
    def test_dev_env(self):
        print("fghjk")
        os.environ["ENV"] = "dev"
        res = hello_world.hello_hello()

        assert res == "dev", f"Error: Expected 'dev' but got {res}."

    def test_stag_env(self):
        os.environ["ENV"] = "stag"
        res = hello_world.hello_hello()

        assert res == "stag", f"Error: Expected 'stag' but got {res}."

    def test_prod_env(self):
        os.environ["ENV"] = "prod"
        res = hello_world.hello_hello()

        assert res == "prod", f"Error: Expected 'prod' but got {res}."

    def test_unc(self):
        print("pirulito dev")
        os.environ["ENV"] = "dev"
        res = hello_world.not_covered_by_unittests()
        assert res == "dev", f"Error: Expected 'dev' but got {res}."

    def test_two(self):
        hello_world.another_one()
