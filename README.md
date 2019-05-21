# DiscoIPC Examples
This repository holds example/template scripts that send Rich Presence to Discord using discoIPC.

Remember to place your client ID in the config file before you try the scripts.

## Tips

### Check if an application is running (Linux only)

```
import subprocess

# If Firefox is running then update activity otherwise exit
if "Firefox" in subprocess.check_output('wmctrl -l', shell=True)[:-1]:
    client.update_activity(set_activity())
else:
    print('\nFirefox is not running\n')
    sys.exit()
```

### Time remaining (Linux only)

```
timeElapsed = int(time.time()) # Time elapsed
timeRemaining = int(subprocess.check_output('date -d +30min +%s', shell=True)[:-1]) # Get a timestamp for (now + 30mins)

activity['timestamps']['start'] = timeElapsed
activity['timestamps']['end'] = timeRemaining
```
