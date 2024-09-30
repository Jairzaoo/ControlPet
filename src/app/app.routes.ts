import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { AppComponent } from './app.component';

export const routes: Routes = [
   { path: 'login', component: LoginComponent },
  { path: '', redirectTo: '/login', pathMatch: 'full' } // Rota padrão redireciona para login
];


