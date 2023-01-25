import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration/config.ini")


class Readconfig:
    @staticmethod
    def getapplictionURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getuseremail():
        username = config.get('common info', 'user_email')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'pass')
        return password
