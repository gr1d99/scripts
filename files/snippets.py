import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read('res/secret.ini')
print Config.sections()