import os

import lagom

container = lagom.Container()


class ConfigReader:
    def get_config(self):
        pass


class EnvironmentConfigReader(ConfigReader):
    def get_config(self):
        return {
            "logging": {"level": os.environ.get("LOGGING_LEVEL", "debug")},
            "greeting": os.environ.get("GREETING", "Hello world"),
        }


class Greeter:
    def greet(self):
        pass


class ConsoleGreeter:
    def __init__(self, config_reader: ConfigReader):
        self.config = config_reader.get_config()

    def greet(self):
        print(self.config["greeting"])


container[ConfigReader] = lambda: EnvironmentConfigReader()
container[Greeter] = lambda c: ConsoleGreeter(c[ConfigReader])


def lagom_main():
    greeter = container.resolve(Greeter)
    assert isinstance(greeter, ConsoleGreeter)


if __name__ == "__main__":
    lagom_main()
