echo "Building the project..."
pip install --upgrade pip
pip install --target . --upgrade -r requirements.txt

echo "make migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "collect static files..."
python manage.py collectstatic --noinput --clear