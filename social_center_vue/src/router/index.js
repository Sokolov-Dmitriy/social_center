import Vue from 'vue'
import Router from 'vue-router'
import Authorization from "../components/Authorization"
import MainWindow from "../components/MainPage/MainWindow";
import Profile from "../components/Profile";
import Client from "../components/Client";
import ClientView from "../components/Information/ClientView";
import ASocialBehavior from "../components/Information/ASocialBehavior";
import ChronicDisease from "../components/Information/ChronicDisease";
import ChildList from "../components/Information/ChildList";
import ChildAdd from "../components/Information/ChildAdd";
import Child from "../components/Information/Child";
import FamilyMembers from "../components/Information/FamilyMembers";
import HusbandInformation from "../components/Information/HusbandInformation";
import SocialLivingCondition from "../components/Information/SocialLivingCondition";
import SocialEconomicCondition from "../components/Information/SocialEconomicCondition";
import SourceIncome from "../components/Information/SourceIncome";
import SocialPayment from "../components/Information/SocialPayment";
import ChildAllowanceAndCompensation from "../components/Information/ChildAllowanceAndCompensation";
import Facilities from "../components/Information/Facilities";
import ExpertOpinion from "../components/Information/ExpertOpinion";
import TestBoykoList from "../components/Test/TestBoykoList";
import TestBoyko from "../components/Test/TestBoyko";
import InterpretationBoyko from "../components/Test/InterpretationBoyko";
import TestGAGEList from "../components/Test/TestGAGEList";
import TestSOCRATESList from "../components/Test/TestSOCRATESList";
import TestSOCRATES from "../components/Test/TestSOCRATES";
import InterpretationSOCRATES from "../components/Test/InterpretationSOCRATES";
import TestGAGE from "../components/Test/TestGAGE";
import InterpretationGAGE from "../components/Test/InterpretationGAGE";
import TypologicalGroupList from "../components/Test/TypologicalGroupList";
import TypologicalGroup from "../components/Test/TypologicalGroup";
import GraphicBoyko from "../components/Test/GraphicBoyko";
import GraphicGAGE from "../components/Test/GraphicGAGE";
import GraphicSOCRATES from "../components/Test/GraphicSOCRATES";
// import "bootstrap-vue/dist/bootstrap-vue.min.css"
import MainPageComp from "../components/Table/MainPageComp";
import Users from "../components/Users";
import EnterEmail from "../components/Reset/EnterEmail";
import ConfirmPassword from "../components/Reset/ConfirmPassword";
import HusbandList from "../components/Information/HusbandList";
import HusbandAdd from "../components/Information/HusbandAdd";

Vue.use(Router)

export const router = new Router({
  routes: [
    {
      path: '/',
      name: 'mainwindow',
      component: MainWindow
    },
    {
      path: '/login',
      name: 'login',
      component: Authorization
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    },
    {
      path: '/client',
      name: 'client',
      component: Client
    },
    {
      path: '/info',
      name: 'clientView',
      component: ClientView,
    },
    {
      path: '/socialBehavior',
      name: 'socialBehavior',
      component: ASocialBehavior
    },
    {
      path: '/chronicDisease',
      name: 'chronicDisease',
      component: ChronicDisease
    },
    {
      path: '/childList',
      name: 'childList',
      component: ChildList
    },
    {
      path: '/childAdd',
      name: 'childAdd',
      component: ChildAdd
    },
    {
      path: '/child',
      name: 'child',
      component: Child
    },
    {
      path: '/familyMembers',
      name: 'familyMembers',
      component: FamilyMembers
    },
    {
      path: '/husbandInformation',
      name: 'husbandInformation',
      component: HusbandInformation
    },
    {
      path: '/socialLiving',
      name: 'socialLivingCondition',
      component: SocialLivingCondition
    },
    {
      path: '/socialEconomic',
      name: 'socialEconomicCondition',
      component: SocialEconomicCondition
    },
    {
      path: '/sourceIncome',
      name: 'sourceIncome',
      component: SourceIncome
    },
    {
      path: '/socialPayment',
      name: 'socialPayment',
      component: SocialPayment
    },
    {
      path: '/childAllowance',
      name: 'childAllowance',
      component: ChildAllowanceAndCompensation
    },
    {
      path: '/facilities',
      name: 'facilities',
      component: Facilities
    },
    {
      path: '/expertOpinion',
      name: 'expertOpinion',
      component: ExpertOpinion
    },
    {
      path: '/testBoykoList',
      name: 'testBoykoList',
      component: TestBoykoList
    },
    {
      path: '/testBoyko',
      name: 'testBoyko',
      component: TestBoyko
    },
    {
      path: '/interpretationBoyko',
      name: 'interpretationBoyko',
      component: InterpretationBoyko
    },
    {
      path: '/testGAGEList',
      name: 'testGAGEList',
      component: TestGAGEList
    },
    {
      path: '/testSOCRATESList',
      name: 'testSOCRATESList',
      component: TestSOCRATESList
    },
    {
      path: '/testSOCRATES',
      name: 'testSOCRATES',
      component: TestSOCRATES
    },
    {
      path: '/interpretationSOCRATES',
      name: 'interpretationSOCRATES',
      component: InterpretationSOCRATES
    },
    {
      path: '/testGAGE',
      name: 'testGAGE',
      component: TestGAGE
    },
    {
      path: '/interpretationGAGE',
      name: 'interpretationGAGE',
      component: InterpretationGAGE
    },
    {
      path: '/typologicalGroupList',
      name: 'typologicalGroupList',
      component: TypologicalGroupList
    },
    {
      path: '/typologicalGroup',
      name: 'typologicalGroup',
      component: TypologicalGroup
    },
    {
      path: '/graphicBoyko',
      name: 'graphicBoyko',
      component: GraphicBoyko
    },
    {
      path: '/graphicGAGE',
      name: 'graphicGAGE',
      component: GraphicGAGE
    },
    {
      path: '/graphicSOCRATES',
      name: 'graphicSOCRATES',
      component: GraphicSOCRATES
    },
    {
      path: '/table',
      name: 'mainPageComp',
      component: MainPageComp,
    },
    {
      path: '/users',
      name: 'users',
      component: Users,
    },
    {
      path: '/enterEmail',
      name: 'enterEmail',
      component: EnterEmail,
    },
    {
      path: '/confirmPassword/:uid/:token',
      name: 'confirmPassword',
      component: ConfirmPassword,
    },
    {
      path: '/husbandList',
      name: 'husbandList',
      component: HusbandList
    },
    {
      path: '/husbandAdd',
      name: 'husbandAdd',
      component: HusbandAdd
    }
  ],
});
router.beforeEach((to, from, next) => {
  if (localStorage.getItem('auth_token')) next();
  else if (to.name !== 'login') {
    localStorage.clear();
    $.ajaxSetup({
      headers: {'Authorization': null}
    });
    if(['enterEmail','confirmPassword'].includes(to.name)) next();
    else next({name: 'login'});
  } else next()
});
