#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # GETTING-STARTED: change 'OutSourcer' to your project name:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OutSourcer.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
