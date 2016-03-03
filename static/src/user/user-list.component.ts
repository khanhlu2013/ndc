import { Component } from 'angular2/core';
import { UserDaoService } from './user.dao';
import { OnInit } from 'angular2/core';
import { User } from './user.model';

@Component({
	template:`
		<h3>members management</h3>
		<table border="1">
			<tr>
				<th>first name</th>
				<th>last name</th>
				<th>email</th>
				<th>phone</th>
				<th>not member</th>
			</tr>
			<tr *ngFor="#user of user_lst">
				<td>{{user.first_name}}</td>
				<td>{{user.last_name}}</td>
				<td>{{user.email}}</td>
				<td>{{user.phone}}</td>
				<td>{{user.is_member ? '' : 'yes'}}</td>
			</tr>
		</table>	
	`
})
export class UserListComponent implements OnInit{
	constructor(private _user_dao_service:UserDaoService){ }
	
	private user_lst:User[];
	private error_message: string;

	private get_user_lst() {
		this._user_dao_service.get_user_lst()
			.subscribe(
				user_lst => this.user_lst = user_lst,
				error => this.error_message = <any>error
			);
	}

	ngOnInit(){
		this.get_user_lst();
	}
}