import configparser
from mybot.util.logger import log

config = configparser.RawConfigParser()
config_file = config.read('setting.ini')
if not config_file:
    with open('setting.ini', 'w') as setting:
        if not config.has_section('credentials'):
            config.add_section('credentials')
            config.set('credentials', 'token', '')

        if not config.has_section('configs'):
            config.add_section('configs')
            config.set('configs', 'foo', 'bar')
        config.write(setting)
        setting.close()

TOKEN = config.get('credentials', 'token')
if TOKEN == '':
    log.error("ERROR :: Input your bot's TOKEN in setting.ini")
