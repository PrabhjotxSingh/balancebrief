import { Component } from '@angular/core';
import { SearchSharingService } from '../search-sharing.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'],
})
export class SearchComponent {
  inputValue: string = '';
  queryToSearch: string = '';

  constructor(private searchSharingService: SearchSharingService) {
    const queryToSearch: string = this.searchSharingService.getSearchData();
    if (queryToSearch != '') {
      console.log(queryToSearch);
      this.inputValue = queryToSearch;
    }
  }

  get searchData(): string {
    return this.searchSharingService.getSearchData();
  }

  onSearch(event: KeyboardEvent) {
    if (this.inputValue != '') {
      if (event.key === 'Enter') {
        this.queryToSearch = this.inputValue;
        console.log(this.queryToSearch);
      }
    }
  }
}
