(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{34:function(e,a,t){e.exports=t.p+"static/media/logo50.78de8641.png"},37:function(e,a,t){e.exports=t.p+"static/media/loading.baeaf0c7.gif"},38:function(e,a,t){e.exports=t.p+"static/media/404.9adc6c33.png"},39:function(e,a,t){e.exports=t(71)},46:function(e,a,t){},66:function(e,a,t){},69:function(e,a,t){},70:function(e,a,t){},71:function(e,a,t){"use strict";t.r(a);var n=t(0),r=t.n(n),l=t(32),c=t.n(l);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));t(44),t(21),t(45),t(46);var s=t(14),o=t(6),i=t(15),d=t(9),m=t(10),u=t(12),_=t(11),f=t(13),h=t.n(f),E=t(17),v="http://localhost:8000",g=t(34),p=t.n(g),b=function(e){return r.a.createElement("header",null,r.a.createElement("nav",{className:"navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0 shadow"},r.a.createElement("a",{className:"navbar-brand col-sm-3 col-md-2 mr-0",href:"/"},r.a.createElement("img",{className:"img-thumbnail","data-test":"logo",src:p.a,alt:"Logo"}),"\xa0 ",e.disease)))},N=(t(66),function(e){Object(u.a)(t,e);var a=Object(_.a)(t);function t(){return Object(d.a)(this,t),a.apply(this,arguments)}return Object(m.a)(t,[{key:"render",value:function(){return r.a.createElement("nav",{className:"col-sm-2 d-none d-sm-block bg-light sidebar"},r.a.createElement("div",{className:"sidebar-sticky"},r.a.createElement("ul",{className:"nav flex-column sidebar-nav"},r.a.createElement("li",{className:"nav-item centraliza_texto "},r.a.createElement(s.b,{className:"nav-link sidebar-nav-item-a",to:"/"},"Index")),r.a.createElement("li",{className:"nav-item centraliza_texto"},r.a.createElement(s.b,{className:"nav-link sidebar-nav-item-a",to:"/dados"},"Dados Diarios"))),r.a.createElement("h6",{className:"centraliza_texto"},"Desenvolvedor"),r.a.createElement("ul",{className:"nav flex-column mb-2"},r.a.createElement("li",{className:"nav-item centraliza_texto"},r.a.createElement("a",{className:"nav-link  sidebar-nav-item-a",target:"_blank",rel:"noopener noreferrer",href:"http://lariodiniz.com.br/"},"L\xe1rio Diniz")))))}}]),t}(n.Component)),y=(t(69),function(e){return r.a.createElement(r.a.Fragment,null,r.a.createElement(b,{disease:e.disease,title:e.title}),r.a.createElement("div",{className:"container-fluid"},r.a.createElement("div",{className:"row"},r.a.createElement(N,null),r.a.createElement("main",{role:"main",className:"col-12 col-sm-10 main"},e.children))))}),k=(t(70),function(e){return r.a.createElement("div",{className:"row panel_div"},r.a.createElement("div",{className:"col"},e.children))}),w=t(37),x=t.n(w),O=function(e){return r.a.createElement("div",{className:"image"},r.a.createElement("img",{className:"img-thumbnail","data-test":"loading",src:x.a,alt:"loading"}))},j={last_update:"00/00/0000",infected:0,dead:0,lethality:0},D=function(e){Object(u.a)(t,e);var a=Object(_.a)(t);function t(e){var n;return Object(d.a)(this,t),(n=a.call(this,e)).state={dados_gerais:j,dados_especificos:{},mostraGraficos:!1},n}return Object(m.a)(t,[{key:"_get_dados",value:function(){var e=this;h.a.get("".concat(v,"/api/totais")).then((function(a){e.setState(Object(i.a)({},e.state,{dados_gerais:a.data}))})).catch((function(e){return console.log(e)})),h.a.get("".concat(v,"/api/diario")).then((function(a){console.log(a.data),e.setState(Object(i.a)({},e.state,{dados_especificos:a.data,mostraGraficos:!0}))})).catch((function(e){return console.log(e)}))}},{key:"_set_continuos_get",value:function(){setInterval(this._get_dados(),3e4)}},{key:"componentWillMount",value:function(){this._get_dados()}},{key:"_format_date",value:function(e){if(e&&-1!==e.indexOf("-")){var a=e.split("-");if(3===a.length)return"".concat(a[2],"/").concat(a[1],"/").concat(a[0])}return e}},{key:"_render_dados_gerais",value:function(){return r.a.createElement("div",{className:"row"},r.a.createElement("div",{className:"col"},r.a.createElement("h3",null,"Dados Totais"),r.a.createElement("div",{className:"table-responsive"},r.a.createElement("table",{className:"table table-bordered"},r.a.createElement("thead",{className:"thead-dark"},r.a.createElement("tr",null,r.a.createElement("th",null,"Atualizado"),r.a.createElement("th",null,"Total de Infectados"),r.a.createElement("th",null,"Total de Mortos"),r.a.createElement("th",null,"Letalidade"))),r.a.createElement("tbody",null,r.a.createElement("tr",{className:"table-danger centraliza_texto"},r.a.createElement("td",null,this._format_date(this.state.dados_gerais.last_update)),r.a.createElement("td",null,this.state.dados_gerais.infected),r.a.createElement("td",null,this.state.dados_gerais.dead),r.a.createElement("td",null,this.state.dados_gerais.lethality," % ")))))))}},{key:"_render_grafico_totais",value:function(){var e=[["Estatos","Quantidade"],["Saldavel",211462943-this.state.dados_gerais.infecteds],["Infectados",this.state.dados_gerais.infecteds],["Mortos",this.state.dados_gerais.deads]];return r.a.createElement("div",{className:"row"},r.a.createElement("div",{className:"col"},r.a.createElement(E.a,{height:"300px",chartType:"PieChart",data:e,options:{title:"Popoula\xe7\xe3o Brasileira"}})))}},{key:"_render_grafico_linha",value:function(e,a,t,n){var l={series:e,lineWidth:3,pointSize:5,hAxis:{title:t,slantedText:!0,slantedTextAngle:90},vAxis:{title:n}};return r.a.createElement("div",{className:"row"},r.a.createElement("div",{className:"col"},r.a.createElement("div",{className:"image"},r.a.createElement(E.a,{height:"300px",chartType:"LineChart",data:a,options:l}))))}},{key:"_render_grafico_dia_infectados",value:function(){var e=this,a=[["Dia","Infectados","Novos Infectados"]];return this.state.dados_especificos.forEach((function(t){var n=[e._format_date(t.day),t.infecteds,t.infected_news];a.push(n)})),this._render_grafico_linha({0:{color:"#e2431e"},1:{color:"#43459d"}},a,"Dia","Infectados")}},{key:"_render_grafico_dia_mortos",value:function(){var e=this,a=[["Dia","Mortos"]];return this.state.dados_especificos.forEach((function(t){var n=[e._format_date(t.day),t.deads];a.push(n)})),this._render_grafico_linha({0:{color:"#e2431e"}},a,"Dia","Mortos")}},{key:"_render_grafico_dia_letalidae",value:function(){var e=this,a=[["Dia","Letalidade"]];return this.state.dados_especificos.forEach((function(t){var n=[e._format_date(t.day),Number(t.lethality)];a.push(n)})),this._render_grafico_linha({0:{color:"#e2431e"}},a,"Dia","Letalidade")}},{key:"_render_graficos",value:function(){return this.state.mostraGraficos?r.a.createElement("div",{className:"row"},r.a.createElement("div",{className:"col"},this._render_grafico_totais(),r.a.createElement("hr",null),r.a.createElement("h3",null,"Infectados / Dia"),this._render_grafico_dia_infectados(),r.a.createElement("hr",null),r.a.createElement("h3",null,"Mortos / Dia"),this._render_grafico_dia_mortos(),r.a.createElement("hr",null),r.a.createElement("h3",null,"Letalidade"),this._render_grafico_dia_letalidae())):r.a.createElement(O,null)}},{key:"render",value:function(){return r.a.createElement(y,{disease:"Sars-CoV-2 (Coronavirus)"},r.a.createElement(k,null,this._render_dados_gerais(),r.a.createElement("hr",null),this._render_graficos()))}}]),t}(n.Component),I=function(e){Object(u.a)(t,e);var a=Object(_.a)(t);function t(e){var n;return Object(d.a)(this,t),(n=a.call(this,e)).state={dados_especificos:{},mostraGraficos:!1},n}return Object(m.a)(t,[{key:"_get_dados",value:function(){var e=this;h.a.get("".concat(v,"/api/diario")).then((function(a){e.setState(Object(i.a)({},e.state,{dados_especificos:a.data,mostraGraficos:!0}))})).catch((function(e){return console.log(e)})),console.log("dados atualizados")}},{key:"_set_continuos_get",value:function(){setInterval(this._get_dados,500)}},{key:"componentWillMount",value:function(){this._get_dados()}},{key:"_format_date",value:function(e){if(e&&-1!==e.indexOf("-")){var a=e.split("-");if(3===a.length)return"".concat(a[2],"/").concat(a[1],"/").concat(a[0])}return e}},{key:"_render_table_line",value:function(){var e=this;return this.state.dados_especificos.map((function(a){return r.a.createElement("tr",{key:a.pk,className:"centraliza_texto"},r.a.createElement("td",null,e._format_date(a.day)),r.a.createElement("td",null,a.infecteds),r.a.createElement("td",null,a.infected_porcents),r.a.createElement("td",null,a.infected_news),r.a.createElement("td",null,a.infected_news_porcents),r.a.createElement("td",null,a.deads),r.a.createElement("td",null,a.dead_porcents),r.a.createElement("td",null,a.dead_news),r.a.createElement("td",null,a.dead_news_porcents),r.a.createElement("td",null,a.lethality))}))}},{key:"_render_table_dados",value:function(){return r.a.createElement("div",{className:"row"},r.a.createElement("div",{className:"col"},r.a.createElement("h3",null,"Dados Diarios"),r.a.createElement("div",{className:"table-responsive"},r.a.createElement("table",{className:"table table-bordered table-striped table-sm"},r.a.createElement("thead",{className:"thead-dark"},r.a.createElement("tr",null,r.a.createElement("th",null,"Dia"),r.a.createElement("th",null,"Infectados"),r.a.createElement("th",null,"%"),r.a.createElement("th",null,"Novos Infectados"),r.a.createElement("th",null,"%"),r.a.createElement("th",null,"Mortos"),r.a.createElement("th",null,"%"),r.a.createElement("th",null,"Novos Mortos"),r.a.createElement("th",null,"%"),r.a.createElement("th",null,"Letalidade"))),r.a.createElement("tbody",null,this._render_table_line())))))}},{key:"_render_graficos",value:function(){return this.state.mostraGraficos?this._render_table_dados():r.a.createElement(O,null)}},{key:"render",value:function(){return r.a.createElement(y,{disease:"Sars-CoV-2 (Coronavirus)"},r.a.createElement(k,null,this._render_graficos()))}}]),t}(n.Component),z=t(38),M=t.n(z),C=function(e){return r.a.createElement("div",{className:"container"},r.a.createElement("br",null),r.a.createElement("div",{className:"row"},r.a.createElement("div",{className:"col"},r.a.createElement("div",{className:"row justify-content-md-center"},r.a.createElement("img",{className:"img-fluid rounded",alt:"mostra 404 not found",src:M.a})))))},L=function(e){return r.a.createElement(s.a,null,r.a.createElement(o.c,null,r.a.createElement(o.a,{path:"/",exact:!0,component:D}),r.a.createElement(o.a,{path:"/dados",component:I}),r.a.createElement(o.a,{path:"*",component:C})))};c.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(L,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[39,1,2]]]);
//# sourceMappingURL=main.d407a8b3.chunk.js.map