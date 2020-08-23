from django.contrib import admin
# from django.apps import apps
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


class Admin(admin.ModelAdmin):
    pass


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('patronymic', 'position')}),
    )


admin.site.register(User, MyUserAdmin)
admin.site.register(Child)
admin.site.register(Client)
admin.site.register(FamilyMembersInformation)
admin.site.register(SocialEconomicCondition)
admin.site.register(SourceIncome)
admin.site.register(SocialPayment)
admin.site.register(SocialLivingCondition)
admin.site.register(HusbandInformation)
admin.site.register(GeneralInformation)
admin.site.register(Facilities)
admin.site.register(ExpertOpinion)
admin.site.register(ChronicDisease)
admin.site.register(ChildAllowanceAndCompensation)
admin.site.register(ASocialBehavior)

admin.site.register(TestBoyko)
admin.site.register(InterpretationBoyko)
admin.site.register(TestGAGE)
admin.site.register(InterpretationGAGE)
admin.site.register(TestSOCRATES)
admin.site.register(InterpretationSOCRATES)
admin.site.register(TypologicalGroup)
# Register your models here.
