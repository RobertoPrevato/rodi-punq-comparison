import rodi
import os


container = rodi.Container()


class ConfigReader:
    def get_config(self):
        pass


class EnvironmentConfigReader(ConfigReader):
    def get_config(self):
        return {
            "logging": {"level": os.environ.get("LOGGING_LEVEL", "debug")},
            "greeting": os.environ.get("GREETING", "Hello world"),
        }


container.add_scoped(ConfigReader, EnvironmentConfigReader)


class Greeter:
    def greet(self):
        pass


class ConsoleGreeter(Greeter):
    def __init__(self, config_reader: ConfigReader):
        self.config = config_reader.get_config()

    def greet(self):
        print(self.config["greeting"])


container.add_transient(Greeter, ConsoleGreeter)

provider = container.build_provider()


def rodi_main():
    greeter = provider.get(Greeter)
    assert isinstance(greeter, ConsoleGreeter)


if __name__ == "__main__":
    rodi_main()
