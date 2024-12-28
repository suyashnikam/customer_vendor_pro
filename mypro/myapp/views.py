from django.shortcuts import render,redirect,HttpResponse
from .models import Contact, NewUser,Customer
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from pyexpat.errors import messages
from django.contrib import messages
from django.core.paginator import Paginator
from .helpers import send_forget_password_mail
from .forms import CustomerRegistration
from django.contrib.auth.forms import PasswordChangeForm
import uuid
# Create your views here.

# To Display home page 
def home(request):
    user = request.user
    print('user:',user)
    return render(request,"myapp/index.html",{'user':user})

def contact(request):
    if request.method == "POST":
        Name = request.POST['Name']
        PhoneNumber = request.POST['PhoneNumber']
        FromEmailAddress = request.POST['FromEmailAddress']
        Comments = request.POST['Comments']
        if len(PhoneNumber)>10:
                messages.error(request, "Mobile Number must be of 10 digits!")
                return redirect('contact')

        if len(PhoneNumber)<10:
                messages.error(request, "Mobile Number must be of 10 digits!")
                return redirect('contact')
        contact = Contact(Name=Name, PhoneNumber=PhoneNumber, FromEmailAddress=FromEmailAddress,Comments=Comments)
        contact.save()
        messages.success(request,"Thank You!, Our executive will contact you soon!")
        return redirect('home')
    else:
        return render(request,'myapp/contact.html',{})


# To display about-page of organiszation
def aboutUs(request):
    return render(request,"myapp/aboutus.html")

# To register a New Vendor 
def register(request):
    if request.method == "POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            mobile = request.POST['mobile']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            if NewUser.objects.filter(username=username):
                messages.error(request, "Username already exist! Please try some other username.")
                return redirect('register')
       
            if NewUser.objects.filter(email=email).exists():
                messages.error(request, "Email Already Registered!!")
                return redirect('register')
       
            if NewUser.objects.filter(mobile=mobile).exists():
                messages.error(request, "Mobile no. is alredy linked with existed vendor!!")
                return redirect('register')
       
            if len(mobile)>10:
                messages.error(request, "Mobile Number must be of 10 digits!")
                return redirect('register')

            if len(mobile)<10:
                messages.error(request, "Mobile Number must be of 10 digits!")
                return redirect('register')
       
       
            if len(username)>20:
                messages.error(request, "Username must be under 20 charcters!!")
                return redirect('register')
       
            if pass1 != pass2:
                messages.error(request, "Passwords didn't matched!!")
                return redirect('register')

            myuser = NewUser.objects.create_user(username,email,pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.mobile = mobile
            myuser.save()
            messages.success(request,"Your Account has been successfully created")
            return redirect('register')
    else:
        use = NewUser.objects.all()
    return render(request,"myapp/register.html",{'users':use})

# To display existed vendor list
def showvendors(request):
    
    # Pagination setup thing
    p = Paginator(NewUser.objects.filter(is_superuser=False),1)
    page = request.GET.get('page')
    vend = p.get_page(page)
    nums = "a" *vend.paginator.num_pages
    return render(request,"myapp/showvendors.html",{'vend':vend,'nums':nums})

# To login into the vendors account 
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"myapp/index.html",{'fname':fname})
        else:
            messages.error(request,"Bad Credentials!")
            return redirect('home')
    return render(request,"myapp/signin.html")

# To signing out the Current Vendor
def signout(request):
    logout(request)
    messages.success(request," Logged Out Successfully!")
    return redirect('home')

