(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-51ab2327"],{"412f":function(t,s,e){"use strict";e.r(s);var a=function(){var t=this,s=t.$createElement,e=t._self._c||s;return e("div",{staticClass:"tests-wrapper"},[t.testStatus?e("div",{staticClass:"test"},[e("div",{staticClass:"test__progress"},[e("router-link",{staticClass:"progress-close",attrs:{to:"/tests"}},[e("Close")],1),e("progress",{staticClass:"progress-bar",attrs:{max:t.test.questions.length},domProps:{value:t.currentQuestionNumber+1}})],1),e("h2",{staticClass:"test__name"},[t._v(t._s(t.test.name))]),e("h3",{staticClass:"test__question-number"},[t._v(" Вопрос "+t._s(t.currentQuestionNumber+1)+" ")]),e("p",{staticClass:"test__question-description"},[t._v(" "+t._s(t.test.questions[t.currentQuestionNumber].question)+" ")]),t._l(t.test.questions[t.currentQuestionNumber].options,(function(s){return e("div",{key:s,staticClass:"test__answer-options"},[e("button",{staticClass:"answer-option",class:{active:t.selectedValue==s},on:{click:function(e){return t.selectOption(s)}}},[t._v(" "+t._s(s)+" ")])])})),t.currentQuestionNumber<t.test.questions.length-1?e("button",{staticClass:"test__next active",attrs:{disabled:!t.selectedValue},on:{click:function(s){return t.nextQuestion()}}},[t._v(" Дальше ")]):e("button",{staticClass:"test__next active",attrs:{disabled:!t.selectedValue},on:{click:function(s){return t.endTest()}}},[t._v(" Завершить тест ")])],2):e("div",{staticClass:"test-passed"},[e("Medal",{staticClass:"test-passed__medal"}),e("h2",{staticClass:"test-passed__headline"},[t._v("Тест пройден")]),e("div",{staticClass:"test-passed__statistic"},[e("div",{staticClass:"statistic__rights-answers"},[e("Complete",{staticClass:"rights-answers__icon"}),t._v(t._s(t.rightAnswers)+" из "+t._s(t.test.questions.length)+" ")],1),e("div",{staticClass:"statistic__time"},[e("Time",{staticClass:"time__icon"}),t._v(t._s(t.leadTime)+" ")],1)]),e("div",{staticClass:"test-passed__reward"},[e("div",{staticClass:"reward__coins"},[e("CoinSvg",{staticClass:"coins__icon"}),t._v(t._s(t.reward.coins)+" ")],1),e("div",{staticClass:"reward__lightning"},[e("LightningSvg",{staticClass:"lightning__icon"}),t._v(t._s(t.reward.lightnings)+" ")],1)]),e("router-link",{staticClass:"test-passed__back",attrs:{to:"/tests"}},[t._v("К списку тестов")])],1)])},i=[],n=e("1da1"),r=e("5530"),l=(e("96cf"),e("4de4"),e("ff22")),c=e.n(l),o=e("4844"),u=e.n(o),d=e("4ed0"),h=e.n(d),v=e("b0cb"),_=e.n(v),f=e("55c2"),g=e.n(f),w=e("bb10"),p=e.n(w),C=e("e172"),m=e("2f62"),b={components:{Close:c.a,Medal:u.a,LightningSvg:h.a,CoinSvg:_.a,Complete:g.a,Time:p.a},props:{id:{default:"0",type:String}},data:function(){return{testStatus:!0,startTime:new Date,leadTime:"",selectedValue:null,currentQuestionNumber:0,rightAnswers:0,reward:{}}},computed:Object(r["a"])(Object(r["a"])({},Object(m["c"])("tests",["getTests","getQuestionsList"])),{},{test:function(){var t=this;return this.getTests.filter((function(s){return s.id===parseInt(t.id,10)}))[0]}}),mounted:function(){var t=this;return Object(n["a"])(regeneratorRuntime.mark((function s(){return regeneratorRuntime.wrap((function(s){while(1)switch(s.prev=s.next){case 0:return s.next=2,t.QUESTIONS_REQUEST(t.id);case 2:console.log(t.getQuestionsList);case 3:case"end":return s.stop()}}),s)})))()},methods:Object(r["a"])(Object(r["a"])(Object(r["a"])({},Object(m["b"])("tests",[C["a"]])),Object(m["d"])(["accrueReward"])),{},{selectOption:function(t){this.selectedValue===t?this.selectedValue=null:this.selectedValue=t},nextQuestion:function(){this.test.questions[this.currentQuestionNumber].answer===this.selectedValue&&(this.rightAnswers+=1),this.currentQuestionNumber+=1,this.selectedValue=null},endTest:function(){this.test.questions[this.currentQuestionNumber].answer===this.selectedValue&&(this.rightAnswers+=1),this.testStatus=!1;var t=new Date,s=t-this.startTime,e=new Date(s);this.leadTime=e.getUTCMinutes()+":"+e.getUTCSeconds();var a=Math.round(this.test.reward.coins*(this.rightAnswers/this.test.questions.length)),i=Math.round(this.test.reward.lightnings*(this.rightAnswers/this.test.questions.length));this.reward={coins:a,lightnings:i},this.$store.commit("accrueReward",this.reward),this.$store.commit("tests/deleteTest",this.test.id)}})},S=b,y=(e("84b5"),e("2877")),x=Object(y["a"])(S,a,i,!1,null,"72b4ec58",null);s["default"]=x.exports},4844:function(t,s,e){var a=e("ded3").default,i=e("4082").default,n=["class","staticClass","style","staticStyle","attrs"];e("99af"),t.exports={functional:!0,render:function(t,s){var e=s._c,r=(s._v,s.data),l=s.children,c=void 0===l?[]:l,o=r.class,u=r.staticClass,d=r.style,h=r.staticStyle,v=r.attrs,_=void 0===v?{}:v,f=i(r,n);return e("svg",a({class:[o,u],style:[d,h],attrs:Object.assign({viewBox:"0 0 151 151",fill:"none",xmlns:"http://www.w3.org/2000/svg"},_)},f),c.concat([e("path",{attrs:{d:"M75.366 119.908c33.112 0 59.954-26.842 59.954-59.954S108.478 0 75.366 0C42.255 0 15.412 26.842 15.412 59.954s26.843 59.954 59.954 59.954z",fill:"#FFD15C"}}),e("path",{attrs:{d:"M26.797 95.029l-20.63 35.758 24.078-1.278L41.182 151l19.083-33.083c-13.673-3.538-25.414-11.771-33.47-22.888zM124.055 94.85c-7.996 11.147-19.737 19.411-33.38 23.007L109.816 151l10.938-21.491 24.077 1.278-20.777-35.936z",fill:"#1A2740"}}),e("path",{attrs:{d:"M75.366 103.411c24.001 0 43.457-19.456 43.457-43.457 0-24-19.456-43.457-43.457-43.457-24 0-43.457 19.456-43.457 43.457 0 24 19.457 43.457 43.457 43.457z",fill:"#F8B64C"}}),e("path",{attrs:{d:"M105.15 55.258c1.338-1.308.594-3.597-1.248-3.865l-17.151-2.496a2.236 2.236 0 01-1.695-1.249l-7.669-15.546c-.832-1.694-3.24-1.694-4.072 0l-7.639 15.546a2.36 2.36 0 01-1.694 1.249L46.83 51.393c-1.843.268-2.586 2.557-1.249 3.865l12.395 12.097a2.29 2.29 0 01.654 1.992l-2.913 17.062c-.327 1.843 1.635 3.27 3.3 2.378l15.338-8.056a2.215 2.215 0 012.11 0l15.338 8.056c1.664.862 3.596-.535 3.3-2.378L92.16 69.347a2.236 2.236 0 01.654-1.992l12.336-12.097z",fill:"#fff"}})]))}}},"55c2":function(t,s,e){var a=e("ded3").default,i=e("4082").default,n=["class","staticClass","style","staticStyle","attrs"];e("99af"),t.exports={functional:!0,render:function(t,s){var e=s._c,r=(s._v,s.data),l=s.children,c=void 0===l?[]:l,o=r.class,u=r.staticClass,d=r.style,h=r.staticStyle,v=r.attrs,_=void 0===v?{}:v,f=i(r,n);return e("svg",a({class:[o,u],style:[d,h],attrs:Object.assign({viewBox:"0 0 24 24",fill:"none",xmlns:"http://www.w3.org/2000/svg"},_)},f),c.concat([e("path",{attrs:{"fill-rule":"evenodd","clip-rule":"evenodd",d:"M12 24c6.627 0 12-5.373 12-12S18.627 0 12 0 0 5.373 0 12s5.373 12 12 12zm8.796-17.895a1 1 0 00-1.592-1.21l-8.717 11.47-4.7-5.983a1 1 0 10-1.573 1.236l5.5 7 .8 1.017.782-1.03 9.5-12.5z",fill:"#26BCC2"}})]))}}},"84b5":function(t,s,e){"use strict";e("d343")},bb10:function(t,s,e){var a=e("ded3").default,i=e("4082").default,n=["class","staticClass","style","staticStyle","attrs"];e("99af"),t.exports={functional:!0,render:function(t,s){var e=s._c,r=(s._v,s.data),l=s.children,c=void 0===l?[]:l,o=r.class,u=r.staticClass,d=r.style,h=r.staticStyle,v=r.attrs,_=void 0===v?{}:v,f=i(r,n);return e("svg",a({class:[o,u],style:[d,h],attrs:Object.assign({viewBox:"0 0 22 25",fill:"none",xmlns:"http://www.w3.org/2000/svg"},_)},f),c.concat([e("path",{attrs:{"fill-rule":"evenodd","clip-rule":"evenodd",d:"M15.738 1.41a1 1 0 01-1 1H6.902a1 1 0 110-2h7.836a1 1 0 011 1zm3.902 12.77a8.82 8.82 0 11-17.64 0 8.82 8.82 0 0117.64 0zm2 0c0 5.976-4.844 10.82-10.82 10.82S0 20.155 0 14.18C0 8.204 4.844 3.36 10.82 3.36c2.738 0 5.238 1.017 7.143 2.693l1.002-1.002a1 1 0 111.415 1.414l-1.042 1.042a10.774 10.774 0 012.302 6.673zm-9.804-5.886a1 1 0 10-2 0v4.886a1 1 0 102 0V8.294z",fill:"#26BCC2"}})]))}}},d343:function(t,s,e){},ff22:function(t,s,e){var a=e("ded3").default,i=e("4082").default,n=["class","staticClass","style","staticStyle","attrs"];e("99af"),t.exports={functional:!0,render:function(t,s){var e=s._c,r=(s._v,s.data),l=s.children,c=void 0===l?[]:l,o=r.class,u=r.staticClass,d=r.style,h=r.staticStyle,v=r.attrs,_=void 0===v?{}:v,f=i(r,n);return e("svg",a({class:[o,u],style:[d,h],attrs:Object.assign({xmlns:"http://www.w3.org/2000/svg",viewBox:"0 0 22.27 20",fill:"none"},_)},f),c.concat([e("path",{attrs:{stroke:"#545969","stroke-width":"1.996","stroke-linecap":"round",d:"M21.177 1.093L1.031 18.727M1.107 1.044l20.146 17.634"}})]))}}}}]);
//# sourceMappingURL=chunk-51ab2327.9138a463.js.map