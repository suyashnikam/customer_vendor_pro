# customer_vendor_pro
customer and vendor project

step 1: Create and activate venv
python -m venv venv
source venv/bin/activate

Step2: clone the project usin repo_url
git clone repo_url .

Step 3: Run the requirement.txt
pip install -r requirements.txt

Step4: makemigration
python manage.py makemigrations myapp

Step 5: migrate
python manage.py migrate

Step 6: create superuser
python manage.py createsuperuser

Step 7: Run the server
python manage.py runserver


And All Set!!!!!

