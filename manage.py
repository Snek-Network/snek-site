#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import typing as t

import django
from django.contrib.auth import get_user_model
from django.core.management import call_command, execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snek_site.settings')
os.environ.setdefault('SUPERUSER_USERNAME', 'admin')
os.environ.setdefault('SUPERUSER_PASSWORD', 'password')
os.environ.setdefault('DEFAULT_SNEK_API_TOKEN', '704Z1PjVo0SbjDCbtkL5J4GYQMqiUm9vJrjCXY8OB18')


class SiteManager:
    """Manages the preparation of serving of the site and API."""

    def __init__(self, args: t.List[str]) -> None:
        self.debug = '--debug' in args

        if self.debug:
            os.environ.setdefault('DEBUG', 'true')
            print('Starting in debug mode.')

    @staticmethod
    def create_superuser() -> None:
        """Create a default Django super user in development environments."""
        print('Creating a superuser.')

        username = os.environ['SUPERUSER_USERNAME']
        password = os.environ['SUPERUSER_PASSWORD']
        api_token = os.environ['DEFAULT_SNEK_API_TOKEN']
        user = get_user_model()

        if user.objects.filter(username=username).exists():
            user = user.objects.get(username=username)
        else:
            user = user.objects.create_superuser(username, '', password)

        from rest_framework.authtoken.models import Token
        Token.objects.update_or_create(user=user, key=api_token)

    def prepare_server(self) -> None:
        """Perform preparation tasks before running the server."""
        django.setup()

        print('Appling migrations..')
        call_command('migrate')
        print('Collecting static files..')
        call_command('collectstatic', interactive=False, clear=True)

        if self.debug:
            self.create_superuser()

    def run_server(self) -> None:
        """Prepare and run the server."""

        # Prevent preparing twice when in development mode due to reloader
        if not self.debug or os.environ.get('RUN_MAIN') == 'true':
            self.prepare_server()

        print('Starting server..')

        if self.debug:
            # Run in development
            call_command('runserver', '0.0.0.0:8000')
        else:
            import pyuwsgi

            # Run in production
            pyuwsgi.run(['--ini', 'uwsgi.ini'])


def main():
    """Entry point for Django management script."""
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        # Run the custom site manager
        SiteManager(sys.argv).run_server()
    else:
        # Run the standard management commands
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
