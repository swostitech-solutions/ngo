import razorpay
from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import contactform,userregistrationform,payform
from .models import Contact_model,donation_payment_model
# Create your views here.

from app1.models import Post, Category

#home view
def home(request):
    #load all the post from db(10)
    posts=Post.objects.all()[:11]
    # load all category
    cats = Category.objects.all()
    data={
        'posts': posts,
        'cats': cats,
    }
    return render(request,'app1/home_page.html',data)



def profile(request):
    if request.user.is_authenticated:
        user=request.user
        username=user.username
        full_name=user.get_full_name()
        email=user.email
        return render(request, 'app1/profile.html',{'username':username,'full_name':full_name,'email':email})
    else:
        return HttpResponseRedirect('/login/')



def About(request):
    return render(request,'app1/about.html')

def contact(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            cfm=contactform(request.POST)
            if cfm.is_valid():
                nm=cfm.cleaned_data['name']
                em=cfm.cleaned_data['email']
                ads=cfm.cleaned_data['address']
                msg=cfm.cleaned_data['message']
                data=Contact_model(name=nm,email=em,address=ads,message=msg)
                data.save()
                messages.success(request, "Your Resposns recorded successfully!!")
                return redirect('home')
        else:
            cfm=contactform()
            return render(request, 'app1/contact.html',{'cfm':cfm})
    else:
        return redirect('login')



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')



#user login
def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully!!')
                return HttpResponseRedirect('/home/')
    else:
        fm = AuthenticationForm()
    return render(request, 'app1/login.html', {'form': fm})

def user_signup(request):
    if request.method == "POST":
        form = userregistrationform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successfully!!")
            return HttpResponseRedirect('/login/')

    else:
        fm=userregistrationform()
        return render(request,'app1/signup.html',{'form':fm})




# def payment_view(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             name=request.POST.get('name')
#             amount=int(request.POST.get('amount')) * 100
#             client= razorpay.Client(auth=('rzp_test_gqnLGb3poHpdSz','EHdxpKnZ3H13IB2eWvuhJ6jB'))
#
#             # create order
#             response_payment = client.order.create(dict(amount=amount, currency='INR'))
#             print(response_payment)
#
#             order_id = response_payment['id']
#             order_status = response_payment['status']
#             fm=payform(request.POST or None)
#             return render(request,'app1/payment.html',{'form':fm})
#         else:
#             fm=payform()
#             return render(request, 'app1/payment.html',{'form':fm})
#     else:
#         return redirect('login')

#payment gatway part

def payment_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('name')
            amount= int(request.POST.get('amount')) * 100
            print(amount,type(amount))
            # create razorpay client
            client = razorpay.Client(auth=('rzp_test_gqnLGb3poHpdSz', 'EHdxpKnZ3H13IB2eWvuhJ6jB'))

            # create order
            response_payment = client.order.create(dict(amount=amount, currency='INR'))

            # print(response_payment)

            order_id=response_payment['id']
            order_status = response_payment['status']

            if order_status == 'created':
                donation_payment=donation_payment_model(
                    name=name,
                    amount=amount,
                    order_id=order_id
                )
                donation_payment.save()
                response_payment['name']= name

                fm = payform()
                return render(request, 'app1/payment.html', {'form': fm,'payment':response_payment})
        else:
            fm = payform()
            return render(request, 'app1/payment.html', {'form': fm})
    else:
         return redirect('login')


def payment_status_view(request):
    response= request.POST
    print(response)

    params_dict= {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }
    client=razorpay.Client(auth=('rzp_test_gqnLGb3poHpdSz','EHdxpKnZ3H13IB2eWvuhJ6jB'))
    try:
        status=client.utility.verify_payment_signature(params_dict)
        details=donation_payment_model.objects.get(order_id= response['razorpay_order_id'])
        details.razorpay_payment_id = response['razorpay_payment_id']
        details.paid = True
        details.save()
        return render(request,'app1/payment_status.html', {'status':True})
    except:
        return render(request, 'app1/payment_status.html',{'status': False})












#post view
def post_view(request):
    post=Post.objects.all()[:11]
    print(post)
    return render(request,'app1/posts.html',{'post': post})

#category wise post view

def cat_post_view(request,url):
    post=Post.objects.filter(url=url)[:11]
    return render(request, 'app1/cat_post.html', {'post': post})















