from rest_framework import serializers
from social_center_app.models import *
from rest_framework.fields import SerializerMethodField


class MyModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(MyModelSerializer, self).__init__(*args, **kwargs)

        if 'labels' in self.fields:
            raise RuntimeError(
                'You cant have labels field defined '
                'while using MyModelSerializer'
            )

        self.fields['labels'] = SerializerMethodField()

    def get_labels(self, *args):
        labels = {}

        for field in self.Meta.model._meta.get_fields():
            if field.name in self.fields:
                labels[field.name] = field.verbose_name

        return labels


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        return self._choices[obj]


class ClientListForMainWindow(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("number", "code", "full_name")


class ClientSerializers(MyModelSerializer):
    """Клиент"""

    class Meta:
        model = Client
        fields = '__all__'


class ChildListSerializers(serializers.ModelSerializer):
    """Список детей клиента"""
    sex = ChoiceField(choices=Child.SEX)

    class Meta:
        model = Child
        fields = ('full_name', 'sex', 'age')


class ChildSerializers(MyModelSerializer):
    """Ребенок"""
    # client = ClientSerializers()
    sex = ChoiceField(choices=Child.SEX)
    status = ChoiceField(choices=Child.STATUS)
    location = ChoiceField(choices=Child.LOCATION)
    documents = ChoiceField(choices=YESNO)
    fatherhood = ChoiceField(choices=YESNO)
    education = ChoiceField(choices=YESNO)
    educate_child = ChoiceField(choices=Child.EDUCATE)
    reason_refusal = ChoiceField(choices=Child.REASON)

    health = ChoiceField(choices=YESNO)
    withdrawal_symptoms = ChoiceField(choices=YESNO)
    with_mother = ChoiceField(choices=YESNO)
    hiv_status_child = ChoiceField(choices=Child.HIV)
    hiv_plus = ChoiceField(choices=YESNO)
    center_aids = ChoiceField(choices=YESNO)
    center_prevention = ChoiceField(choices=YESNO)
    hiv_prevention = ChoiceField(choices=Child.HIV_PREVENTION)

    class Meta:
        model = Child
        fields = '__all__'


class ChildCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'


class SocialLivingConditionSerializers(MyModelSerializer):
    """Социально бытовые условия"""
    # client = ClientSerializers()
    type_room = ChoiceField(choices=SocialLivingCondition.TYPE)
    sanitary_condition = ChoiceField(choices=SocialLivingCondition.SANITARY_CONDITION)
    ownership = ChoiceField(choices=SocialLivingCondition.OWNERSHIP)
    payment = ChoiceField(choices=SocialLivingCondition.PAYMENT)

    class Meta:
        model = SocialLivingCondition
        fields = '__all__'


class SocialLivingConditionCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = SocialLivingCondition
        fields = '__all__'


class SocialEconomicConditionSerializers(MyModelSerializer):
    """Социально экономические условия проживания"""
    # client = ClientSerializers()
    income_level = ChoiceField(choices=SocialEconomicCondition.LEVEL)
    income_confirmation = ChoiceField(choices=SocialEconomicCondition.CONFIRMATION)
    client_security = ChoiceField(choices=SocialEconomicCondition.SECURITY)

    class Meta:
        model = SocialEconomicCondition
        fields = '__all__'


class SocialEconomicConditionCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = SocialEconomicCondition
        fields = '__all__'


class SourceIncomeSerializers(MyModelSerializer):
    """Источники дохода"""
    # economic_condition = SocialEconomicConditionSerializers()
    salary = ChoiceField(choices=SourceIncome.SALARY)
    alimony = ChoiceField(choices=YESNO)
    material_means = ChoiceField(choices=SourceIncome.MEANS)
    rent = ChoiceField(choices=SourceIncome.RENT)
    benefits = ChoiceField(choices=YESNO)

    class Meta:
        model = SourceIncome
        fields = '__all__'


class SourceIncomeCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = SourceIncome
        fields = '__all__'


class SocialPaymentSerializers(MyModelSerializer):
    """Социальные выплаты"""
    # economic_condition = SocialEconomicConditionSerializers()
    basis_social_payments = ChoiceField(choices=BASIS)
    pension = ChoiceField(choices=SocialPayment.PENSION)
    type_social_payment = ChoiceField(choices=SocialPayment.TYPE_SOCIAL_PAYMENT)

    class Meta:
        model = SocialPayment
        fields = '__all__'


class SocialPaymentCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = SocialPayment
        fields = '__all__'


class ChildAllowanceAndCompensationSerializers(MyModelSerializer):
    """Детские пособия и компенсационные выплаты"""
    # economic_condition = SocialEconomicConditionSerializers()
    basis_payments = ChoiceField(choices=BASIS)
    type_benefit_payment = ChoiceField(choices=ChildAllowanceAndCompensation.TYPE_BENEFIT_PAYMENT)

    class Meta:
        model = ChildAllowanceAndCompensation
        fields = '__all__'


class ChildAllowanceAndCompensationCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChildAllowanceAndCompensation
        fields = '__all__'


class FacilitiesSerializers(MyModelSerializer):
    """Льготы и меры социальной поддержки,предусмотренные для определенных категорий"""
    # economic_condition = SocialEconomicConditionSerializers()
    basis_facilities = ChoiceField(choices=YESNO)
    right_facilities = ChoiceField(choices=YESNO)
    stage_registration_facilities = ChoiceField(choices=Facilities.STAGE)

    class Meta:
        model = Facilities
        fields = '__all__'


class FacilitiesCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = '__all__'


class GeneralInformationSerializers(MyModelSerializer):
    """Общая информация"""
    # client = ClientSerializers()

    sex = ChoiceField(choices=GeneralInformation.SEX)
    workPlace = ChoiceField(choices=GeneralInformation.WORK_PLACE)
    avDoc = ChoiceField(choices=YESNO)
    cityzenship = ChoiceField(choices=GeneralInformation.CITYZENSHIP)
    registration = ChoiceField(choices=GeneralInformation.REGISTRATION)
    placeOfRegistration = ChoiceField(choices=GeneralInformation.PLACE_OF_REGISTRATION)
    education = ChoiceField(choices=GeneralInformation.EDUCATION)
    professionalEducation = ChoiceField(choices=GeneralInformation.PROFESSIONAL_EDUCATION)
    specialSocialStatus = ChoiceField(choices=GeneralInformation.SPECIAL_SOCIAL_STATUS)
    disabilityGroup = ChoiceField(choices=GeneralInformation.DISABILITY_GROUP)

    class Meta:
        model = GeneralInformation
        fields = '__all__'


class GeneralInformationCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = GeneralInformation
        fields = '__all__'


class ASocialBehaviorSerializers(MyModelSerializer):
    """Информация о противоправных действиях, правонарушениях, употреблении наркотиков, алкоголя"""
    # client = ClientSerializers()
    drugUse = ChoiceField(choices=YESNO)
    frequencyOfDrugsUse = ChoiceField(choices=ASocialBehavior.FREQUENCY_OF_DRUGS_USE)
    theTreatmentWasD = ChoiceField(choices=YESNO)
    psychologicalRehabilitationWasD = ChoiceField(choices=YESNO)
    alcoholUse = ChoiceField(choices=YESNO)
    frequencyOfAlcoholUse = ChoiceField(choices=ASocialBehavior.FREQUENCY_OF_DRUGS_USE)
    alcoholDrinksType = ChoiceField(choices=ASocialBehavior.ALCOHOL_DRINKS_TYPE)
    theTreatmentWasA = ChoiceField(choices=YESNO)
    psychologicalRehabilitationWasA = ChoiceField(choices=YESNO)
    accountingInNarcologicalClinic = ChoiceField(choices=YESNO)
    criminalRecord = ChoiceField(choices=YESNO)
    accountingInODN_RUVD = ChoiceField(choices=YES_NO_DONTKNOW)
    caseExaminedInKDN_ZP = ChoiceField(choices=YES_NO_DONTKNOW)
    commercialSexExperience = ChoiceField(choices=YESNO)
    physicalAbuseExperience = ChoiceField(choices=YESNO)
    fromHwomPhysical = ChoiceField(choices=ASocialBehavior.FROM_WHOM)
    experienceSexualAbuse = ChoiceField(choices=YESNO)
    fromHwomSexual = ChoiceField(choices=ASocialBehavior.FROM_WHOM)

    class Meta:
        model = ASocialBehavior
        fields = '__all__'


class ASocialBehaviorCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = ASocialBehavior
        fields = '__all__'


class ChronicDiseaseSerializers(MyModelSerializer):
    """Информация о наличии хронического заболевания"""
    # client = ClientSerializers()

    hepatitisC = ChoiceField(choices=ChronicDisease.DISEASE)
    HIVStatus = ChoiceField(choices=ChronicDisease.DISEASE)
    estimatedRouteOfInfection = ChoiceField(choices=ChronicDisease.TYPE_INVASION)
    AIDSCenter = ChoiceField(choices=YESNO)
    doesCenterVisitAIDS = ChoiceField(choices=YESNO)
    receivedChemoprophylaxis = ChoiceField(choices=ChronicDisease.CHEMOPROPHYLAXIS)
    HIVGetTreatment = ChoiceField(choices=ChronicDisease.HIV_TREATMENT)
    whoKnow = ChoiceField(choices=ChronicDisease.HIV_FAMILY_AWARENESS)

    class Meta:
        model = ChronicDisease
        fields = '__all__'


class ChronicDiseaseCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChronicDisease
        fields = '__all__'


class FamilyMembersInformationSerializers(MyModelSerializer):
    """Сведения о членах семьи"""
    # client = ClientSerializers()
    maritalStatus = ChoiceField(choices=FamilyMembersInformation.MARITAL_STATUS)
    withWhomLiving = ChoiceField(choices=FamilyMembersInformation.LIVING_WITH_WHOM)
    regularPartner = ChoiceField(choices=YESNO)

    class Meta:
        model = FamilyMembersInformation
        fields = '__all__'


class FamilyMembersInformationCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = FamilyMembersInformation
        fields = '__all__'


class HusbandInformationSerializers(MyModelSerializer):
    """Информация о муже/партнёре"""
    # husband = FamilyMembersInformationSerializers()
    workPlace = ChoiceField(choices=HusbandInformation.WORK_PLACE)
    avDoc = ChoiceField(choices=YESNO)
    cityzenship = ChoiceField(choices=HusbandInformation.CITYZENSHIP)
    registration = ChoiceField(choices=HusbandInformation.REGISTRATION)
    placeOfRegistration = ChoiceField(choices=HusbandInformation.PLACE_OF_REGISTRATION)
    education = ChoiceField(choices=HusbandInformation.EDUCATION)
    professionalEducation = ChoiceField(choices=HusbandInformation.PROFESSIONAL_EDUCATION)
    specialSocialStatus = ChoiceField(choices=HusbandInformation.SPECIAL_SOCIAL_STATUS)
    disabilityGroup = ChoiceField(choices=HusbandInformation.DISABILITY_GROUP)
    drugUse = ChoiceField(choices=YESNO)
    frequencyOfDrugsUse = ChoiceField(choices=HusbandInformation.FREQUENCY_OF_DRUGS_USE)
    theTreatmentWasD = ChoiceField(choices=YESNO)
    psychologicalRehabilitationWasD = ChoiceField(choices=YESNO)
    alcoholUse = ChoiceField(choices=YESNO)
    frequencyOfAlcoholUse = ChoiceField(choices=HusbandInformation.FREQUENCY_OF_DRUGS_USE)
    alcoholDrinksType = ChoiceField(choices=HusbandInformation.ALCOHOL_DRINKS_TYPE)
    theTreatmentWasA = ChoiceField(choices=YESNO)
    psychologicalRehabilitationWasA = ChoiceField(choices=YESNO)
    accountingInNarcologicalClinic = ChoiceField(choices=YESNO)
    criminalRecord = ChoiceField(choices=YESNO)

    class Meta:
        model = HusbandInformation
        fields = '__all__'


class HusbandInformationCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = HusbandInformation
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    """Специалист"""

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "patronymic", "position", "email")


