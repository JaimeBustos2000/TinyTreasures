#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import signal
import django


def cleanup_data():
    # Aquí colocas el código que quieres ejecutar cuando el servidor se detenga.
    ruta_relativa = os.path.join('TinyTreasures', 'sessions.json')
    with open(ruta_relativa, 'w') as file:
        file.write('')

def signal_handler(sig, frame):
    print("Interrupción recibida, limpiando datos...")
    cleanup_data()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TinyTreasures.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    

if __name__ == '__main__':
    main()
