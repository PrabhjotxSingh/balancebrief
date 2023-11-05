import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class SearchSharingService {
  private searchData: string = '';

  setSearchData(data: string) {
    this.searchData = data;
  }

  getSearchData() {
    return this.searchData;
  }
}
