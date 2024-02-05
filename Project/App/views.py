from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib import auth,messages
from django.contrib.auth.models import *
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime, timedelta, date
from .forms import *
from django.db.models import Sum
from django.contrib.auth import *

def home(request):
    current_date = datetime.now().date()
    date_days_ago = current_date - timedelta(days=30)
    
    recent_movies = Movie.objects.filter(release_year__gte=date_days_ago)
    context = {'recent_movies': recent_movies}
    
    return render(request, 'home.html',context)

def about(request):
    return render(request,'about.html')


def login(request):
    
    if request.method =="POST":
        
        username = request.POST['username']
        password = request.POST['password']
        
        user =auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            return redirect("login")
    else:
        return render(request,"auth/login.html")
    
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Ndryshoni 'home' me emrin e rrugës që dëshironi
    return render(request, 'auth/login.html')

    
def logout(request):
    auth.logout(request)
    return redirect("/")
    
def contact(request):
    if request.method =="POST":
        name=request.POST["name"]
        surname=request.POST["surname"]
        email=request.POST["email"]
        comment=request.POST["comment"]
        
        if name != "" and surname != "" and email != "" and comment != "":
            Contact(
                contact_name=name,
                contact_surname=surname,
                contact_email=email,
                comment=comment 
                
            ).save()
            messages.success(request, "Mesazhi juaj u derga me sukses!")
        else:
            messages.error(request, "Mesazhi juaj nuk u dergua!Iu lutem plotesoni te gjitha fushat e kerkuara!")
    
    
    return render(request,'contact.html')

def register(request):

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if (
            first_name == ""
            and last_name == ""
            and username == ""
            and email == ""
            and password == ""
            and confirm_password == ""
        ):
            messages.error(request, "Fill in all fields.")
        # Nese password nuk jane te njejta
        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")
        # Nese user-i ekziston
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            # Krijimi i user-it te ri
            user = User.objects.create_user(
                email=email,
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            # Vendosja e sigurise per password
            user.set_password(password)
            user.save()
            # Pas regjistrimit te userit kalohet tek faqja e login-it
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("../login/")
    # Renderizimi i html-se dhe kontekstit
    return render(request, "auth/register.html")

def movie_list(request):
    current_date = datetime.now().date()
    selected_date_str = request.GET.get('date', str(current_date))

    selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()

    showings_today = Showing.objects.filter(date=selected_date).order_by('time')

    program_title = get_program_title(selected_date, current_date)

    context = {
        'showings_today': showings_today,
        'current_date': current_date,
        'max_date': current_date + timedelta(days=7),
        'program_title': program_title,
    }

    return render(request, 'movie_list.html', context)

def get_program_title(selected_date, current_date):
    difference_in_days = (selected_date - current_date).days

    if difference_in_days == 0:
        return "Programi në Kinema për Sot"
    elif difference_in_days == 1:
        return "Programi në Kinema për Neser"
    else:
        return "Programi në Kinema"




def movie_detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})

def actor_list(request):
    actors = Actor.objects.all()
    return render(request, 'actor_list.html', {'actors': actors})

def actor_detail(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    movies = actor.movies.all() 
    context={
        'actor': actor,
        'movies': movies
    }
    return render(request, 'actor_detail.html', context)


@login_required(login_url='/user-login/') 
def reserve_ticket(request, showing_id):
    showing = get_object_or_404(Showing, pk=showing_id)
    hall_capacity = showing.hall.seat_capacity

    total_price = 0  

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            num_tickets = form.cleaned_data['number_of_tickets']
            total_reserved_tickets = Reservation.objects.filter(showing=showing).aggregate(total_tickets=Sum('number_of_tickets'))['total_tickets'] or 0

            if total_reserved_tickets + num_tickets > hall_capacity:
                all_tickets_reserved = True
            else:
                reservation = Reservation.objects.create(
                    showing=showing,
                    user=request.user,
                    number_of_tickets=num_tickets
                )
                total_price = num_tickets * showing.ticket_price
                reservation.total_price = total_price
                reservation.save()
                return redirect('reservation_detail', reservation_id=reservation.id)
    else:
        form = ReservationForm()
        all_tickets_reserved = False

    total_reserved_tickets = showing.reservation_set.aggregate(Sum('number_of_tickets'))['number_of_tickets__sum'] or 0
    ticket_price = showing.ticket_price
    
    context = {
        'form': form, 
        'showing': showing, 
        'all_tickets_reserved': all_tickets_reserved, 
        'total_reserved_tickets': total_reserved_tickets, 
        'ticket_price': ticket_price,
        'total_price': total_price, 
    }

    return render(request, 'reserve_ticket.html', context)

@user_passes_test(lambda u: u.is_authenticated, login_url='/auth/login/')
def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    return render(request, 'reservation_detail.html', {'reservation': reservation})

@login_required
def profile_view(request):
    user = request.user
    reservations = Reservation.objects.filter(user_id=user.id)
    
    # Përditësojeni llogaritjet për totalin e çmimit
    for reservation in reservations:
        reservation.total_price = reservation.showing.ticket_price * reservation.number_of_tickets

    return render(request, 'profile.html', {'user': user, 'reservations': reservations})
