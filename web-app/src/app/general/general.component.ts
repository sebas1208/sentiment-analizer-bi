import { GeneralService } from './general.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-general',
  templateUrl: './general.component.html',
  styleUrls: ['./general.component.css']
})
export class GeneralComponent implements OnInit {

  options: Object;

  constructor(private general:GeneralService) { }

  ngOnInit() {
    this.general.getGeneral().subscribe(data => {
      console.log(data);
      let list = []
      for (const prop in data){
        list.push(data[prop])
      }
      this.options = {
        chart: {
            type: 'column'
        },
        plotOptions: {
          column: {
            dataLabels: {
              enabled: true
            }
          }
        },
        title : { text : 'Percepción de Sentimientos General' },
        xAxis: {
            categories: ['# Tweet']
        },
        series: [{
            name: 'Positivo',
            data: [list[2]],
        }, {
            name: 'Negativo',
            data: [list[0]],
        }, {
            name: 'Neutro',
            data: [list[1]],
        }]
      };
    })
  }

}
