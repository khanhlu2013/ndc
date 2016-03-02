import { Component,Injectable } from 'angular2/core';

@Injectable()
@Component({

})
export class AppSettingComponent{
	public MEMBERSHIP_TYPE_LST;
	public GENDER_LST;
	public DANCE_RATE_LST;
	public PHONE_REGX;

	constructor(){
		let setting = JSON.parse(window['SHARE_SETTING_JSON_STRING']);
		// delete window['SHARE_SETTING_JSON_STRING'];

		this.MEMBERSHIP_TYPE_LST = setting['MEMBERSHIP_TYPE_LST'];
		this.GENDER_LST = setting['GENDER_LST'];
		this.DANCE_RATE_LST = setting['DANCE_RATE_LST'];
		this.PHONE_REGX = setting['PHONE_REGX'];
	}
}