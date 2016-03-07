export class Venue{
	constructor(
        private _id,
        private _name,
        private _start_time,
        private _duration
	){ }

	get name() { return this._name; }

	static build(json){
		return new Venue(
			json.id,
			json.name,
			json.start_time,
			json.duration
		)
	}
}