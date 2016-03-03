export class User{
	constructor(
        private _id: string,
        private _email: string,
        private _is_email_verify: boolean,
        private _create_date: Date,
        private _first_name: string,
        private _last_name: string,
        private _phone: string,
        private _gender: string,
        private _is_active: boolean,
        private _is_exempt: boolean,
        private _ndc_old_id: string,
        private _is_member_old: boolean
	){

	}

	get first_name() { return this._first_name; }
	get last_name() { return this._last_name; }
	get full_name() { return this._first_name + ' ' + this._last_name; }
	get email() { return this._email; }
	get phone() { return this._phone; }
	get ndc_old_id() { return this._ndc_old_id; }
	get is_member() { return this._is_member_old; }

	static build(json): User{
		return new User(
			json.id,
			json.email,
			json.is_email_verify,
			json.create_date,
			json.first_name,
			json.last_name,
			json.phone,
			json.gender,
			json.is_active,
			json.is_exempt,
			json.ndc_old_id,
			json._is_member_old
		)
	}
}