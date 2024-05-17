echo "Building the project..."
pip install -r requirements.txt

echo "make migration..."
python3.11 manage.py makemigrations --noinput
python3.11 manage.py migrate --noinput

echo "collect static files..."
python3.11 manage.py collectstatic --noinput --clear