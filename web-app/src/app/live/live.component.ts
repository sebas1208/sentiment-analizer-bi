import { LiveService } from './live.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-live',
  templateUrl: './live.component.html',
  styleUrls: ['./live.component.css']
})
export class LiveComponent implements OnInit {

  tweet = '';
  pos = '😊';
  neg = '☹'
  neu = '😐'
  sent = ''

  constructor(private live: LiveService) { }

  ngOnInit() {
    setInterval(() => {
      this.live.getLastTweetFromDB().subscribe(data => {
        this.live.processTweet(data.rows[0].value.text).subscribe(processedTweet => {
          if(processedTweet[2] === 'pos'){
            this.sent = this.pos;
          } else if(processedTweet[2] === 'neg'){
            this.sent = this.neg;
          } else if(processedTweet[2] === 'neu'){
            this.sent = this.neu;
          }
          data.rows[0].value.user.sent = this.sent;
          data.rows[0].value.user.text = data.rows[0].value.text;
          let tweet = this.live.users.filter(item => item.text === data.rows[0].value.text);
          if (this.live.users.filter(item => item.text === data.rows[0].value.text).length === 0){
            this.live.users = [data.rows[0].value.user, ...this.live.users];
          }
        });
      });
    }, 3000)
  }

}
