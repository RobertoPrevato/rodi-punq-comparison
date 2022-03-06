import di
from di.container import bind_by_type
import os


container = di.Container()


class ConfigReader:
    def get_config(self):
        pass


class EnvironmentConfigReader(ConfigReader):
    def get_config(self):
        return {
            "logging": {"level": os.environ.get("LOGGING_LEVEL", "debug")},
            "greeting": os.environ.get("GREETING", "Hello world"),
        }


container.bind(bind_by_type(di.Dependant(EnvironmentConfigReader), ConfigReader))


class Greeter:
    def greet(self):
        pass


class ConsoleGreeter(Greeter):
    def __init__(self, config_reader: ConfigReader):
        self.config = config_reader.get_config()

    def greet(self):
        print(self.config["greeting"])


container.bind(bind_by_type(di.Dependant(ConsoleGreeter), Greeter))
provider = container.solve(di.Dependant(Greeter), scopes=(None,))
executor = di.SyncExecutor()

def di_main():
    with container.enter_scope(None):
        greeter = container.execute_sync(provider, executor=executor)
    assert isinstance(greeter, ConsoleGreeter)


if __name__ == "__main__":
    di_main()
