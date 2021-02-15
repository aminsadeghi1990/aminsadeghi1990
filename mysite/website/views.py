from django.shortcuts import render
from django.core.mail import send_mail
def home(request):
    return render(request, 'home.html',{})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        send_mail(
            message_name,
            message,
            message_email,
            ['drghfatehi@gmail.com'],
            )          

        return render(request, 'contact.html',{})


    def about(request):
        return render(request, 'about.html',{})


    def service(request):
        return render(request, 'service.html',{})

    def article(request):
        return render(request, 'article.html',{})
    
def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_scheldule = request.POST['your-scheldule']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']
        appointment = 'Name: " + your_name" +  "Phone:" + your_phone + " Email: " + "your_email" 
        send_mail(
            'Appointment Request',#sunject
            appointment,#message
            your_email,# from email
            ['drghfatehi@gmail.com'],# to email
            )          

        return render(request, 'appointment.html',{
            'your-name': your-name,   
            'your-phone': your-phone,   
            'your-email': your-email,    
            'your-address': your-address,
            'your-scheldule': your-scheldule,
            'your-time': your-time,
            'your-message': your-message,
})
    else:
        return render(request, 'home.html',{})
