import { Component } from 'angular2/core';
import { AppSettingComponent } from './app.setting';

@Component({
	selector : 'my-app',
	template :`
		<h1>{{title}}</h1>
		<p>{{setting|json}}</p>
	`,
	providers:[AppSettingComponent]
})
export class AppComponent{
	constructor(private setting: AppSettingComponent){
		console.log(setting);
	}
	title = 'Hello world';
}