# Functionality to reset password with mail service 
def ForgetPassword(request):
    try:
        if request.method == 'POST':
            print("entering into forget pass")
            username = request.POST.get('username')
           
            if not NewUser.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/forget-password/')
           
            user_obj = NewUser.objects.get(username = username)
            print(user_obj.email)
            token = str(uuid.uuid4())
            print("creating token:",token)
            profile_obj= NewUser.objects.get(username = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email has been sent successfully, Please check your inbox or spam!')
            return redirect('/forget-password/')
    except Exception as e:
        print(e)
    return render(request , 'myapp/forget-password.html')


# To search vendor by username
def searchvendor(request):
    if request.method == "POST":
        search = request.POST['search']
        vendor=NewUser.objects.filter(username__contains=search,is_superuser=False)
        return render(request,"myapp/searchvendor.html",{'search':search,'vendors':vendor})
    else:
        return render(request,"myapp/searchvendor.html")


# To save New customer 
def saveCustomer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        mobile = request.POST.get('mobile')
        user = request.user
        print("name:",name)
        print("mobile:",mobile)
        print("user:",user)
        ur = Customer(name=name,lname=lname,mobile=mobile,user=user)

        if Customer.objects.filter(name=name,lname=lname).exists():
            messages.error(request, "Customer with same Name Already Registered!!")
            return redirect('add_show')

        if Customer.objects.filter(mobile=mobile).exists():
            messages.error(request, "Mobile No. Already Registered!!")
            return redirect('add_show')
        ur.save()
        return render(request, 'myapp/congrats.html')

    else:
        fm = CustomerRegistration()
    ur = request.user  
    cus = Customer.objects.filter(user=ur.id)
    return render(request, 'myapp/addandshow.html', {'form':fm,'custom':cus})


# To show customers data into list view 
def showcustomers(request):
    fm = CustomerRegistration()
    ur = request.user
    cus = Customer.objects.filter(user=ur.id)

    # Set up Pagination
    ur = request.user
    p = Paginator(Customer.objects.filter(user=ur.id),1)
    page = request.GET.get('page')
    cust = p.get_page(page)
    nums = "a" *cust.paginator.num_pages
    return render(request, 'myapp/showcustomers.html', {'form':fm,
    'custom':cus,
    'cust':cust,'nums':nums})



# Function to search a particular customer    
def searchcustomer(request):
    if request.method == "POST":
        ur = request.user
        searched = request.POST['searched']
        customer=Customer.objects.filter(name__contains=searched,user=ur.id)
        return render(request,"myapp/searchcustomer.html",{'searched':searched,'customer':customer})
    else:
        return render(request,"myapp/searchcustomer.html")


# To show details of customer 
def customerdetails(request,id):
    pi =Customer.objects.get(pk=id)
    fm =CustomerRegistration(instance=pi)
    ur = request.user
    cus = Customer.objects.filter(user=ur.id)
    customer = Customer.objects.get(id=id)
    return render(request,'myapp/customerdetails.html',{'form':fm,'custom':cus,'customer':customer})


# To finally update the customer 
def FinalUpdateCustomer(request, id):
    if request.method == "POST":
        mobile = request.POST['mobile']
        lname = request.POST['lname']
        member = Customer.objects.get(id=id)

        # if Customer.objects.filter(mobile=mobile).exists():
        #     messages.error(request, "Mobile no. is alredy linked with existed Customer!!")
        #     return redirect('showcustomers')
      
        member.lname = lname
        member.mobile = mobile
        member.save()
        messages.success(request,"Successully Updated!")
        return render(request, 'myapp/customerupdated.html')

    else:
        pi =Customer.objects.get(pk=id)
    fm =CustomerRegistration(instance=pi)
    ur = request.user
    cus = Customer.objects.filter(user=ur.id)
    customer = Customer.objects.get(id=id)
    return render(request,'myapp/updatecustomer.html',{'form':fm,'custom':cus,'customer':customer})


# To take user confirmation from customer to delete customer data 
def askdelete(request,id):
    cus = Customer.objects.get(id=id)
    return render(request,"myapp/suredelete.html",{'cus':cus})

# To final delete customer 
def delete_customer(request, id):
    if request.method == 'POST':
        pi = Customer.objects.get(pk=id)
        pi.delete()
        messages.success(request,"Successfully Deleted!")
        return redirect('showcustomers')


# Function to update user's password with old password 
def user_change_pass(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            return render(request,"myapp/passchanged.html")
    else:
        fm = PasswordChangeForm(user=request.user)
    user = fm.user
    return render(request,"myapp/changepass.html",{'form':fm,'user':user})

# Function to show vendor details 
def vendordetails(request,id):
    use = NewUser.objects.filter(is_superuser=False)
    member = NewUser.objects.get(id=id)
    return render(request,'myapp/vendordetails.html',{'users':use,'member':member})


# function to finally update vendor 
def FinalUpdateVendor(request,id):
    if request.method == "POST":
        print("entering into finalUpdateVendor function ")
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        member = NewUser.objects.get(id=id)
        print(mobile)
        print(lname)
        print(fname)
        print(email)
       
        if len(mobile)<10:
                messages.error(request, "Mobile Number must be of 10 digits!")
                return redirect('showvendors')
       
        if len(mobile)>10:
                messages.error(request, "Mobile Number must be of 10 digits!")
                return redirect('showvendors')
       
        # if NewUser.objects.filter(mobile=mobile).exists():
        #     messages.error(request, " Mobile no. is alredy linked with existed vendor!")
        #     return redirect('showvendors')

        member.first_name = fname
        member.last_name = lname
        member.email = email
        member.mobile = mobile
        member.save()
        return render(request, 'myapp/vendorupdated.html')

    else:
        print("Entering into else part of finalUpdatevendor function!")
    use = NewUser.objects.filter(is_superuser=False)
    member = NewUser.objects.get(id=id)
    return render(request,'myapp/updatevendor.html',{'users':use,'member':member})

# function to take user confirmation from vendor 
def askdeletevendor(request,id):
    cus = NewUser.objects.get(id=id)
    return render(request,"myapp/suredeletevendor.html",{'cus':cus})

# function to delete particular vendor 
def delete_vendor(request, id):
    if request.method == 'POST':
        pi = NewUser.objects.get(pk=id)
        pi.delete()
        messages.success(request,"Your Account has been Deleted!!")
        return redirect('register')

# Function to final reset password with mail integration 
def ChangePassword(request , token):
    context = {}
    print(token)
    try:
        profile_obj = NewUser.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.id}

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')
           
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change-password/{token}/')
               
            if  new_password != confirm_password:
                messages.success(request, 'both password should  be match.')
                return redirect(f'/change-password/{token}/')
                         
            user_obj = NewUser.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            messages.success(request, 'Password have been reset successfully!')
            return redirect('signin')
    except Exception as e:
        print(e)
    return render(request , 'myapp/change-password.html' , context)