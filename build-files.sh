echo "Building the project..."
pip3.11 install --disable-pip-version-check --target . --upgrade -r /vercel/path0/requirements.txt


echo "make migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "collect static files..."
python manage.py collectstatic --noinput --clear