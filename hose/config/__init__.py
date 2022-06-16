""" 
The argument that is passed to `python3.9 run.py --env=ARGUMENT`
is parsed here and that how script defines which config to use,
because we may have several, one for each environment
"""

import argparse
import os
import yaml

parser = argparse.ArgumentParser()
parser.add_argument('--env', help='set environment variable')
args = parser.parse_args()

try: 
    ENV = args.env.lower()
    if ENV not in {'test', 'dev'}:
        raise Exception("Acceptable --env values are: test, dev")
except AttributeError:
    raise AttributeError("Script should be ran with '--env=ENV_VARIABLE' argument")

config_dir = os.path.dirname(__file__)

# Establish test environment
if ENV == 'test': 
    # implement config loading...
    application_config_file = os.path.join(config_dir, os.path.join('test_config', 'config.yaml'))

    with open(application_config_file, 'r', encoding='utf-8') as stream:
        ETL_CONFIG = yaml.safe_load(stream)

    # TODO: implement table loading... 
    # same as above

    project_abs_path = os.path.dirname(os.path.dirname(__file__))

# Establish dev environment
elif ENV == 'dev': 
    # implement config loading...
    application_config_file = os.path.join(config_dir, os.path.join('dev_config', 'config.yaml'))

    with open(application_config_file, 'r', encoding='utf-8') as stream:
        ETL_CONFIG = yaml.safe_load(stream)

    # TODO: implement table loading... 
    # same as above

    project_abs_path = os.path.dirname(os.path.dirname(__file__))

else: 
    raise Exception("System Environment Variable 'ENV' has unacceptable value."
                    "Acceptable 'ENV' values are: 'test', 'dev'")

# TODO: add in tables here 
__all__ = ['ETL_CONFIG', 'project_abs_path']

if __name__ == '__main__': 
    print(__file__)