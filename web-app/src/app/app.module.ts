import { GeneralService } from './general/general.service';
import { LiveService } from './live/live.service';
import { ByHourService } from './by-hour/by-hour.service';
import { TodoService } from './todo.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RouterModule, Routes } from '@angular/router';
import { HttpModule } from '@angular/http';
import { FormsModule } from '@angular/forms';
import { ChartModule } from 'angular2-highcharts';

import { FieldsetModule } from 'primeng/primeng';

import { MenuModule, CalendarModule } from 'primeng/primeng';

import { AlertModule } from 'ngx-bootstrap';

import { AppComponent } from './app.component';
import { ByHourComponent } from './by-hour/by-hour.component';
import { LiveComponent } from './live/live.component';
import { GeneralComponent } from './general/general.component';

const routes: Routes = [
  { path: 'by-hour', component: ByHourComponent},
  { path: 'live', component: LiveComponent},
  { path: 'general', component: GeneralComponent},
];

@NgModule({
  declarations: [
    AppComponent,
    ByHourComponent,
    LiveComponent,
    GeneralComponent,
  ],
  imports: [
    FormsModule,
    BrowserModule,
    ChartModule.forRoot(require('highcharts')),
    HttpModule,
    RouterModule.forRoot(routes),
    AlertModule.forRoot(),
    BrowserAnimationsModule,

    // PrimeNG Modules
    MenuModule,
    CalendarModule,
    FieldsetModule
  ],
  providers: [TodoService, ByHourService, LiveService, GeneralService],
  bootstrap: [AppComponent]
})
export class AppModule { }
