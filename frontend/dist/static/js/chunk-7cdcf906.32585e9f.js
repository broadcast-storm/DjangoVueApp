(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-7cdcf906"],{"274b":function(s,t,e){"use strict";e("8e57")},"43fe":function(s,t,e){"use strict";var a=function(){var s=this,t=s.$createElement,e=s._self._c||t;return e("div",{staticClass:"task"},[e("h4",{staticClass:"task__name"},[s._v(s._s(s.data.title))]),e("ProgressBar",{staticClass:"progressbar",attrs:{percent:s.data.progress}}),e("div",{staticClass:"task__info"},[e("p",{staticClass:"task__type"},[s._v("тип: "+s._s(s.getTaskType(s.data.taskType)))]),e("p",{staticClass:"task__deadline"},[null!==s.data.deadline?e("span",[s.showMore?e("span",[s._v("Дэдлайн: ")]):e("span",[s._v("До: ")]),s._v(" "+s._s(s.data.deadline)+" ")]):s._e()]),e("div",{staticClass:"task__awards"},[e("span",{directives:[{name:"show",rawName:"v-show",value:s.showMore,expression:"showMore"}]},[s._v("Награда:")]),e("div",{staticClass:"task__awards-content"},[e("div",{staticClass:"task__awards-content-item"},[e("CoinSvg",{staticClass:"task__awards-icon"}),s._v(" "+s._s(null===s.data.money?0:s.data.money)+" ")],1),e("div",{staticClass:"task__awards-content-item"},[e("LightningSvg",{staticClass:"task__awards-icon"}),s._v(" "+s._s(null===s.data.energy?0:s.data.energy)+" ")],1)])]),e("p",{directives:[{name:"show",rawName:"v-show",value:s.showMore,expression:"showMore"}],staticClass:"task__difficulty"},[s._v(" Сложность: "+s._s(s.data.difficulty)+" ")]),e("ol",{directives:[{name:"show",rawName:"v-show",value:s.showMore,expression:"showMore"}],staticClass:"task__subtasks"},[e("h6",{staticClass:"task__subtasks-title"},[s._v("Подзадачи")]),s._l(s.data.subTasks,(function(t,a){return e("li",{key:a,style:["done"===t.status?{"text-decoration":"line-through"}:{"text-decoration":"none"}]},[s._v(" "+s._s(a+1)+". "+s._s(t.title)+" ")])}))],2),e("div",{directives:[{name:"show",rawName:"v-show",value:s.showMore,expression:"showMore"}],staticClass:"task__desc"},[e("h6",{staticClass:"task__desc-title"},[s._v("Описание")]),e("p",{staticClass:"task__desc-text"},[s._v(s._s(s.data.description))])])]),e("input",{directives:[{name:"model",rawName:"v-model",value:s.showMore,expression:"showMore"}],staticClass:"task__toggle-inp",attrs:{id:"task__toggle"+(""===s.customId?s.data.id:s.customId),type:"checkbox"},domProps:{checked:Array.isArray(s.showMore)?s._i(s.showMore,null)>-1:s.showMore},on:{change:function(t){var e=s.showMore,a=t.target,i=!!a.checked;if(Array.isArray(e)){var o=null,n=s._i(e,o);a.checked?n<0&&(s.showMore=e.concat([o])):n>-1&&(s.showMore=e.slice(0,n).concat(e.slice(n+1)))}else s.showMore=i}}}),e("label",{staticClass:"task__toggle",attrs:{for:"task__toggle"+(""===s.customId?s.data.id:s.customId)}},[e("div",{staticClass:"arrow"}),e("div",{staticClass:"dot"})])],1)},i=[],o=e("b0cb"),n=e.n(o),r=e("4ed0"),l=e.n(r),c=e("b6b4"),_={name:"Task",components:{ProgressBar:c["a"],CoinSvg:n.a,LightningSvg:l.a},props:{data:{type:Object,default:function(){}},customId:{type:String,default:""}},data:function(){return{showMore:!1}},methods:{getTaskType:function(s){return"quest"===s?"Квест":"daily"===s?"Ежедневное":void 0===s?"Еженедельное":""}}},p=_,d=(e("274b"),e("2877")),v=Object(d["a"])(p,a,i,!1,null,"342adca2",null);t["a"]=v.exports},"78cc":function(s,t,e){"use strict";e("eafd")},"8e57":function(s,t,e){},b6b4:function(s,t,e){"use strict";var a=function(){var s=this,t=s.$createElement,e=s._self._c||t;return e("div",{staticClass:"progressbar"},[e("span",{staticClass:"progressbar__value"},[s._v(s._s(s.percent)+"%")]),e("div",{staticClass:"progressbar__bar",style:{width:s.percent+"%"}})])},i=[],o=(e("a9e3"),{name:"ProgressBar",props:{percent:{type:Number,default:0}}}),n=o,r=(e("bbf6"),e("2877")),l=Object(r["a"])(n,a,i,!1,null,"7561fcca",null);t["a"]=l.exports},bbf6:function(s,t,e){"use strict";e("bd35")},bd35:function(s,t,e){},d922:function(s,t,e){"use strict";e.r(t);var a=function(){var s=this,t=s.$createElement,e=s._self._c||t;return e("div",["success"===s.profileStatus?e("div",{staticClass:"profile-wrapper"},[e("div",{staticClass:"column-wrap wrap__profile"},[e("div",{ref:"profile",staticClass:"profile"},[e("div",{staticClass:"profile__main-info"},[e("div",{staticClass:"profile__main-info__photo"},[e("img",{staticClass:"img",attrs:{src:s.profileInfo.photo,alt:"User photo"}})]),e("div",{staticClass:"profile__main-info__text"},[e("h2",{staticClass:"text__name"},[s._v(" "+s._s(s.profileInfo.surname+" "+s.profileInfo.name)+" "),e("span",{staticClass:"text__name__patronymic"},[s._v(" "+s._s(s.profileInfo.patronymic)+" ")])]),e("p",{staticClass:"text__department"},[s._v(" "+s._s(s.profileInfo.division_details.title)+" ")]),e("p",{staticClass:"text__bio"},[s._v(" "+s._s(s.profileInfo.description)+" ")]),e("p",{staticClass:"text__level"},[s._v(" Текущий уровень "),e("span",{staticClass:"text__level__count"},[s._v(" "+s._s(s.profileInfo.level)+" ")])])])]),e("div",{staticClass:"profile__stats"},[e("div",{staticClass:"profile__stats-item"},[e("CoinSvg",{staticClass:"profile__stats-icon"}),e("span",{staticClass:"profile__stats-value coins"},[s._v(s._s(s.profileInfo.money))])],1),e("div",{staticClass:"profile__stats-item"},[e("LightningSvg",{staticClass:"profile__stats-icon"}),e("span",{staticClass:"profile__stats-value lightnings"},[s._v(s._s(s.profileInfo.energy))])],1),e("div",{staticClass:"profile__stats-item"},[e("HeartSvg",{staticClass:"profile__stats-icon"}),e("span",{staticClass:"profile__stats-value hearts"},[s._v(s._s(s.profileInfo.health))])],1)]),e("div",{staticClass:"task-props"},[e("div",{staticClass:"profile__task"},[e("p",{staticClass:"profile__task-title"},[s._v("Основной квест:")]),"success"===s.mainQuest.status&&0!==s.mainQuest.data.length?[e("h3",{staticClass:"profile__task-name"},[s._v(" "+s._s(s.mainQuest.data[0].title)+" ")]),e("ProgressBar",{staticClass:"progress-bar",attrs:{percent:void 0===s.mainQuest.data[0].progress?0:s.mainQuest.data[0].progress}}),e("p",{staticClass:"profile__task-deadline"},[e("span",{staticClass:"progress"},[e("span",{staticClass:"gray-txt"},[s._v("Прогресс:")]),s._v(s._s(void 0===s.mainQuest.data[0].progress?0:s.mainQuest.data[0].progress)+"% ")]),e("span",{staticClass:"gray-txt"},[s._v("Срок:")]),s._v(" до "+s._s(s.date)+" ")])]:s._e(),"success"===s.mainQuest.status&&0===s.mainQuest.data.length?e("span",{style:{color:"#7d849a",textAlign:"center",marginTop:"10px"}},[s._v("Нет активного квеста")]):s._e(),"loading"===s.mainQuest.status?e("Spinner",{attrs:{size:25,"line-bg-color":"#b1b2b7","line-fg-color":"#26bcc2"}}):s._e()],2),e("table",{staticClass:"profile__props"},[e("tr",{staticClass:"profile__props-row"},[e("td",{staticClass:"profile__props-row-title"},[s._v(" Продуктивность: ")]),e("td",{staticClass:"profile__props-row-value"},[s._v(" "+s._s(s.profileInfo.productivity)+"% ")]),e("td",{staticClass:"profile__props-row-light"},[s._v(" из 100% на сегодня ")])]),e("tr",{staticClass:"profile__props-row"},[e("td",{staticClass:"profile__props-row-title"},[s._v(" Качество: ")]),e("td",{staticClass:"profile__props-row-value"},[s._v(" "+s._s(s.profileInfo.quality)+" ")]),e("td",{staticClass:"profile__props-row-light"},[s._v(" из 100 на сегодня ")])]),e("tr",{staticClass:"profile__props-row level"},[e("td",{staticClass:"profile__props-row-title"},[s._v(" Текущий уровень: ")]),e("td",{staticClass:"profile__props-row-value"},[s._v(" "+s._s(s.profileInfo.level)+" ")]),e("td")])])])])]),e("div",{staticClass:"profile-mobile-nav"},[e("button",{staticClass:"profile-mobile-nav__btn left-btn",class:{active:"tasks"===s.screenMobile},on:{click:function(t){return s.changeScreenMobile("tasks")}}},[s._v(" Задачи ")]),e("button",{staticClass:"profile-mobile-nav__btn right-btn",class:{active:"achieves"===s.screenMobile},on:{click:function(t){return s.changeScreenMobile("achieves")}}},[s._v(" Достижения ")])]),e("div",{staticClass:"column-wrap wrap__tasks",class:{hide:"all"!==s.screenMobile&&"tasks"!==s.screenMobile}},[e("div",{staticClass:"tasks",style:{height:s.commonHeight}},[e("h2",{staticClass:"tasks__title"},[s._v("Список задач")]),"success"===s.weeklyTasks.status?["success"===s.weeklyTasks.status&&0===s.weeklyTasks.data.length?e("span",{style:{display:"inline-block",width:"100%",color:"#7d849a",textAlign:"center",marginTop:"200px"}},[s._v("Нет активных задач")]):s._l(s.weeklyTasks.data,(function(t){return e("Task",{key:s.getTaskId(t.taskType,t.id),staticClass:"tasks__item",attrs:{data:t,"custom-id":s.getTaskId(t.taskType,t.id)}})}))]:s._e(),"loading"===s.weeklyTasks.status?e("Spinner",{style:{marginTop:"200px"},attrs:{size:25,"line-bg-color":"#b1b2b7","line-fg-color":"#26bcc2"}}):s._e()],2)]),e("div",{staticClass:"column-wrap wrap__achieves",class:{hide:"all"!==s.screenMobile&&"achieves"!==s.screenMobile}},[e("div",{staticClass:"achievements",style:{height:s.commonHeight}},[e("h2",{staticClass:"achievements__title"},[s._v("Ачивки")]),e("div",{staticClass:"achievements__inner"},s._l(s.user.achievements,(function(s){return e("div",{key:s.id,staticClass:"achievements__inner-item"},[e("img",{staticClass:"achievements__inner-item__image",attrs:{alt:"",src:"completed"!==s.status?"https://via.placeholder.com/150/f7d9b9":s.img}})])})),0)])])]):s._e()])},i=[],o=e("1da1"),n=e("5530"),r=(e("96cf"),e("b0cb")),l=e.n(r),c=e("7d16"),_=e.n(c),p=e("4ed0"),d=e.n(p),v=e("b6b4"),u=e("43fe"),f=e("2f62"),h=e("9ab8"),m=e("5b7e"),g=e.n(m),w={name:"Profile",components:{CoinSvg:l.a,HeartSvg:_.a,LightningSvg:d.a,ProgressBar:v["a"],Task:u["a"],Spinner:g.a},data:function(){return{commonHeight:"",windowWidth:window.innerWidth,screenMobile:window.innerWidth>768?"all":"tasks",user:Object.assign({},this.$store.getters.getUserData)}},computed:Object(n["a"])(Object(n["a"])(Object(n["a"])(Object(n["a"])({},Object(f["c"])(["getUserData"])),Object(f["c"])("profile",["profileStatus","profileInfo"])),Object(f["c"])("tasks",["dailyTasks","weeklyTasks","mainQuest"])),{},{date:function(){var s=this.getUserData.task.deadline,t=s.getMonth()+1,e=s.getDate();return t=t<10?"0"+t:t,e=e<10?"0"+e:e,e+"."+t+"."+s.getFullYear()}}),watch:{windowWidth:function(s){s>768&&"all"!==this.screenMobile&&(this.matchHeight(),this.screenMobile="all"),s<768&&"all"===this.screenMobile&&(this.commonHeight="auto",this.screenMobile="tasks")}},mounted:function(){var s=this;return Object(o["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return s.$nextTick((function(){window.addEventListener("resize",s.onResize)})),t.next=3,s.WEEKLY_TASKS_REQUEST();case 3:return t.next=5,s.MAIN_QUEST_REQUEST();case 5:case"end":return t.stop()}}),t)})))()},beforeDestroy:function(){window.removeEventListener("resize",this.onResize)},methods:Object(n["a"])(Object(n["a"])({},Object(f["b"])("tasks",[h["h"],h["e"]])),{},{getTaskId:function(s,t){return"quest"===s?"q".concat(t):"daily"===s?"d".concat(t):void 0===s?"w".concat(t):"e".concat(t)},changeScreenMobile:function(s){this.screenMobile=s},onResize:function(){this.windowWidth=window.innerWidth,this.$refs.profile.clientHeight!==this.commonHeight&&this.matchHeight()},matchHeight:function(){this.windowWidth>768&&(this.commonHeight=this.$refs.profile.clientHeight+"px")}})},b=w,C=(e("78cc"),e("2877")),k=Object(C["a"])(b,a,i,!1,null,"6d687fc4",null);t["default"]=k.exports},eafd:function(s,t,e){}}]);
//# sourceMappingURL=chunk-7cdcf906.32585e9f.js.map