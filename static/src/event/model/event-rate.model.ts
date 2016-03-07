export class Event_rate{
	constructor(
		private _id:number,
		private _rate_internal:number,
		private _amount:number
	){ }

	get sort_order() { return this._rate_internal; }

	static build(json){
		return new Event_rate(
			json.id,
			json.rate_internal,
			json.amount
		);
	}
}