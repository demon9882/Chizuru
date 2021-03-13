class Config(object):
    LOGGER = True
    TOKEN = "1658765294:AAFaCpdkFxzCmDwBgbJmsDSDxRcigTBN1mA"
    DB_URI = "postgres://pbhnwssiubuske:064155610519ea8957d1ad156cdb12d83206c0315e0500c7f3a61ca33344d9d6@ec2-52-6-178-202.compute-1.amazonaws.com:5432/d860sv8343r6iv"
    OWNER_ID = 680241924


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
