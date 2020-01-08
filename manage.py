<<<<<<< HEAD
#!/usr/bin/env python3.7
=======
#!/usr/bin/env python
>>>>>>> ec5b10d872aeee42525a5b72c246035f1a0cd100
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ttt.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ttthuoc.settings')
>>>>>>> ec5b10d872aeee42525a5b72c246035f1a0cd100
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
<<<<<<< HEAD
        ) #from exc
=======
        ) from exc
>>>>>>> ec5b10d872aeee42525a5b72c246035f1a0cd100
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
