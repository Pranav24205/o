from tg_bot.sample_config import Config

class Development(Config):

    OWNER_ID =  1511373882 # my telegram ID

    OWNER_USERNAME = "its_pranav_xd"  # my telegram username

    API_KEY = "5014894069:AAEo3NMCEBlvFUYe7sPIi9La1g0igvbMXn8" # my api key, as provided by the botfather

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:iAzIkTRdVuPocDqhz7m6@containers-us-west-11.railway.app:7176/railway'  # sample db credentials

    MESSAGE_DUMP = '-1001276224293' # some group chat that your bot is a member of

    USE_MESSAGE_DUMP = True

    SUDO_USERS = [163494588, 1311769691]  # List of id's for users which have sudo access to the bot.

    LOAD = []

    NO_LOAD = ['translation']
