import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { WelcomeComponent } from './welcome/welcome.component';
import { SearchComponent } from './search/search.component';

const routes: Routes = [
  { path: '', component: WelcomeComponent, title: 'BalanceBrief' },
  { path: 'search', component: SearchComponent, title: 'BalanceBrief' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
