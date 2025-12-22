import datetime
from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings
from myapp.forms import notesdata  # apna actual model use karo


# Create your views here.

def admin_login(request):
    if request.method=='POST':
        unm=request.POST["username"]
        pas=request.POST["password"]
        
        if unm=="admin" and pas=="admin@123":
            print("Login Success!")
            return redirect('admin_dashboard')
        else:
            print("Error!Login Faild...")
    return render(request,'admin_login.html')


def admin_dashboard(request):
    total_users = Noteinfo.objects.count()
    total_notes = notesdata.objects.count()
    total_pending = notesdata.objects.filter(status = 'pending').count()
    total_approval = notesdata.objects.filter(status = 'approved').count()
    total_rejected = notesdata.objects.filter(status = 'rejected').count()

    return render(request,'admin_dashboard.html',{'total_users': total_users, 'total_notes': total_notes,'total_pending':total_pending,'total_approval':total_approval,'total_rejected':total_rejected})

def admin_notes_card(request):
    status = request.GET.get('status')

    if status:
        ndata = notesdata.objects.filter(status__iexact=status)
    else:
        ndata = notesdata.objects.all()

    return render(request, 'admin_notes.html', {
        'ndata': ndata,
        'active_status': status
    })

def adminuserdata(request):
    udata=Noteinfo.objects.all()
    return render(request,'admin_userdata.html',{'udata':udata})

def admin_note(request):
    ndata=notesdata.objects.all()
    return render(request,'admin_notes.html',{'ndata':ndata})

def admin_logout(request):
    logout(request)
    return redirect('admin_login')



def admin_user_view(request, uid):
    user = get_object_or_404(Noteinfo, id=uid)
    user_notes = notesdata.objects.filter(user=user)  # user ke sare notes

    return render(request, 'admin_user_view.html', {'user': user,'user_notes': user_notes})


def admin_user_delete(request,uid):
    udata=Noteinfo.objects.get(id=uid)
    udata.delete()
    return redirect('admin_userdata')

def admin_note_approve(request,nid):
    ndata=get_object_or_404(notesdata,id=nid)
    ndata.status='approved'
    ndata.updated_at=datetime.datetime.now()
    ndata.save()
    print("Approved")

# email content
    sub = "Your Note Has Been Approved 🎉"
    msg = f"""
            Hello {ndata.user.name},

            Good news! 🎉

            Your note titled "{ndata.title}" has been approved by the admin.

            You can now view it in your dashboard.

            Thank you for using NotesApp.

            Regards,
            NotesApp Team
            """

    f_email = settings.EMAIL_HOST_USER
    r_email = [ndata.user.email]

    # send email
    send_mail(subject=sub, message=msg, from_email=f_email, recipient_list=r_email)
    print("Approved & Email Sent")

    return redirect('admin_notes_card')


def admin_note_rejected(request,nid):
    ndata=get_object_or_404(notesdata,id=nid)
    ndata.status='rejected'
    ndata.updated_at=datetime.datetime.now()
    ndata.save()
    print("rejected")

# email content
    sub = "Your Note Has Been rejected 🎉"
    msg = f"""
            Hello {ndata.user.name},

            Bad news! 🎉

            Your note titled "{ndata.title}" has been rejected by the admin.

            You can now view it in your dashboard.

            Thank you for using NotesApp.

            Regards,
            NotesApp Team
            """

    f_email = settings.EMAIL_HOST_USER
    r_email = [ndata.user.email]

    # send email
    send_mail(subject=sub, message=msg, from_email=f_email, recipient_list=r_email)
    print("rejected & Email Sent")

    return redirect('admin_notes_card')

def admin_note_delete(request,nid):
    ndata=notesdata.objects.get(id=nid)
    ndata.delete()
    return redirect('admin_notes')

def contact(request):
    c_data = contactinfo.objects.all()
    return render(request,'admin_contact.html',{'c_data':c_data})

def contact_delete(request,cid):
    c_data=contactinfo.objects.get(id=cid)
    c_data.delete()
    return redirect('admin_contact')





