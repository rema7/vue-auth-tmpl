import os
from logging.config import dictConfig

from invoke import Collection, task

import settings as app_settings
from db import tasks as db_tasks
from qa import tasks as qa_tasks

LOCAL_SETTINGS = 'settings_local.py'


@task
def init_config(ctx, db_connection, disable_signup=False, silent=False):
    settings_local = '''
LOG_LEVEL = 'DEBUG'
DB_CONNECTION = '{db_connection}'
DISABLE_SIGNUP = {disable_signup}
'''.format(
        db_connection=db_connection,
        disable_signup=disable_signup
    )

    settings_local_path = os.path.join(
        app_settings.PROJECT_ROOT, LOCAL_SETTINGS)
    if os.path.isfile(settings_local_path):
        if silent:
            exit(0)

        print('{} already exists'.format(LOCAL_SETTINGS))
        exit(1)

    with open(settings_local_path, 'w') as settings_file:
        settings_file.write(settings_local)


dictConfig(app_settings.LOGGING)

ns = Collection()
ns.add_collection(Collection.from_module(db_tasks), name='db')
ns.add_collection(Collection.from_module(qa_tasks), name='qa')
ns.add_task(init_config)