class ExpertOpinionSerializers(MyModelSerializer):
    """Заключение специалиста"""

    # client = ClientSerializers()
    # specialist = UserSerializers()

    class Meta:
        model = ExpertOpinion
        fields = '__all__'


class ExpertOpinionCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExpertOpinion
        fields = ('client', 'otherInformation', 'expectations', 'personaImpressions')


class TestBoykoListSerializers(serializers.ModelSerializer):
    """Список тестов Бойко"""

    class Meta:
        model = TestBoyko
        fields = ('id', 'attempt')


class TestBoykoSerializers(MyModelSerializer):
    """Тест Бойко"""
    aggressiveness = ChoiceField(choices=TestBoyko.AGGRESS)
    alarm = ChoiceField(choices=TestBoyko.ALARM)
    memory_disorder = ChoiceField(choices=TestBoyko.MEMORY_DISORDER)
    criticism = ChoiceField(choices=TestBoyko.CRITICISM)
    self_service = ChoiceField(choices=TestBoyko.SELF_SERVICE)
    work_activity = ChoiceField(choices=TestBoyko.WORK_ACTIVITY)
    friends = ChoiceField(choices=TestBoyko.FRIENDS)
    family_relation = ChoiceField(choices=TestBoyko.FAMILY_RELATION)
    child_parent = ChoiceField(choices=TestBoyko.CHILD_PARENT)
    leisure = ChoiceField(choices=TestBoyko.LEISURE)
    attempt = ChoiceField(choices=ATTEMPT)

    class Meta:
        model = TestBoyko
        fields = '__all__'


class TestBoykoCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestBoyko
        fields = '__all__'


class InterpretationBoykoSerializers(MyModelSerializer):
    """Интерпретация теста Бойко"""
    aggressiveness = ChoiceField(choices=InterpretationBoyko.AGGRESS)
    alarm = ChoiceField(choices=InterpretationBoyko.ALARM)
    memory_disorder = ChoiceField(choices=InterpretationBoyko.MEMORY_DISORDER)
    criticism = ChoiceField(choices=InterpretationBoyko.CRITICISM)
    self_service = ChoiceField(choices=InterpretationBoyko.SELF_SERVICE)
    work_activity = ChoiceField(choices=InterpretationBoyko.WORK_ACTIVITY)
    friends = ChoiceField(choices=InterpretationBoyko.FRIENDS)
    family_relation = ChoiceField(choices=InterpretationBoyko.FAMILY_RELATION)
    child_parent = ChoiceField(choices=InterpretationBoyko.CHILD_PARENT)
    leisure = ChoiceField(choices=InterpretationBoyko.LEISURE)
    overall_assessment = ChoiceField(choices=InterpretationBoyko.OVERALL_ASSESSMENT)

    class Meta:
        model = InterpretationBoyko
        fields = '__all__'


class InterpretationBoykoCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = InterpretationBoyko
        fields = '__all__'


