import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { PrimarySideNavComponent } from './components/primary-side-nav/primary-side-nav.component';
import { SecondarySideNavComponent } from './components/secondary-side-nav/secondary-side-nav.component';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { PageNotFoundComponent } from './pages/page-not-found/page-not-found.component';

@NgModule({
  declarations: [
    AppComponent,
    PrimarySideNavComponent,
    SecondarySideNavComponent,
    HeaderComponent,
    FooterComponent,
    DashboardComponent,
    PageNotFoundComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FontAwesomeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
