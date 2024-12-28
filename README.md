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

**Step 6: Change the working directory**

cd mypro

**Step 7:Apply Django command for makemigration**

python manage.py makemigrations myapp

**Step 8: Apply Django commad for migrate**

python manage.py migrate

**Step 9: Create superuser for your Application**

python manage.py createsuperuser

**Step 10: Run the server**

python manage.py runserver

**Note**: Here in this project we have  functionality of forget password via email. For sending the reset password link along with generated token. We need one google mail account to trigger the mails from. That mail account may need  kind of developer permission to trigger the mail. So in our settings.py file there are three configurable fields like EMAIL_HOST_USER = '', EMAIL_HOST_PASSWORD = '', DEFAULT_HOST = ''. This host configuration you needs to be done under google smtp settings it should provide you the host user, host password and hostname. Those details you will need to provide here instead of empty strings. Once this fields contains correct string values; your forget password functionality should work as expected.



Once Webapp is running, you can able to register Vendors with signup option. After Registration you can login to system with the same credentials you provided while creating vendor. Now once you looged in to the system you can now create customer and get list of customer who created under you!!

You can also login with your superuser creds, So that you can get the list of all registered vendors.


And All Set!!!!!

