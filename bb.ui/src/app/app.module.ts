import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { SearchComponent } from './search/search.component';
import { FormsModule } from '@angular/forms';
import { SearchSharingService } from './search-sharing.service';

@NgModule({
  declarations: [AppComponent, WelcomeComponent, SearchComponent],
  imports: [BrowserModule, AppRoutingModule, FormsModule],
  providers: [SearchSharingService],
  bootstrap: [AppComponent],
})
export class AppModule {}
