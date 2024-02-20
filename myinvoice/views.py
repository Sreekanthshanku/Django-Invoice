from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def gen_pdf(request):
    if request.method == 'POST':
        SamsungTV = request.POST['Samsung TV']
        JBLSpeaker = request.POST['JBL Speaker']
        MacbookAir = request.POST['Macbook Air']
        Iphone11PRO = request.POST['Iphone 11 PRO']
        dt=request.POST['dt']
        if int(SamsungTV)<0 or int(JBLSpeaker)<0 or int(MacbookAir)<0 or int(Iphone11PRO)<0:
            return HttpResponse("<h1> Quantity cannot be negetive </h1>")
        
        SamsungTV_rt = 10000
        JBLSpeaker_rt = 15000
        MacbookAir_rt = 70000
        Iphone11PRO_rt = 50000
        total = int(SamsungTV)*SamsungTV_rt +int(JBLSpeaker)*JBLSpeaker_rt +int(MacbookAir)*MacbookAir_rt +int(Iphone11PRO)*Iphone11PRO_rt 
        print("Total amout is :",total)
        return render(request,'pdf.html',{'SamsungTV':SamsungTV, 'JBLSpeaker':JBLSpeaker, 'MacbookAir':MacbookAir, 'Iphone11PRO':Iphone11PRO, 'dt':dt, 'total':total})
    return render(request,'index.html')