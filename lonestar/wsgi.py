"""
WSGI config for lonestar project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lonestar.settings")

application = get_wsgi_application()

# --- Auto-create admin on Render ---
# (This only runs when deployed to Render, not locally)
if os.environ.get("RENDER"):
    try:
        from django.contrib.auth import get_user_model
        from django.db.utils import OperationalError
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                "admin", "admin@example.com", "admin123"
            )
            print("✅ Superuser created automatically on Render!")
        else:
            print("ℹ️ Superuser already exists.")
    except OperationalError:
        pass
