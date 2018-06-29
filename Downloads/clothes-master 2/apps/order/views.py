from django.shortcuts import render, HttpResponse, redirect
# stripe.api_key = "sk_test_eo8n9U6JGbt0Sxmm5PQYdJtu"


# token = request.form['stripeToken'] # Using Flask

# charge = stripe.Charge.create(
#     amount=999,
#     currency='usd',
#     description='Example charge',
#     source=token,
# )

def index(request):
    return render(request, 'order/main_page.html')

def order(request):
    return render(request, 'order/order.html')

# def swag_api(request):
#     users = User.objects.filter(first_name__startswith=request.POST['starts_with'])
#     return render(request, 'user_login/all.html', { users: users })