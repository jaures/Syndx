import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PrimarySideNavComponent } from './primary-side-nav.component';

describe('PrimarySideNavComponent', () => {
  let component: PrimarySideNavComponent;
  let fixture: ComponentFixture<PrimarySideNavComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PrimarySideNavComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PrimarySideNavComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