class TestGAGEListSerializers(serializers.ModelSerializer):
    """Список тестов GAGE"""

    class Meta:
        model = TestGAGE
        fields = ('id', 'attempt')


class TestGAGESerializers(MyModelSerializer):
    """Тест GAGE"""
    alcohol = ChoiceField(choices=GAGE_YESNO)
    substances = ChoiceField(choices=TestGAGE.SUBSTANCES)
    loss_documents = ChoiceField(choices=GAGE_YESNO)
    loss_documents_when = ChoiceField(choices=TestGAGE.LOSS_DOCUMENTS_WHEN)
    loss_documents_time = ChoiceField(choices=TestGAGE.LOSS_DOCUMENTS_TIME)
    do_not_work = ChoiceField(choices=GAGE_YESNO)
    do_not_work_when = ChoiceField(choices=TestGAGE.DO_NOT_WORK_WHEN)
    loss_loved_ones = ChoiceField(choices=GAGE_YESNO)
    fight = ChoiceField(choices=GAGE_YESNO)
    injuries = ChoiceField(choices=TestGAGE.INJURIES)
    lots_alcohol = ChoiceField(choices=GAGE_YESNO)
    lots_alcohol_time = ChoiceField(choices=TestGAGE.LOTS_ALCOHOL_TIME)
    drink_alcohol_time = ChoiceField(choices=TestGAGE.DRINK_ALCOHOL_TIME)
    try_substances_choice = ChoiceField(choices=TestGAGE.TRY_SUBSTANCES)
    how_use = ChoiceField(choices=TestGAGE.HOW_USE)
    difficulties = ChoiceField(choices=GAGE_YESNO)
    poor_health = ChoiceField(choices=TestGAGE.POOR_HEALTH)
    company = ChoiceField(choices=TestGAGE.COMPANY)
    dose_reduction = ChoiceField(choices=GAGE_YESNO)
    irritation = ChoiceField(choices=GAGE_YESNO)
    fault = ChoiceField(choices=GAGE_YESNO)
    tone = ChoiceField(choices=GAGE_YESNO)
    attempt = ChoiceField(choices=ATTEMPT)

    class Meta:
        model = TestGAGE
        fields = '__all__'


class TestGAGECRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestGAGE
        fields = '__all__'


