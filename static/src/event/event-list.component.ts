import { Component,OnInit } from 'angular2/core';
import { EventDaoService } from './event.dao';
import { Event } from './model/event.model';
@Component({
	template:`
		<h3>events management</h3>
		<table border="1">
			<tr>
				<th>date</th>
				<th>venue</th>
			</tr>
			<tr *ngFor="#event of event_lst">
		 		<td>{{event.date | date}}</td>
				<td>{{event.venue.name}}</td>
			</tr>
		</table>	
	`
})
export class EventListComponent implements OnInit{

	private event_lst: Event[];
	private error_message: string;

	constructor(
		private event_dao_service:EventDaoService
	){ }
	get_event_lst(){
		this.event_dao_service.get_event_lst().subscribe(
			event_lst => this.event_lst = event_lst,
			error => this.error_message = <any>error
		)
	}
	ngOnInit(){
		this.get_event_lst();
	}
}