(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-846b7b88"],{"0707":function(t,i,a){var s=a("ded3").default,r=a("4082").default,e=["class","staticClass","style","staticStyle","attrs"];a("99af"),t.exports={functional:!0,render:function(t,i){var a=i._c,n=(i._v,i.data),o=i.children,c=void 0===o?[]:o,l=n.class,d=n.staticClass,_=n.style,g=n.staticStyle,u=n.attrs,f=void 0===u?{}:u,v=r(n,e);return a("svg",s({class:[l,d],style:[_,g],attrs:Object.assign({viewBox:"0 0 8 12",fill:"none",xmlns:"http://www.w3.org/2000/svg"},f)},v),c.concat([a("path",{attrs:{d:"M7.41 10.58L2.83 6l4.58-4.59L6 0 0 6l6 6 1.41-1.42z",fill:"#26BCC2"}})]))}}},1148:function(t,i,a){"use strict";var s=a("da84"),r=a("5926"),e=a("577e"),n=a("1d80"),o=s.RangeError;t.exports=function(t){var i=e(n(this)),a="",s=r(t);if(s<0||s==1/0)throw o("Wrong number of repetitions");for(;s>0;(s>>>=1)&&(i+=i))1&s&&(a+=i);return a}},"25f0":function(t,i,a){"use strict";var s=a("e330"),r=a("5e77").PROPER,e=a("6eeb"),n=a("825a"),o=a("3a9b"),c=a("577e"),l=a("d039"),d=a("ad6d"),_="toString",g=RegExp.prototype,u=g[_],f=s(d),v=l((function(){return"/a/b"!=u.call({source:"a",flags:"b"})})),p=r&&u.name!=_;(v||p)&&e(RegExp.prototype,_,(function(){var t=n(this),i=c(t.source),a=t.flags,s=c(void 0===a&&o(g,t)&&!("flags"in g)?f(t):a);return"/"+i+"/"+s}),{unsafe:!0})},"5d3d":function(t,i,a){"use strict";a.r(i);var s=function(){var t=this,i=t.$createElement,a=t._self._c||i;return a("div",{staticClass:"wrapper"},[a("main",{staticClass:"main"},[a("div",{staticClass:"wrap-info-right"},[a("div",{staticClass:"rating-wrap"},[a("h3",{staticClass:"individual-rating"},[t._v("Индивидуальный рейтинг")]),a("div",{staticClass:"period"},[a("span",{staticClass:"period__arrow"},[a("PeriodArrowSvg",{staticClass:"period__arrow__svg"})],1),a("p",{staticClass:"period__info"},[t._v("за неделю")]),a("span",{staticClass:"period__arrow"},[a("PeriodArrowSvg",{staticClass:"period__arrow__svg to-right"})],1)])]),a("div",{staticClass:"b-right"},t._l(t.individualRating,(function(i){return a("div",{key:i.id,staticClass:"b-right__item"},[a("div",{staticClass:"b-right__num"},[t._v(t._s(i.id))]),a("div",{staticClass:"b-right__info"},[a("img",{staticClass:"b-right__img",attrs:{src:i.img,alt:""}}),a("div",{staticClass:"b-right__wrap"},[a("h4",{staticClass:"b-right__title"},[t._v(" "+t._s(i.name)+" ")]),a("span",{staticClass:"b-right__description"},[t._v(t._s(i.description))]),a("p",{staticClass:"b-right__rating"},[t._v(" Рейтинг "+t._s(t.toNumberString(i.ratingValue))+" ")])])])])})),0)]),a("div",{staticClass:"wrap-info-right"},[a("div",{staticClass:"rating-wrap"},[a("h3",{staticClass:"individual-rating"},[t._v("Командный рейтинг")]),a("div",{staticClass:"period"},[a("span",{staticClass:"period__arrow"},[a("PeriodArrowSvg",{staticClass:"period__arrow__svg"})],1),a("p",{staticClass:"period__info"},[t._v("за месяц")]),a("span",{staticClass:"period__arrow"},[a("PeriodArrowSvg",{staticClass:"period__arrow__svg to-right"})],1)])]),a("div",{staticClass:"b-left"},t._l(t.teamRating,(function(i){return a("div",{key:i.id,staticClass:"b-left__item"},[a("div",{staticClass:"b-left__num"},[t._v(t._s(i.id))]),a("div",{staticClass:"b-left__info"},[a("img",{staticClass:"b-left__img",attrs:{src:i.img,alt:""}}),a("div",{staticClass:"b-left__wrap"},[a("h4",{staticClass:"b-left__title"},[t._v(" "+t._s(i.name)+" ")]),a("p",{staticClass:"b-left__rating"},[t._v(" Рейтинг "+t._s(t.toNumberString(i.ratingValue))+" ")])])])])})),0)])])])},r=[],e=a("5530"),n=(a("8ba4"),a("a9e3"),a("d3b7"),a("25f0"),a("b680"),a("0707")),o=a.n(n),c=a("2f62"),l={name:"Rating",components:{PeriodArrowSvg:o.a},props:{},computed:Object(e["a"])(Object(e["a"])({},Object(c["c"])("rating",["getIndividRating","getTeamRating","getIsLoading"])),{},{individualRating:function(){return this.getIndividRating},teamRating:function(){return this.getTeamRating},isLoading:function(){return this.getIsLoading}}),methods:{toNumberString:function(t){return Number.isInteger(t)?t+".00":t.toFixed(2).toString()}}},d=l,_=(a("b9df"),a("2877")),g=Object(_["a"])(d,s,r,!1,null,"5f1e1af9",null);i["default"]=g.exports},"8ba4":function(t,i,a){var s=a("23e7"),r=a("eac5");s({target:"Number",stat:!0},{isInteger:r})},"9a82":function(t,i,a){},b680:function(t,i,a){"use strict";var s=a("23e7"),r=a("da84"),e=a("e330"),n=a("5926"),o=a("408a"),c=a("1148"),l=a("d039"),d=r.RangeError,_=r.String,g=Math.floor,u=e(c),f=e("".slice),v=e(1..toFixed),p=function(t,i,a){return 0===i?a:i%2===1?p(t,i-1,a*t):p(t*t,i/2,a)},b=function(t){var i=0,a=t;while(a>=4096)i+=12,a/=4096;while(a>=2)i+=1,a/=2;return i},h=function(t,i,a){var s=-1,r=a;while(++s<6)r+=i*t[s],t[s]=r%1e7,r=g(r/1e7)},C=function(t,i){var a=6,s=0;while(--a>=0)s+=t[a],t[a]=g(s/i),s=s%i*1e7},w=function(t){var i=6,a="";while(--i>=0)if(""!==a||0===i||0!==t[i]){var s=_(t[i]);a=""===a?s:a+u("0",7-s.length)+s}return a},m=l((function(){return"0.000"!==v(8e-5,3)||"1"!==v(.9,0)||"1.25"!==v(1.255,2)||"1000000000000000128"!==v(0xde0b6b3a7640080,0)}))||!l((function(){v({})}));s({target:"Number",proto:!0,forced:m},{toFixed:function(t){var i,a,s,r,e=o(this),c=n(t),l=[0,0,0,0,0,0],g="",v="0";if(c<0||c>20)throw d("Incorrect fraction digits");if(e!=e)return"NaN";if(e<=-1e21||e>=1e21)return _(e);if(e<0&&(g="-",e=-e),e>1e-21)if(i=b(e*p(2,69,1))-69,a=i<0?e*p(2,-i,1):e/p(2,i,1),a*=4503599627370496,i=52-i,i>0){h(l,0,a),s=c;while(s>=7)h(l,1e7,0),s-=7;h(l,p(10,s,1),0),s=i-1;while(s>=23)C(l,1<<23),s-=23;C(l,1<<s),h(l,1,1),C(l,2),v=w(l)}else h(l,0,a),h(l,1<<-i,0),v=w(l)+u("0",c);return c>0?(r=v.length,v=g+(r<=c?"0."+u("0",c-r)+v:f(v,0,r-c)+"."+f(v,r-c))):v=g+v,v}})},b9df:function(t,i,a){"use strict";a("9a82")},eac5:function(t,i,a){var s=a("861d"),r=Math.floor;t.exports=Number.isInteger||function(t){return!s(t)&&isFinite(t)&&r(t)===t}}}]);
//# sourceMappingURL=chunk-846b7b88.837c99c9.js.map