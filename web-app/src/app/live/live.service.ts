import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/distinctUntilChanged';
import 'rxjs/add/observable/of';
import 'rxjs/Observable';

@Injectable()
export class LiveService {

    users:Array<any> = [];

    private limit = 5;
    private offset = 120;

    constructor(private http: Http) { }
    
    getLastTweetFromDB() {
        let url = `http://localhost:5984/tweets_uio/_design/quito_view/_view/quito_view?descending=true&limit=${this.limit}&skip=${this.offset}`;
        this.offset = this.offset + this.limit;
        return this.http.get(url).map(res => res.json())
    }

    processTweet(tweet) {
        var source = Observable.of(42, 42, 24, 24);
        return this.http.get('http://localhost:5000/processTweet/' + tweet).map(res => res.json())
            ;
    }
}