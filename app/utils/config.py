import configparser

class Config:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get(self, section, option, default=None):
        # Get configuration value
        try:
            value = self.config.get(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError):
            value = default
        return value

    def set(self, section, option, value):
        # Set configuration value
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, str(value))

    def save(self, config_file):
        # Save configuration to file
        with open(config_file, 'w') as f:
            self.config.write(f)