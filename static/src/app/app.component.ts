import { Component } from 'angular2/core';
import { AppSettingComponent } from './app.setting';
import { RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from 'angular2/router';
import { EventListComponent } from '../event/event-list.component';
import { UserListComponent } from '../user/user-list.component';
import { UserDaoService } from '../user/user.dao';
import { HTTP_PROVIDERS }    from 'angular2/http';

@Component({
	selector : 'my-app',
	template :`
		<h1>NDC Manage App</h1>
		<nav>
			<a [routerLink] = "['EventList']">Events</a>
			<a [routerLink] = "['MemberList']">Members</a>
		</nav>
		<router-outlet></router-outlet>
	`,
	directives: [ROUTER_DIRECTIVES],
	providers: [
		ROUTER_PROVIDERS, HTTP_PROVIDERS, 
		AppSettingComponent, 
		UserDaoService
	]
})
@RouteConfig([
	{ path:'/events', name:'EventList', component:EventListComponent},
	{ path: '/members', name: 'MemberList', component: UserListComponent }
])
export class AppComponent{
	constructor(private setting: AppSettingComponent){

	}
}