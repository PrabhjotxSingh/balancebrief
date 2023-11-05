import { Component, NgModule } from '@angular/core';
import { SearchSharingService } from '../search-sharing.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css'],
})
export class WelcomeComponent {
  inputValue: string = '';

  constructor(
    private searchSharingService: SearchSharingService,
    private router: Router
  ) {}

  onEnterPressed(event: KeyboardEvent) {
    if (this.inputValue != '') {
      if (event.key === 'Enter') {
        this.searchSharingService.setSearchData(this.inputValue);
        this.router.navigate(['search']);
      }
    }
  }
}
