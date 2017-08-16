import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class ByHourService {
    constructor(private http: Http) { }

    getByHours() {
        return this.http.get('http://localhost:5000/horas').map(res => res.json());
    }
    
}