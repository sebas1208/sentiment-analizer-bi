import { ByHourService } from './by-hour.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-by-hour',
  templateUrl: './by-hour.component.html',
  styleUrls: ['./by-hour.component.css']
})
export class ByHourComponent implements OnInit {

  options: Object;

  constructor(private hourService: ByHourService) { }

  ngOnInit() {
    this.hourService.getByHours().subscribe(data => {
      let list = []
      for (const prop in data){
        list.push(data[prop])
      }
      this.options = {
        title : { text : 'Tweets por Hora' },
        plotOptions: {
          line: {
            dataLabels: {
              enabled: true
            },
            enableMouseTracking: false
          }
        },
        xAxis: {
            categories: ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
                          '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
        },
        series: [{
            name: '# tweets',
            data: list,
        }]
      };
    })
  }

}
