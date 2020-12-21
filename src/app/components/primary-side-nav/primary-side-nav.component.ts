import { Component, OnInit } from '@angular/core';

import {
  faHome,
  faCalendar,
  faTasks,
  faStickyNote,
  faCog,
  faTh,
  faTable,
  faBorderAll,
  faUser,
  faExpand,
} from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-primary-side-nav',
  templateUrl: './primary-side-nav.component.html',
  styleUrls: ['./primary-side-nav.component.scss']
})
export class PrimarySideNavComponent implements OnInit {

  faCalendar = faCalendar;
  faTasks = faTasks;
  faStickyNote = faStickyNote;
  faCog = faCog;
  faTh = faTh;
  faHome = faHome;
  faUser = faUser;
  faTable = faTable;
  faBorderAll = faBorderAll;
  faExpand = faExpand;
  constructor() { }

  ngOnInit(): void {
  }

}
