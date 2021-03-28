class Config(object):
    LOGGER = True
    TOKEN = "1658765294:AAFaCpdkFxzCmDwBgbJmsDSDxRcigTBN1mA"
    DB_URI = "postgres://xwlklsxachwchj:6622a706fbf5e4dabe4e8469f4072eb6bed8a5bd992272b4a174df5319d980a6@ec2-23-21-229-200.compute-1.amazonaws.com:5432/d6ej9i89a02hhs"
    OWNER_ID = 680241924


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
