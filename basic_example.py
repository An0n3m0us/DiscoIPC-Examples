import time, sys, configparser
from discoIPC import ipc

config = configparser.ConfigParser()
config.read('config.ini')

base_activity = {
    'assets': {
        'large_image': 'example-big',
        'large_text': 'Example big',
        'small_image': 'example-small',
        'small_text': 'Example small',
    },
    'timestamps': {}
}

timeElapsed = int(time.time())

client = ipc.DiscordIPC(config['CLIENT']['client_id'])
client.connect()

print('\nStarting ICP...\n')

def set_activity():
    activity = base_activity
    activity['details'] = 'Example'
    activity['state'] = 'example'
    activity['timestamps']['start'] = timeElapsed
    return activity

try:
    while True:
        print('Sending data ...')
        client.update_activity(set_activity())
        time.sleep(5) # Send data every second seconds

except KeyboardInterrupt:
    print('Disconnecting Discord ICP ...\n')
    client.disconnect()
    sys.exit()
