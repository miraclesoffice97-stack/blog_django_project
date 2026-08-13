#!/usr/bin/env bash
#!/usr/bin/env bash
#!/usr/bin/env bash
#!/usr/bin/env bash
#!/usr/bin/env bash
# Render runs this file automatically before starting your app.
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