class InterpretationGAGESerializers(MyModelSerializer):
    """Интерпретация теста GAGE"""
    risk_abuse = ChoiceField(choices=InterpretationGAGE.RISK_ABUSE)
    risk_dependency = ChoiceField(choices=InterpretationGAGE.RISK_DEPENDENCY)

    class Meta:
        model = InterpretationGAGE
        fields = '__all__'


class InterpretationGAGECRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = InterpretationGAGE
        fields = '__all__'


class TestSOCRATESListSerializers(serializers.ModelSerializer):
    """Список тестов SOCRATES"""

    class Meta:
        model = TestSOCRATES
        fields = ('id', 'attempt')


class TestSOCRATESSerializers(MyModelSerializer):
    """Тест SOCRATES"""
    changes = ChoiceField(choices=TestSOCRATES.FORM)
    doubt = ChoiceField(choices=TestSOCRATES.FORM)
    aggravation = ChoiceField(choices=TestSOCRATES.FORM)
    make_changes = ChoiceField(choices=TestSOCRATES.FORM)
    too_much = ChoiceField(choices=TestSOCRATES.FORM)
    harm = ChoiceField(choices=TestSOCRATES.FORM)
    serious_problem = ChoiceField(choices=TestSOCRATES.FORM)
    changes_lifestyle = ChoiceField(choices=TestSOCRATES.FORM)
    hold = ChoiceField(choices=TestSOCRATES.FORM)
    know_trouble = ChoiceField(choices=TestSOCRATES.FORM)
    control = ChoiceField(choices=TestSOCRATES.FORM)
    much_harm = ChoiceField(choices=TestSOCRATES.FORM)
    reduce_stop = ChoiceField(choices=TestSOCRATES.FORM)
    help = ChoiceField(choices=TestSOCRATES.FORM)
    have_problem = ChoiceField(choices=TestSOCRATES.FORM)
    use_lot = ChoiceField(choices=TestSOCRATES.FORM)
    alcoholic = ChoiceField(choices=TestSOCRATES.FORM)
    try_my_best = ChoiceField(choices=TestSOCRATES.FORM)
    move_on = ChoiceField(choices=TestSOCRATES.FORM)
    attempt = ChoiceField(choices=ATTEMPT)

    class Meta:
        model = TestSOCRATES
        fields = '__all__'


class TestSOCRATESCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestSOCRATES
        fields = '__all__'


class InterpretationSOCRATESSerializers(MyModelSerializer):
    """Интерпретация тестов SOCRATES"""
    realization = ChoiceField(choices=InterpretationSOCRATES.REALIZATION)
    ambivalence = ChoiceField(choices=InterpretationSOCRATES.AMBIVALENCE)
    action = ChoiceField(choices=InterpretationSOCRATES.ACTION)
    ready_change = ChoiceField(choices=InterpretationSOCRATES.READY_CHANGE)

    class Meta:
        model = InterpretationSOCRATES
        fields = '__all__'


class InterpretationSOCRATESCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = InterpretationSOCRATES
        fields = '__all__'


class TypologicalGroupListSerializers(serializers.ModelSerializer):
    """Список типологических групп"""
    test = TestBoykoListSerializers()

    class Meta:
        model = TypologicalGroup
        fields = ('id', 'test')


class TypologicalGroupSerializers(MyModelSerializer):
    """Типологические группы"""
    group = ChoiceField(choices=TypologicalGroup.GROUP)
    subgroup = ChoiceField(choices=TypologicalGroup.SUBGROUP)

    class Meta:
        model = TypologicalGroup
        fields = '__all__'


class TypologicalGroupCRUDSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypologicalGroup
        fields = '__all__'


class GroupASocialBehaviorSerializers(serializers.ModelSerializer):
    class Meta:
        model = ASocialBehavior
        fields = ('id', 'caseExaminedInKDN_ZP')


class GroupTestBoykoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TestBoyko
        fields = ('id', 'aggressiveness')


class GroupGeneralInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = GeneralInformation
        fields = ('id', 'age')


class GroupChronicDiseaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChronicDisease
        fields = ('id', 'hepatitisC', 'HIVStatus')


class FamilyMemberSpecial(serializers.ModelSerializer):
    class Meta:
        model = FamilyMembersInformation
        fields = ('id', 'client')
        # fields = '__all__'


class ExpertForTable(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")
