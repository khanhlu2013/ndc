import { Venue } from './venue.model';
import { Attendance } from './attendance.model';
import { Event_rate } from './event-rate.model';

export class Event{
	constructor(
		private _id:number,
		private _date:Date,
		private _duration:number,
		private _venue:Venue,
		private _attendance_lst:Attendance[],
		private _event_rate_lst:Event_rate[]
	){ }

	get date() { return this._date; }
	get venue() { return this._venue; }

	static build(json){
		let venue = Venue.build(json.venue);
		let attendance_lst = json.attendance_lst.map(Attendance.build);
		let event_rate_lst = json.event_rate_lst.map(Event_rate.build);

		return new Event(
			json.id,
			new Date(json.date),
			json.duration,
			venue,
			attendance_lst,
			event_rate_lst
		);
	}
}