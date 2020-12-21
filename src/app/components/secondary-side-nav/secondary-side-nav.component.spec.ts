import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SecondarySideNavComponent } from './secondary-side-nav.component';

describe('SecondarySideNavComponent', () => {
  let component: SecondarySideNavComponent;
  let fixture: ComponentFixture<SecondarySideNavComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SecondarySideNavComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SecondarySideNavComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
