import { TestBed } from '@angular/core/testing';

import { SearchSharingService } from './search-sharing.service';

describe('SearchSharingService', () => {
  let service: SearchSharingService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SearchSharingService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
