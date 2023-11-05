import { Component } from '@angular/core';
import { SearchSharingService } from '../search-sharing.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'],
})
export class SearchComponent {
  constructor(private searchSharingService: SearchSharingService) {}

  get searchData(): string {
    return this.searchSharingService.getSearchData();
  }
}
