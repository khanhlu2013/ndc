import { Event_rate } from './event-rate.model';
import { User } from '../../user/user.model';

export class Attendance{
	constructor(
		private _id: number,
		private _date_time: Date,
		private _user: User,
		private _anonymous_first_name: string,
		private _anonymous_last_name: string,
		private _event_rate: Event_rate,
		private _payment_type_internal: number
	){ }

	static build(json){
		let user = null;
		if(json.user != null){
			user = User.build(json.user);
		}
		let event_rate = Event_rate.build(json.event_rate);
		
		return new Attendance(
			json.id,
			new Date(json.date_time),
			user,
			json.anonymous_first_name,
			json.anonymous_last_name,
			event_rate,
			json.payment_type
		);
	}
}