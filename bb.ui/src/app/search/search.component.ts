import { Component } from '@angular/core';
import { SearchSharingService } from '../search-sharing.service';
import { HttpClient, HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'],
})
export class SearchComponent {
  inputValue: string = '';
  queryToSearch: string = '';

  constructor(
    private searchSharingService: SearchSharingService,
    private http: HttpClient
  ) {
    const queryToSearch: string = this.searchSharingService.getSearchData();
    if (queryToSearch != '') {
      this.inputValue = queryToSearch;
    }
  }

  ngOnInit(): void {
    const queryToSearch: string = this.searchSharingService.getSearchData();
    if (queryToSearch !== '') {
      const apiUrl = 'http://127.0.0.1:8000/query';
      const params = new HttpParams().set('queryToSearch', queryToSearch);

      this.http.get(apiUrl, { params }).subscribe((data: any) => {
        if (data) {
          //do stuff id data
        }
      });
    }
  }

  get searchData(): string {
    return this.searchSharingService.getSearchData();
  }

  onSearch(event: KeyboardEvent) {
    if (this.inputValue != '') {
      if (event.key === 'Enter') {
        this.queryToSearch = this.inputValue;
        //console.log(this.queryToSearch);
        //start req
        const apiUrl = 'http://127.0.0.1:8000/query';
        const params = new HttpParams().set(
          'queryToSearch',
          this.queryToSearch
        );
        this.http.get(apiUrl, { params }).subscribe((data) => {
          //console.log(data);
        });

        //end req
      }
    }
  }
}
