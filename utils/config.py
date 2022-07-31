import configparser
import os


class Config:
    @staticmethod
    def create_config(path):
        if not os.path.exists(path):
            config = configparser.ConfigParser()
            config.add_section("Settings")

            config.set("Settings", "autorun", "False")
            config.set("Settings", "version", "v1.5")

            with open(path, "w") as file:
                config.write(file)
        else:
            return print("The file exists")

    @staticmethod
    def get_config(path):
        if not os.path.exists(path):
            Config.create_config(path)

        config = configparser.ConfigParser()
        config.read(path)
        return config

    @staticmethod
    def get_setting(path, section, setting):
        config = Config.get_config(path)
        value = config.get(section, setting)
        return value

    @staticmethod
    def update_setting(path, section, setting, value):
        config = Config.get_config(path)
        config.set(section, setting, value)
        with open(path, "w") as file:
            config.write(file)

    @staticmethod
    def delete_setting(path, section, setting):
        config = Config.get_config(path)
        config.remove_option(section, setting)
        with open(path, "w") as file:
            config.write(file)
