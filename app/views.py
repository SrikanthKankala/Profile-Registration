
from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from .models import register
from django.contrib.auth.hashers import make_password


def Indexview(request):
    return render(request,'app/Register.html') 

#-----------------------------------------


def insert(request):
    if request.method == 'POST':
        email = request.POST['email']
        Mobile_number = request.POST['Mobile_number']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']

        # Check if email already exists
        if register.objects.filter(email=email).exists():
            message = "User with this email already exists"
            return render(request, 'app/register.html', {'msg1': message})
        #return redirect('loginpage')  # 'loginpage' is the name of your loginpage URL pattern
        
        # Check if mobile number already exists
        elif register.objects.filter(Mobile_number=Mobile_number).exists():
            message = "User with this mobile number already exists"
            return render(request, 'app/register.html', {'msg2': message})
        else:
            if password == confirm_password:
                if len(Mobile_number) == 10:
                    # Create a new user object and save it to the database
                    newuser = register.objects.create(
                        email=email,
                        Mobile_number=Mobile_number,
                        password=password
                    )

                    newuser.password=make_password(newuser.password)
                    newuser.save()
                    message = "User registered successfully"
                    return render(request, 'app/Register.html', {'msg': message})
                   # return redirect('loginpage')  # 'loginpage' is the name of your loginpage URL pattern
                else:
                    message = "Please check your phone number"
                    return render(request, 'app/register.html', {'msg3': message})
            else:
                message = "Confirm password doesn't match with password"
                return render(request, 'app/register.html', {'msg4': message})
    else:
        # Handle GET requests or other cases as needed
        return render(request, 'app/Register.html')
#--------------------------------------------------------------


# def insert(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         Mobile_number = request.POST['Mobile_number']
#         password = request.POST['password']
#         confirm_password = request.POST['confirmpassword']

#         response_data = {}  # Initialize a dictionary to hold response data

#         # Check if email already exists
#         if register.objects.filter(email=email).exists():
#             response_data['success'] = False
#             response_data['errors'] = {'email': 'User with this email already exists'}
#         # Check if mobile number already exists
#         elif register.objects.filter(Mobile_number=Mobile_number).exists():
#             response_data['success'] = False
#             response_data['errors'] = {'Mobile_number': 'User with this mobile number already exists'}
#         else:
#             if password == confirm_password:
#                 if len(Mobile_number) == 10:
#                     # Create a new user object and save it to the database
#                     newuser = register.objects.create(
#                         email=email,
#                         Mobile_number=Mobile_number,
#                         password=password
#                     )

#                     newuser.password = make_password(newuser.password)
#                     newuser.save()
#                     response_data['success'] = True
#                     response_data['redirect_url'] = '/login/'  # Redirect to login page
#                 else:
#                     response_data['success'] = False
#                     response_data['errors'] = {'Mobile_number': 'Please check your phone number'}
#             else:
#                 response_data['success'] = False
#                 response_data['errors'] = {'confirmpassword': 'Confirm password doesn\'t match with password'}

#         return JsonResponse(response_data)  # Return a JSON response
#     else:
#         # Handle GET requests or other cases as needed
#         return render(request, 'app/Register.html')

#----------------------------------------------------------------------------------------------------



def Loginview(request):
    return redirect('login')