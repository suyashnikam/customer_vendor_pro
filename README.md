# customer_vendor_pro
customer and vendor project

**Step 1: Make a directory locally** 

**Step 2: Open VS code for created directory** 

**Step 3: Once open in VS code, Navigate to termial and hit git clone command to clone the project using repo_url along with "." at the end**

git clone repo_url .

**Step 4: Create and activate venv**

python -m venv venv  

source venv/bin/activate

**Step 5: Run the requirement.txt**

pip install -r requirements.txt

**Step 6: Apply Django command for makemigration**

python manage.py makemigrations myapp

**Step 7: Apply Django commad for migrate**

python manage.py migrate

**Step 8: Create superuser for your Application**

python manage.py createsuperuser

**Step 9: Run the server**

python manage.py runserver



Once Webapp is running, you can able to register Vendors with signup option. After Registration you can login to system with the same credentials you provided while creating vendor. Now once you looged in to the system you can now create customer and get list of customer who created under you!!

You can also login with your superuser creds, So that you can get the list of all registered vendors.


And All Set!!!!!

