import { Component, OnInit } from '@angular/core';
import { SearchSharingService } from '../search-sharing.service';
import { HttpClient, HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'],
})
export class SearchComponent implements OnInit {
  inputValue: string = '';
  queryToSearch: string = '';
  data: any = {};
  apiURL: string = 'http://127.0.0.1:8000/';
  gradientStyle: string;
  showImage = false;

  constructor(
    private searchSharingService: SearchSharingService,
    private http: HttpClient
  ) {
    const queryToSearch: string = this.searchSharingService.getSearchData();
    if (queryToSearch != '') {
      this.inputValue = queryToSearch;
    }
    this.gradientStyle = this.generateRandomGradient();
  }

  ngOnInit(): void {
    const queryToSearch: string = this.searchSharingService.getSearchData();
    if (queryToSearch !== '') {
      const apiUrl = this.apiURL + 'query';
      const params = new HttpParams().set('queryToSearch', queryToSearch);

      this.http.get(apiUrl, { params }).subscribe((data: any) => {
        if (data) {
          //do stuff id data
        }
      });

      this.showImage = true;

      setTimeout(() => {
        this.showImage = false;
      }, 10000); // 10 seconds in milliseconds
    }

    this.http.get(this.apiURL + 'grab').subscribe((response: any) => {
      this.data = response;
    });
  }

  get searchData(): string {
    return this.searchSharingService.getSearchData();
  }

  generateRandomGradient() {
    const randomColor1 = this.getRandomColor();
    const randomColor2 = this.getRandomColor();
    return `linear-gradient(to right, ${randomColor1}, ${randomColor2})`;
  }

  getRandomColor() {
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    return `rgb(${r},${g},${b})`;
  }

  onSearch(event: KeyboardEvent) {
    if (this.inputValue != '') {
      if (event.key === 'Enter') {
        this.showImage = true;
        setTimeout(() => {
          this.showImage = false;
        }, 10000); // 10 seconds in milliseconds
        this.queryToSearch = this.inputValue;
        //console.log(this.queryToSearch);
        //start req
        const apiUrl = this.apiURL + 'query';
        const params = new HttpParams().set(
          'queryToSearch',
          this.queryToSearch
        );
        this.http.get(apiUrl, { params }).subscribe((data) => {
          //console.log(data);
        });

        //end req
        this.http.get(this.apiURL + 'grab').subscribe((response: any) => {
          this.data = response;
        });
      }
    }
  }
}
