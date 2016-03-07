import { Injectable } from 'angular2/core';
import { Http, Response } from 'angular2/http';
import { Observable }     from 'rxjs/Observable';
import { Event } from './model/event.model';

@Injectable()
export class EventDaoService {
	private event_lst_url = 'event/get_event_lst';
	constructor(private http: Http) { }
	get_event_lst() {
		return this.http.get(this.event_lst_url)
			.map(res => {
				console.log(res);
				return <Event[]>res.json().map(Event.build)
			})
			.catch(this.handleError);
	}
	private handleError(error: Response) {
		// in a real world app, we may send the error to some remote logging infrastructure
		// instead of just logging it to the console
		console.error(error);
		return Observable.throw(error.json().error || 'Server error');
	}
}