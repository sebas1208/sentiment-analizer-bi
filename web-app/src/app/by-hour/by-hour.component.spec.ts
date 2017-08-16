import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ByHourComponent } from './by-hour.component';

describe('ByHourComponent', () => {
  let component: ByHourComponent;
  let fixture: ComponentFixture<ByHourComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ByHourComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ByHourComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
