import { Injectable } from 'angular2/core';
import { User } from './user.model';
import { Http, Response } from 'angular2/http';
import { Observable }     from 'rxjs/Observable';

@Injectable()
export class UserDaoService{
	private _user_lst_url = 'ndc_user/get_lst';
	constructor(private _http:Http){ }
	get_user_lst(){
		return this._http.get(this._user_lst_url)
			.map(res => { 
				console.log(res);
				return <User[]>res.json().map(User.build) 
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