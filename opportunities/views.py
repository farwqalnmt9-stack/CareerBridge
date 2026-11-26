from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ApplicationForm, SignUpForm
from .models import Opportunity, Profile


DEMO_OPPORTUNITIES = [
    {"title_ar": "مساعد مطوّر Django", "title_en": "Junior Django Developer", "company": "Nexa Studio", "category": "development", "location_ar": "عن بُعد", "location_en": "Remote", "description_ar": "ساهم في بناء واجهات ولوحة إدارة لمنصة تعليمية.", "description_en": "Help build interfaces and an admin workspace for an education platform."},
    {"title_ar": "متدرب تصميم واجهات", "title_en": "UI Design Intern", "company": "Nova Labs", "category": "design", "location_ar": "دمشق", "location_en": "Damascus", "description_ar": "حوّل الأفكار إلى شاشات واضحة ومتجاوبة.", "description_en": "Turn product ideas into clear, responsive screens."},
    {"title_ar": "مساعد تسويق رقمي", "title_en": "Digital Marketing Assistant", "company": "Orbit", "category": "marketing", "location_ar": "عن بُعد", "location_en": "Remote", "description_ar": "شارك في حملات نموّ حقيقية وتعلّم من فريق متخصص.", "description_en": "Support real growth campaigns and learn with a specialist team."},
]


def home(request):
    items = list(Opportunity.objects.all()[:3]) or DEMO_OPPORTUNITIES
    return render(request, "opportunities/home.html", {"opportunities": items})


def opportunity_list(request):
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    remote = request.GET.get("remote", "")
    items = Opportunity.objects.all()
    if query:
        items = items.filter(Q(title_en__icontains=query) | Q(title_ar__icontains=query) | Q(company__icontains=query) | Q(category__icontains=query))
    if category:
        items = items.filter(category__iexact=category)
    if remote == "1":
        items = items.filter(is_remote=True)
    categories = Opportunity.objects.values_list("category", flat=True).distinct()
    return render(request, "opportunities/list.html", {"opportunities": items if (query or category or remote or items.exists()) else DEMO_OPPORTUNITIES, "query": query, "category": category, "remote": remote, "categories": categories})


def opportunity_detail(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk)
    has_applied = request.user.is_authenticated and request.user.applications.filter(opportunity=opportunity).exists()
    return render(request, "opportunities/detail.html", {"opportunity": opportunity, "has_applied": has_applied})


def sign_up(request):
    if request.user.is_authenticated:
        return redirect("opportunities:dashboard")
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        Profile.objects.create(user=user, role=form.cleaned_data["role"])
        login(request, user)
        return redirect("opportunities:dashboard")
    return render(request, "opportunities/auth.html", {"form": form, "mode": "signup"})


def user_login(request):
    if request.user.is_authenticated:
        return redirect("opportunities:dashboard")
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect(request.GET.get("next") or "opportunities:dashboard")
    return render(request, "opportunities/auth.html", {"form": form, "mode": "login"})


def user_logout(request):
    if request.method == "POST":
        logout(request)
    return redirect("opportunities:home")


@login_required
def dashboard(request):
    applications = request.user.applications.select_related("opportunity")
    return render(request, "opportunities/dashboard.html", {"applications": applications, "application_count": applications.count(), "opportunity_count": Opportunity.objects.count(), "profile": getattr(request.user, "profile", None)})


@login_required
def apply(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk)
    if request.user.applications.filter(opportunity=opportunity).exists():
        messages.info(request, "لقد تقدّمت لهذه الفرصة سابقًا.")
        return redirect("opportunities:dashboard")
    form = ApplicationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        application = form.save(commit=False)
        application.user = request.user
        application.opportunity = opportunity
        application.save()
        messages.success(request, "تم إرسال طلبك بنجاح.")
        return redirect("opportunities:dashboard")
    return render(request, "opportunities/apply.html", {"form": form, "opportunity": opportunity})
